import sys
import unittest
import logging
import io

import pddl
from hipop.problem.problem import Problem
from hipop.search.shop import SHOP
from hipop.utils.io import output_ipc2020_hierarchical
from hipop.utils.logger import setup_logging

class TestIpc(unittest.TestCase):

    def test_empty_plan(self):
        logging.getLogger().setLevel(logging.WARNING)
        domain = """(define (domain test-domain)
            (:requirements :typing :hierarchy)
            (:task task1 :parameters ())
            (:method donothing
                :parameters ()
                :task (task1)
                :subtasks (and )
            ))
        """
        problem = """(define (problem p1)
            (:domain  test-domain)
            (:objects )
            (:htn
                :parameters ()
                :subtasks (and
                    (task0 (task1))
                ))
            (:init ))
        """
        pddl_problem = pddl.parse_problem(problem)
        pddl_domain = pddl.parse_domain(domain)
        problem = Problem(pddl_problem, pddl_domain)
        alg = SHOP(problem, no_duplicate_search=True,
             hierarchical_plan=True,
             poset_inc_impl=True)
        plan = alg.find_plan(problem.init, problem.goal_task)
        seq_plan = list(plan.sequential_plan())
        self.assertEqual(len(seq_plan), 2)
        self.assertEqual("(__top )", seq_plan[0][1].operator)
        self.assertEqual("(task1 )", seq_plan[1][1].operator)
        out_plan = io.StringIO()
        output_ipc2020_hierarchical(plan, out_plan)
        print(out_plan.getvalue())


    def test_forall(self):
        logging.getLogger().setLevel(logging.DEBUG)
        logger = logging.getLogger('test_forall')
        domain = """(define (domain test-domain)
            (:requirements :typing :hierarchy)
            (:types A)
            (:predicates (foo ?a - A))
            (:task task1 :parameters ())
            (:method donothing
                :parameters ()
                :task (task1)
                :subtasks (and (noop))
            )
            (:action noop
                :parameters ()
                :precondition (forall (?a - A) (foo ?a))
            ))
        """
        problem = """(define (problem p1)
            (:domain  test-domain)
            (:objects a b c d - A )
            (:htn
                :parameters ()
                :subtasks (and (task0 (task1)))
            )
            (:init
                (foo a)
                (foo b)
                (foo c)
                (foo d)
            ))
        """
        pddl_problem = pddl.parse_problem(problem)
        pddl_domain = pddl.parse_domain(domain)
        logger.info(pddl_domain.get_action('noop').precondition)
        problem = Problem(pddl_problem, pddl_domain)
        alg = SHOP(problem, no_duplicate_search=True,
             hierarchical_plan=True,
             poset_inc_impl=True)
        plan = alg.find_plan(problem.init, problem.goal_task)
        seq_plan = list(plan.sequential_plan())
        logger.info(seq_plan)
        self.assertEqual(len(seq_plan), 3)
        self.assertEqual("(__top )", seq_plan[0][1].operator)
        self.assertEqual("(task1 )", seq_plan[1][1].operator)
        self.assertEqual("(noop )", seq_plan[2][1].operator)
        out_plan = io.StringIO()
        output_ipc2020_hierarchical(plan, out_plan)
        print(out_plan.getvalue())

def main():
    setup_logging(level=logging.DEBUG)
    unittest.main()


if __name__ == '__main__':
    main()
