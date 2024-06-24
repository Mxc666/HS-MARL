import sys
import unittest
import logging

import pddl

from hipop.problem.problem import Problem
from hipop.utils.logger import setup_logging


class TestGrounding(unittest.TestCase):

    domain = """(define (domain test-grounding)
        (:types B - A C)
        (:predicates (pred ?x - A))
        (:action test-action
         :parameters (?x - A ?y - C)
         :precondition (and (pred ?y) (not (pred ?x)))
         )
        )
        """
    problem = """(define (problem test-grounding-pb)
        (:domain test-grounding)
        (:objects a - A b - B c1 c2 - C)
        (:init
            (pred c1)
            (pred b)
        )
        )
        """

    def test_grounding(self):
        pddl_problem = pddl.parse_problem(self.problem)
        pddl_domain = pddl.parse_domain(self.domain)
        problem = Problem(pddl_problem, pddl_domain)
        logging.getLogger().debug("A: %s", problem.objects_of('A'))
        logging.getLogger().debug("B: %s", problem.objects_of('B'))
        logging.getLogger().debug("C: %s", problem.objects_of('C'))
        self.assertTrue(problem.action('(test-action a c1)'))


def main():
    setup_logging(logging.DEBUG)
    unittest.main()


if __name__ == '__main__':
    main()
