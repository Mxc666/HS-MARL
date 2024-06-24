#!python
import sys
import os
import argparse
import logging
import time
import itertools
import io
import enum
import subprocess
from tempfile import NamedTemporaryFile

import pddl
from hipop.grounding.problem import Problem
from hipop.search.greedy import GreedySearch, OpenLinkHeuristic, PlanHeuristic, HaddVariant
from hipop.utils.profiling import start_profiling, stop_profiling
from hipop.utils.logger import setup_logging
from hipop.utils.io import output_ipc2020_hierarchical

LOGGER = logging.getLogger(__name__)


class EnumAction(argparse.Action):
    """
    Argparse action for handling Enums
    """

    def __init__(self, **kwargs):
        # Pop off the type value
        e = kwargs.pop("type", None)
        # Ensure an Enum subclass is provided
        if e is None:
            raise ValueError(
                "type must be assigned an Enum when using EnumAction")
        if not issubclass(e, enum.Enum):
            raise TypeError("type must be an Enum when using EnumAction")
        # Generate choices from the Enum
        kwargs.setdefault("choices", tuple(x.value for x in e))
        super(EnumAction, self).__init__(**kwargs)
        self._enum = e

    def __call__(self, parser, namespace, values, option_string=None):
        # Convert value back into an Enum
        e = self._enum(values)
        setattr(namespace, self.dest, e)

def main():
    parser = argparse.ArgumentParser(description="HDDL Grounding")
    parser.add_argument("domain", help="PDDL domain file", type=str)
    parser.add_argument("problem", help="PDDL problem file", type=str)
    parser.add_argument("-d", "--debug", help="activate debug logs",
                        action='store_const', dest="loglevel",
                        const=logging.DEBUG, default=logging.WARNING)
    parser.add_argument("-v", "--verbose", help="activate verbose logs",
                        action='store_const', dest="loglevel",
                        const=logging.INFO, default=logging.WARNING)
    parser.add_argument("-o", "--output-graph",
                        const='', default=None,
                        action='store', nargs='?',
                        help="generate output graphs")
    parser.add_argument("--trace-malloc", help="activate tracemalloc",
                        action='store_true')
    parser.add_argument("--profile", help="activate profiling",
                        action='store_true')
    parser.add_argument("--panda", help="path to the PANDA plan verifier",
                        type=str)

    def add_bool_arg(parser: argparse.ArgumentParser, name: str, dest: str, help: str, default: bool = False):
        group = parser.add_mutually_exclusive_group(required=False)
        group.add_argument('--' + name, dest=dest,
                           action='store_true', help=help)
        group.add_argument('--no-' + name, dest=dest,
                           action='store_false', help=f"do not {help}")
        parser.set_defaults(**{dest: default})
    add_bool_arg(parser, 'filter-rigid', 'rigid',
                 "use rigid relations to filter groundings", True)
    add_bool_arg(parser, 'filter-relaxed', 'relaxed',
                 "use delete-relaxation to filter groundings", True)
    add_bool_arg(parser, 'htn', 'htn',
                 "use pure HTN decomposition", True)
    add_bool_arg(parser, 'mutex', 'mutex',
                 "compute mutex on (motion) predicates", True)
    add_bool_arg(parser, 'inc-poset', 'incposet',
                 "use incremental poset impl.", False)

    parser.add_argument("--ol", help="heuristic to sort open links",
                        type=OpenLinkHeuristic, default=OpenLinkHeuristic.LIFO,
                        action=EnumAction)
    parser.add_argument("--plan", help="heuristic to sort plans",
                        type=PlanHeuristic, default=PlanHeuristic.DEPTH,
                        action=EnumAction)
    parser.add_argument("--hadd", help="Hadd variant",
                        type=HaddVariant, default=HaddVariant.HADD,
                        action=EnumAction)

    args = parser.parse_args()
    setup_logging(level=args.loglevel, without=['pddl'])

    tic = time.process_time()
    LOGGER.info("Parsing PDDL domain %s", args.domain)
    pddl_domain = pddl.parse_domain(args.domain, file_stream=True)
    LOGGER.info("Parsing PDDL problem %s", args.problem)
    pddl_problem = pddl.parse_problem(args.problem, file_stream=True)
    toc = time.process_time()
    LOGGER.warning("parsing duration: %.3f", (toc - tic))

    profiler = start_profiling(args.trace_malloc, args.profile)

    tic = time.process_time()
    LOGGER.info("Building HiPOP problem")
    problem = Problem(pddl_problem, pddl_domain, args.output_graph,
                args.rigid, args.relaxed, args.htn, mutex=args.mutex)
    toc = time.process_time()
    LOGGER.warning("grounding duration: %.3f", (toc - tic))

    stop_profiling(args.trace_malloc, profiler, "profile-grounding.stat")
    profiler = start_profiling(args.trace_malloc, args.profile)

    LOGGER.info("Solving problem")
    tic = time.process_time()
    alg = GreedySearch(problem, 
                        ol_heuristic=args.ol, 
                        plan_heuristic=args.plan,
                        hadd_variant=args.hadd,
                        inc_poset=args.incposet)
    plan = alg.solve(output_current_plan=args.output_graph)
    toc = time.process_time()
    LOGGER.warning("solving duration: %.3f", (toc - tic))

    stop_profiling(args.trace_malloc, profiler, "profile-shop.stat")

    if plan is None:
        LOGGER.error("No plan found!")
        sys.exit(1)

    out_plan = io.StringIO()
    output_ipc2020_hierarchical(plan, problem, out_plan)
    plan = out_plan.getvalue()
    print(plan)
    out_plan.close()

    if args.panda:
        with NamedTemporaryFile(dir='.', suffix=".plan", delete=False) as tmpfile:
            plan_file = tmpfile.name
            LOGGER.info("writing plan to file %s", plan_file)
            tmpfile.write(plan.encode(encoding='utf-8'))

        cmd = [args.panda,
               "-verify",
               args.domain,
               args.problem,
               plan_file]
        LOGGER.info("verification command: %s", cmd)
        verificator = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        verification = verificator.stdout.read().decode(encoding='utf-8')
        print(verification)

if __name__ == '__main__':
    main()
