import sys
import os
import argparse
import logging
import time
import itertools

import pddl
from hipop.problem.problem import Problem
from hipop.utils.profiling import start_profiling, stop_profiling
from hipop.utils.logger import setup_logging

LOGGER = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser(description="HDDL Grounding")
    parser.add_argument("domain", help="PDDL domain file", type=str)
    parser.add_argument("problem", help="PDDL problem file", type=str)
    parser.add_argument("-d", "--debug", help="Activate debug logs",
                        action='store_const', dest="loglevel",
                        const=logging.DEBUG, default=logging.WARNING)
    parser.add_argument("-v", "--verbose", help="Activate verbose logs",
                        action='store_const', dest="loglevel",
                        const=logging.INFO, default=logging.WARNING)
    parser.add_argument("--trace-malloc", help="Activate tracemalloc",
                        action='store_true')
    parser.add_argument("--profile", help="Activate profiling",
                        action='store_true')
    args = parser.parse_args()

    setup_logging(level=args.loglevel)

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
    _ = Problem(pddl_problem, pddl_domain)
    toc = time.process_time()
    LOGGER.warning("building problem duration: %.3f", (toc - tic))

    stop_profiling(args.trace_malloc, profiler, "profile-grounding.stat")

if __name__ == '__main__':
    main()
