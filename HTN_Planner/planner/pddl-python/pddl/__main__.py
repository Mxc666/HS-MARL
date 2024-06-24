#!/usr/bin/env python
"""PDDL Parser entry point."""

import argparse
import logging
import sys

from .parsing import parse_domain, parse_problem
from .writer import write_problem, write_domain
from .logger import LOGGER, setup_logging


def main():
    """Implement main function."""
    parser = argparse.ArgumentParser(prog='pddl')
    subparsers = parser.add_subparsers(help='sub-commands')

    # parse domain
    def parser_domain_func(args):
        """parse_domain command function."""
        model = parse_domain(args.file, file_stream=True)
        LOGGER.info("PDDL domain: %s", model.name)
        LOGGER.info("PDDL requirements: %d", len(model.requirements))
        LOGGER.debug("PDDL requirements: %s", ", ".join(model.requirements))
        LOGGER.info("PDDL types: %d", len(model.types))
        LOGGER.debug("PDDL types: %s", ", ".join(map(str, model.types)))
        LOGGER.info("PDDL predicates: %d", len(model.predicates))
        LOGGER.debug("PDDL predicates: %s",
                     ", ".join(map(str, model.predicates)))
        LOGGER.info("PDDL actions: %d", len(model.actions))
        LOGGER.debug("PDDL actions: %s",
                     ", ".join(a.name for a in model.actions))
        LOGGER.info("PDDL tasks: %d", len(model.tasks))
        LOGGER.debug("PDDL tasks: %s",
                     ", ".join(t.name for t in model.tasks))
        LOGGER.info("PDDL methods: %d", len(model.methods))
        LOGGER.debug("PDDL methods: %s",
                     ", ".join(m.name for m in model.methods))
        if args.pprint:
            print(write_domain(model))

    parser_domain = subparsers.add_parser('parse_domain',
                                          # aliases=['d', 'domain'],
                                          help='parse a PDDL domain')
    parser_domain.add_argument('file', type=str, help='PDDL domain file')
    parser_domain.set_defaults(func=parser_domain_func)

    # parse problem
    def parser_problem_func(args):
        """parse_problem command function."""
        model = parse_problem(args.file, file_stream=True)
        LOGGER.info("PDDL problem: %s", model.name)
        LOGGER.info("PDDL domain: %s", model.domain)
        LOGGER.info("PDDL objects: %d", len(model.objects))
        LOGGER.info("PDDL init size: %d", len(model.init))
        if args.pprint:
            print(write_problem(model))

    parser_problem = subparsers.add_parser('parse_problem',
                                           # aliases=['p', 'problem'],
                                           help='parse a PDDL problem')
    parser_problem.add_argument('file', type=str, help='PDDL problem file')
    parser_problem.set_defaults(func=parser_problem_func)

    # common args
    parser.add_argument("-d", "--debug", help="Activate debug logs",
                        action='store_const', dest="loglevel",
                        const=logging.DEBUG, default=logging.WARNING)
    parser.add_argument("-v", "--verbose", help="Activate verbose logs",
                        action='store_const', dest="loglevel",
                        const=logging.INFO, default=logging.WARNING)
    parser.add_argument('-p', '--pprint',
                        help='pretty print the parsed model',
                        action='store_true')
    args = parser.parse_args()
    setup_logging(args.loglevel)

    try:
        args.func
    except AttributeError:
        print("subcommand missing!")
        parser.print_help()
        sys.exit(-1)

    args.func(args)


if __name__ == '__main__':
    main()
