import sys
import unittest
import logging

import pddl

from hipop.problem import Problem


class TestTypes(unittest.TestCase):

    domain = """(define (domain test-typeset)
        (:types
            type-A type-B - supertype-A
            type-C - type-A
            type-D
            )
        (:constants
            obj-A - type-A
            obj-O
            )
        )
        """
    problem = """(define (problem test-typeset-pb)
        (:domain test-typeset)
        (:objects a1 - type-A b1 b2 - type-B c1 - type-C )
        (:init)
        )
        """

    def test_basic_types(self):
        pddl_problem = pddl.parse_problem(self.problem)
        pddl_domain = pddl.parse_domain(self.domain)
        problem = Problem(pddl_problem, pddl_domain)
        self.assertIn('type-A', problem.types)
        self.assertIn('type-B', problem.types)
        self.assertIn('type-C', problem.types)
        self.assertIn('type-D', problem.types)
        self.assertIn('supertype-A', problem.types)
        self.assertNotIn('type-E', problem.types)

    def test_subtypes(self):
        pddl_problem = pddl.parse_problem(self.problem)
        pddl_domain = pddl.parse_domain(self.domain)
        problem = Problem(pddl_problem, pddl_domain)
        self.assertIn('type-A', problem.subtypes('supertype-A'))
        self.assertIn('type-C', problem.subtypes('supertype-A'))
        self.assertNotIn('type-C', problem.subtypes('type-B'))
        self.assertNotIn('type-D', problem.subtypes('type-A'))

    def test_objects(self):
        pddl_problem = pddl.parse_problem(self.problem)
        pddl_domain = pddl.parse_domain(self.domain)
        problem = Problem(pddl_problem, pddl_domain)
        self.assertIn('obj-A', problem.objects_of('type-A'))
        self.assertIn('obj-A', problem.objects_of('supertype-A'))
        self.assertIn('a1', problem.objects_of('type-A'))
        self.assertIn('a1', problem.objects_of('supertype-A'))
        self.assertIn('b1', problem.objects_of('type-B'))
        self.assertIn('obj-O', problem.objects_of('object'))
        self.assertNotIn('c1', problem.objects_of('type-B'))


def main():
    logformat = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG,
                        format=logformat)
    unittest.main()


if __name__ == '__main__':
    main()
