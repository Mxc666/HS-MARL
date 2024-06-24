import sys
import unittest
import logging
import timeit

import pddl

from hipop.problem.problem import Problem
from hipop.search.search import  Search
from hipop.search.heuristics import Zero

class TestAction(unittest.TestCase):

    domain = """(define (domain test-action)
        (:predicates (p ?x))
        (:action ap
         :parameters (?x ?y)
         :precondition (and (p ?x) (not (p ?y)))
         :effect (and
            (p ?y)
            )
         )
        )
        """
    problem = """(define (problem test-action-pb)
        (:domain test-action)
        (:objects a b c)
        (:init
            (p a)
            )
        (:goal
            (and (p b) (p c) (p a)
            ) )
        )
        """

    def test_action(self):
        pddl_problem = pddl.parse_problem(self.problem)
        pddl_domain = pddl.parse_domain(self.domain)
        problem = Problem(pddl_problem, pddl_domain)
        state = problem.init

        print("Starting search")
        search_algo = Search(problem, Zero())
        search_algo.solve()



def main():
    logformat = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG,
                        format=logformat)
    unittest.main()


if __name__ == '__main__':
    main()
