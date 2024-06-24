import sys
import unittest
import logging
import io

import pddl

from hipop.problem.problem import Problem
from hipop.search.plan import HierarchicalPartialPlan
from hipop.utils.io import output_ipc2020

logger = logging.getLogger(__name__)

class TestPlan(unittest.TestCase):

    def test_sequence(self):
        logging.getLogger('hipop.search.plan').setLevel(logging.WARNING)
        plan = HierarchicalPartialPlan(None)
        plan.append_action('A')
        plan.append_action('B')
        plan.append_action('A')
        seq_plan = list(plan.sequential_plan())
        self.assertEqual(seq_plan, [(0, 'A'), (1, 'B'), (2, 'A')])

    def test_task(self):
        logging.getLogger('hipop.search.plan').setLevel(logging.DEBUG)
        plan = HierarchicalPartialPlan(None)
        a1 = plan.append_action('A')
        b1 = plan.append_action('B')
        a2 = plan.append_action('A')
        t = plan.add_task('T')
        self.assertIn(t, plan.hierarchy_flaws)
        self.assertTrue(plan.hierarchy(t, "m", [0, 1]))
        #logger.info('%s', plan.graphviz_string())
        self.assertFalse(plan.hierarchy(t, "m", [a1, 6]))
        self.assertFalse(list(plan.hierarchy_flaws))

    def test_output(self):
        logging.getLogger('hipop.search.plan').setLevel(logging.DEBUG)
        plan = HierarchicalPartialPlan(None)
        a1 = plan.append_action('A')
        b1 = plan.append_action('B')
        a2 = plan.append_action('A')
        t = plan.add_task('T')
        plan.hierarchy(t, "m", [0, 1])
        root = plan.add_task('__top')
        plan.hierarchy(root, '__top_method', [b1, t])
        out_plan = io.StringIO()
        output_ipc2020(plan, out_plan)
        logger.info('%s', out_plan.getvalue())

def main():
    logformat = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG,
                        format=logformat)
    unittest.main()


if __name__ == '__main__':
    main()
