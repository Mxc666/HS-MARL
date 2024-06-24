import sys
import unittest
import logging

import pddl

from hipop.problem.problem import Problem
from hipop.utils.logger import setup_logging

class TestAction(unittest.TestCase):

    domain = """(define (domain test-action)
        (:predicates (p ?x))
        (:constants a)
        (:task task
         :parameters (?x)
        )
        (:method method
         :parameters (?x)
         :task (task ?x)
         :subtasks (and
            (ap ?x a)
         )
        )
        (:action ap
         :parameters (?x ?y)
         :precondition (and (p ?x) (not (p ?y)))
         :effect (and
            (not (p ?x))
            (p ?y)
            )
         )
        )
        """
    problem = """(define (problem test-action-pb)
        (:domain test-action)
        (:objects b)
        (:init
            (p a)
            )
        )
        """

    def test_action(self):
        pddl_problem = pddl.parse_problem(self.problem)
        pddl_domain = pddl.parse_domain(self.domain)
        problem = Problem(pddl_problem, pddl_domain)
        ap_a_a = problem.action('(ap a a)')
        ap_a_b = problem.action('(ap a b)')
        ap_b_a = problem.action('(ap b a)')
        state = problem.init
        self.assertFalse(ap_a_a.is_applicable(state))
        self.assertTrue(ap_a_b.is_applicable(state))
        state = ap_a_b.apply(state)
        self.assertFalse(ap_a_b.is_applicable(state))
        self.assertTrue(ap_b_a.is_applicable(state))


def main():
    setup_logging(logging.DEBUG)
    unittest.main()


if __name__ == '__main__':
    main()
