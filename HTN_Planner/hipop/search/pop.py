import sys
import random
import math
import logging
from collections import deque
from collections import defaultdict
from copy import deepcopy, copy
from sortedcontainers import SortedKeyList

from ..problem.problem import Problem
from ..problem.operator import GroundedTask
from .plan import HierarchicalPartialPlan
from ..utils.logic import Literals

LOGGER = logging.getLogger(__name__)


class POP():

    def __init__(self, problem, shoplikeSearch=False, dq=False, count=20, ol = False):
        self.__problem = problem
        self.__stop_planning = False
        # todo: we can initialize different OpenLists using parameters and heuristic functions
        self.OPEN = SortedKeyList(key=lambda x: x.f)
        self.OPEN_local_OL = []
        self.__ol_boost = ol
        self.__shoplike = shoplikeSearch
        self.__dual_queue = dq
        self.__count = count
        self.OPEN_ShoplikeLIFO = deque()

    @property
    def problem(self):
        return self.__problem

    @property
    def COUNT(self):
        return self.__count

    @property
    def OL_BOOST(self) -> bool:
        return self.__ol_boost

    @property
    def empty_openlist(self):
        if self.__shoplike:
            return len(self.OPEN_ShoplikeLIFO) < 1
        return len(self.OPEN) < 1

    @property
    def empty_local_OL_openlist(self):
        return len(self.OPEN_local_OL) < 1

    def stop(self):
        self.__stop_planning = True

    def get_best_partialPlan(self) -> HierarchicalPartialPlan:
        """
        Returns the best partial plan from the OPEN list
        according to an heuristic.
        Actually, this heuristic is random.
        :param flaws: the set of flaws
        :return: selected flaw
        """
        if self.__shoplike:
            return self.OPEN_ShoplikeLIFO.pop()
        elif not self.OL_BOOST or self.empty_local_OL_openlist:
            return self.OPEN[0]
        else:
            return self.OPEN_local_OL[0]

    """
    Here we're using an 'alternate' method to select. 
    We can boost the heuristic lowering queue.
    :returns: best partial plan, queue from where it was taken, h1 score, h2 score
    """

    def get_partialPlan_from_queues(self, heur_1_openList, heur_2_openList, h1_score, h2_score, prev_h1,
                                    prev_h2) -> HierarchicalPartialPlan:

        LOGGER.debug("Queues status:\n  min f(n) for h1: {} -- h1 score: {}\n  min f(n) for h2: {} -- h2 "
                     "score: {}".format(prev_h1, h1_score, prev_h2, h2_score))

        if self.OL_BOOST and not self.empty_local_OL_openlist:
            n = self.OPEN_local_OL[0]
            return n, self.OPEN_local_OL, h2_score, h1_score

        if h2_score >= h1_score:
            if len(heur_2_openList) > 0:
                h2_score -= 1
                primary_open = heur_2_openList
                secondary_open = heur_1_openList
            else:
                h1_score -= 1
                primary_open = heur_1_openList
                secondary_open = heur_2_openList
        else:
            if len(heur_1_openList) > 0:
                h1_score -= 1
                primary_open = heur_1_openList
                secondary_open = heur_2_openList
            else:
                h2_score -= 1
                primary_open = heur_2_openList
                secondary_open = heur_1_openList

        if len(primary_open) > 0:
            n = primary_open[0]
            return n, primary_open, h2_score, h1_score
        elif len(secondary_open) > 0:
            n = secondary_open[0]
            return n, secondary_open, h2_score, h1_score
        else:
            LOGGER.warning("No queue from where to pop")
            n = self.OPEN_ShoplikeLIFO.pop()
            self.OPEN_ShoplikeLIFO.append(n)
            return n, self.OPEN_ShoplikeLIFO, h2_score, h1_score

        return None, None, math.inf, math.inf

    @staticmethod
    def print_plan(plan):
        import io
        from hipop.utils.io import output_ipc2020_hierarchical
        out_plan = io.StringIO()
        output_ipc2020_hierarchical(plan, out_plan)

    def solve(self, problem, heur_1, heur_2, h_add_variant, open_link_sort, mutex):
        """
         Searches for a plan that accomplishes tasks in state.
        :param heur_1: first heuristic
        :param heur_2: second heuristic
        :param problem: problem to solve
        :return: the plan
        """
        self.__stop_planning = False
        plan = HierarchicalPartialPlan(self.problem, init=True, goal=True, poset_inc_impl=True,
            h_add_variant=h_add_variant, open_link_sort=open_link_sort, mutex=mutex)
        plan.add_task(problem.goal_task)

        if self.__shoplike:
            result = self.seek_plan_shoplike(None, plan)
        elif self.__dual_queue:
            result = self.seek_plan_dualqueue(None, plan, heur_1, heur_2)
        else:
            result = self.seek_plan(None, plan, heur_1)
        if result:
            result.write_dot("plan.dot")
        return result

    def seek_plan_shoplike(self, state, pplan) -> HierarchicalPartialPlan:
        if self.__stop_planning: return None

        LOGGER.debug("state: %s", state)
        LOGGER.debug("partial_plan: %s", pplan)
        LOGGER.debug("initial partial plan: %s", list(pplan.sequential_plan()))

        # Initial partial plan
        self.OPEN_ShoplikeLIFO.append(pplan)
        CLOSED = list()

        # main search loop
        while bool(self.OPEN_ShoplikeLIFO) and not self.__stop_planning:
            current_pplan = self.get_best_partialPlan()
            if not current_pplan in CLOSED:
                CLOSED.append(current_pplan)

            if LOGGER.isEnabledFor(logging.DEBUG):
                current_pplan.write_dot(f"current-plan.dot")
            LOGGER.debug("current plan id: %s (cost function: %s)", id(current_pplan), current_pplan.f)

            if not current_pplan.has_flaws:
                # if we cannot find an operator with flaws, then the plan is good
                LOGGER.warning("returning plan: %s", list(current_pplan.sequential_plan()))
                return current_pplan

            if not current_pplan.compute_flaw_resolvers():
                LOGGER.debug(
                    "current plan %d has no resolver: closing plan", id(current_pplan))
                continue

            LOGGER.info("Current plan has {} flaws ({}/{} : {}/{} : {}/{})".format(
                len(current_pplan.pending_abstract_flaws) + len(current_pplan.pending_open_links) + len(
                    current_pplan.pending_threats),
                len(current_pplan.pending_abstract_flaws), len(
                    current_pplan.abstract_flaws),
                len(current_pplan.pending_open_links), len(
                    current_pplan.open_links),
                len(current_pplan.pending_threats), len(current_pplan.threats)))

            successors = list()
            while current_pplan.has_pending_flaws:
                if len(current_pplan.pending_threats) > 0:
                    current_flaw, _ = current_pplan.pending_threats.pop(0)
                elif len(current_pplan.pending_open_links) > 0:
                    if len(current_pplan.pending_abstract_flaws) > 0:
                        best_ol, _ = current_pplan.pending_open_links[0]
                        best_abstract = current_pplan.pending_abstract_flaws[0]
                        if current_pplan.poset.is_less_than(best_ol.step, best_abstract):
                            current_flaw, _ = current_pplan.pending_open_links.pop(0)
                        else:
                            current_flaw = current_pplan.pending_abstract_flaws.pop(0)
                    else:
                        current_flaw, _ = current_pplan.pending_open_links.pop(0)

                else:
                    current_flaw = current_pplan.pending_abstract_flaws.pop(0)

                LOGGER.debug("current flaw: %s", current_flaw)

                resolvers = current_pplan.resolvers(current_flaw)
                for r in resolvers:
                    # LOGGER.debug("resolver: %s", id(r))
                    if r in CLOSED or r in self.OPEN_ShoplikeLIFO:
                        LOGGER.debug("plan %s already in CLOSED set", id(r))
                    else:
                        successors.append(r)

            LOGGER.debug("   just added %d plans to open lists", len(successors))

            successors.reverse()
            for plan in successors:
                self.OPEN_ShoplikeLIFO.append(plan)

            LOGGER.info("Open List size: %d", len(self.OPEN_ShoplikeLIFO))
            LOGGER.info("Closed List size: %d", len(CLOSED))
        # end while
        LOGGER.warning("nothing leads to solution")
        return None


    def seek_plan_dualqueue(self, state, pplan, h1 = 'htdg', h2 = 'f') -> HierarchicalPartialPlan:
        """
        Implements a dual-queue best first search
        """
        funcdict = {
            'f':    lambda x: x.f,
            'htdg': lambda x: x.htdg,
            'hadd': lambda x: x.hadd,
            'htdg_min': lambda x: x.htdg_min_hadd,
            'htdg_max': lambda x: x.htdg_max_hadd,
            'htdg_max_deep' : lambda x: x.htdg_max_hadd_deep,
            'htdg_min_deep' : lambda x: x.htdg_min_hadd_deep,
        }

        OPEN_heur_1 = SortedKeyList(key=funcdict[h1])
        OPEN_heur_2 = SortedKeyList(key=funcdict[h2])
        heur_score_1 = heur_score_2 = 1
        min_heur_1 = min_heur_2 = math.inf

        if self.__stop_planning:
            return None

        LOGGER.debug("state: %s", state)
        LOGGER.debug("partial_plan: %s", pplan)
        LOGGER.debug("initial partial plan: %s", list(pplan.sequential_plan()))

        # Initial partial plan
        OPEN_heur_1.add(pplan)
        OPEN_heur_2.add(pplan)
        CLOSED = list()
        count = 1  # counter: if in X loops heuristics doesn't improve the min, resets the min
        not_improving = False
        min_local_heur_1, min_local_heur_2 = math.inf, math.inf

        # main search loop
        while (OPEN_heur_2 or OPEN_heur_1) and not self.__stop_planning:

            if not_improving:
                current_pplan = self.OPEN_ShoplikeLIFO.pop()
                self.OPEN_ShoplikeLIFO.append(current_pplan)
            else:
                current_pplan, _, heur_score_2, heur_score_1 = self.get_partialPlan_from_queues(
                    OPEN_heur_1, OPEN_heur_2,
                    heur_score_1, heur_score_2,
                    min_heur_1, min_heur_2)
            not_improving = False

            if LOGGER.isEnabledFor(logging.DEBUG):
                current_pplan.write_dot(f"current-plan.dot")
            LOGGER.debug("current plan id: %s (cost function: f = %s, h1 = %s, h2 = %s)", id(current_pplan),
                         current_pplan.f, funcdict[h1](current_pplan), funcdict[h2](current_pplan))

            if not current_pplan.has_flaws:
                # if we cannot find an operator with flaws, then the plan is good
                LOGGER.warning("returning plan: %s", list(current_pplan.sequential_plan()))
                return current_pplan

            if funcdict[h1](current_pplan) == 0 and  funcdict[h2](current_pplan) == 0:
                LOGGER.info("Heuristics are empty!")

            if current_pplan in CLOSED:
                try:
                    OPEN_heur_2.remove(current_pplan)
                except ValueError:
                    pass
                try:
                    OPEN_heur_1.remove(current_pplan)
                except ValueError:
                    pass
                try:
                    self.OPEN_ShoplikeLIFO.remove(current_pplan)
                except ValueError:
                    pass
                if self.OL_BOOST and not self.empty_local_OL_openlist:
                    self.OPEN_local_OL.remove(current_pplan)
                LOGGER.debug(
                    "current plan %d in CLOSED: removing plan", id(current_pplan))
                continue
            if not current_pplan.compute_flaw_resolvers():
                try:
                    OPEN_heur_2.remove(current_pplan)
                except ValueError:
                    pass
                try:
                    OPEN_heur_1.remove(current_pplan)
                except ValueError:
                    pass
                try:
                    self.OPEN_ShoplikeLIFO.remove(current_pplan)
                except ValueError:
                    pass
                if self.OL_BOOST and not self.empty_local_OL_openlist:
                    try:
                        self.OPEN_local_OL.remove(current_pplan)
                    except ValueError:
                        pass
                CLOSED.append(current_pplan)
                LOGGER.debug(
                    "current plan %d has no resolver: closing plan", id(current_pplan))
                continue

            if funcdict[h2](current_pplan) >= min_heur_2 and funcdict[h1](current_pplan) >= min_heur_1:
                count += 1
                if funcdict[h2](current_pplan) < min_local_heur_2:
                    min_local_heur_2 = funcdict[h2](current_pplan)
                if funcdict[h1](current_pplan) < min_local_heur_1:
                    min_local_heur_1 = funcdict[h1](current_pplan)
            else:
                count = 1
                if funcdict[h2](current_pplan) < min_heur_2:
                    min_heur_2 = funcdict[h2](current_pplan)
                    heur_score_2 += 10
                if funcdict[h1](current_pplan) < min_heur_1:
                    min_heur_1 = funcdict[h1](current_pplan)
                    heur_score_1 += 10

            # Mécanisme pour sortir d'un plateau
            if count == self.COUNT:
                count = 1
                min_heur_2 = min_local_heur_2
                min_heur_1 = min_local_heur_1
                min_local_heur_2 = math.inf
                min_local_heur_1 = math.inf
                not_improving = True

            LOGGER.debug("Count {}".format(count))

            LOGGER.info("Current plan has {} flaws ({} : {} : {})".format(
                len(current_pplan.pending_abstract_flaws) + len(current_pplan.pending_open_links) + len(
                    current_pplan.pending_threats),
                len(current_pplan.pending_abstract_flaws),
                len(current_pplan.pending_open_links),
                len(current_pplan.pending_threats)))

            current_flaw = current_pplan.get_best_flaw()
            LOGGER.debug("resolver candidate: %s", current_flaw)
            # If it's open link, try tto solve all it resolvers.

            close_plan = not current_pplan.has_pending_flaws

            resolvers = current_pplan.resolvers(current_flaw)
            i = 0

            for r in resolvers:
                i += 1
                LOGGER.debug("resolver: %s", id(r))
                if LOGGER.isEnabledFor(logging.DEBUG):
                    r.write_dot(f"plan-{id(r)}.dot")
                if r in CLOSED:
                    LOGGER.debug("plan %s already in CLOSED set", id(r))
                else:
                    if (funcdict[h1](r) == 0 and funcdict[h2](r) == 0) or (funcdict[h1](r) > 0 and funcdict[h2](r) > 0):
                        OPEN_heur_2.add(r)
                        OPEN_heur_1.add(r)
                    elif funcdict[h2](r) == 0 and funcdict[h1](r) > 0:
                        OPEN_heur_1.add(r)
                    elif funcdict[h1](r) == 0 and funcdict[h2](r) > 0:
                        OPEN_heur_2.add(r)
                    self.OPEN_ShoplikeLIFO.append(r)
                    if self.OL_BOOST and current_flaw in current_pplan.open_links:
                        self.OPEN_local_OL.append(r)

            LOGGER.debug("   just added %d plans to open lists", i)

            if close_plan:
                LOGGER.debug("closing current plan")
                CLOSED.append(current_pplan)
                try:
                    OPEN_heur_2.remove(current_pplan)
                except ValueError:
                    pass
                try:
                    OPEN_heur_1.remove(current_pplan)
                except ValueError:
                    pass
                try:
                    self.OPEN_ShoplikeLIFO.remove(current_pplan)
                except ValueError:
                    pass
                if self.OL_BOOST and not self.empty_local_OL_openlist:
                    try:
                        self.OPEN_local_OL.remove(current_pplan)
                    except ValueError:
                        pass
            LOGGER.info("Open List 1 size: %d - Open List 2 size: %d", len(OPEN_heur_1), len(OPEN_heur_2))
            LOGGER.info("Closed List size: %d", len(CLOSED))
        # end while
        LOGGER.warning("nothing leads to solution")
        return None

    def seek_plan(self, state, pplan, h='f') -> HierarchicalPartialPlan:
        funcdict = {
            'f': lambda x: x.f,
            'htdg': lambda x: x.htdg,
            'hadd': lambda x: x.hadd,
            'htdg_min': lambda x: x.htdg_min_hadd,
            'htdg_max': lambda x: x.htdg_max_hadd,
            'htdg_max_deep': lambda x: x.htdg_max_hadd_deep,
            'htdg_min_deep': lambda x: x.htdg_min_hadd_deep,
        }
        self.OPEN = SortedKeyList(key=funcdict[h])
        LOGGER.debug("Solving with heuristic %s", h)

        LOGGER.debug("state: %s", state)
        LOGGER.debug("partial_plan: %s", pplan)
        LOGGER.debug("initial partial plan: %s", list(pplan.sequential_plan()))

        # Initial partial plan
        self.OPEN.add(pplan)
        CLOSED = list()

        # main search loop
        while not self.empty_openlist and not self.__stop_planning:

            current_pplan = self.get_best_partialPlan()
            if LOGGER.isEnabledFor(logging.DEBUG):
                current_pplan.write_dot(f"current-plan.dot")
            LOGGER.debug("current plan id: %s (cost function: %s)", id(current_pplan), current_pplan.f)

            if not current_pplan.has_flaws:
                # if we cannot find an operator with flaws, then the plan is good
                LOGGER.warning("returning plan: %s", list(current_pplan.sequential_plan()))
                return current_pplan

            if current_pplan in CLOSED:
                self.OPEN.remove(current_pplan)
                LOGGER.debug(
                    "current plan %d in CLOSED: removing plan", id(current_pplan))
                if self.OL_BOOST and not self.empty_local_OL_openlist:
                    self.OPEN_local_OL.remove(current_pplan)
                continue
            if not current_pplan.compute_flaw_resolvers():
                self.OPEN.remove(current_pplan)
                CLOSED.append(current_pplan)
                LOGGER.debug(
                    "current plan %d has no resolver: closing plan", id(current_pplan))
                if self.OL_BOOST and not self.empty_local_OL_openlist:
                    self.OPEN_local_OL.remove(current_pplan)
                continue

            LOGGER.info("Current plan has {} flaws ({} : {} : {})".format(
                len(current_pplan.pending_abstract_flaws) + len(current_pplan.pending_open_links) + len(
                    current_pplan.pending_threats),
                len(current_pplan.pending_abstract_flaws),
                len(current_pplan.pending_open_links),
                len(current_pplan.pending_threats)))

            current_flaw = current_pplan.get_best_flaw()
            LOGGER.debug("resolver candidate: %s", current_flaw)
            # If it's open link, try tto solve all it resolvers.

            close_plan = not current_pplan.has_pending_flaws

            resolvers = current_pplan.resolvers(current_flaw)
            i = 0

            for r in resolvers:
                i += 1
                LOGGER.debug("resolver: %s", id(r))
                if LOGGER.isEnabledFor(logging.DEBUG):
                    r.write_dot(f"plan-{id(r)}.dot")
                if r in CLOSED:
                    LOGGER.debug("plan %s already in CLOSED set", id(r))
                else:
                    if self.OL_BOOST and current_flaw in current_pplan.open_links:
                        self.OPEN_local_OL.append(r)
                    self.OPEN.add(r)
            LOGGER.debug("   just added %d plans to open lists", i)

            if close_plan:
                LOGGER.debug("closing current plan")
                CLOSED.append(current_pplan)
                self.OPEN.remove(current_pplan)
                if self.OL_BOOST and not self.empty_local_OL_openlist:
                    try:  # in case it's the fist plan
                        self.OPEN_local_OL.remove(current_pplan)
                    except ValueError:
                        pass
            LOGGER.info("Open List size: %d", len(self.OPEN))
            LOGGER.info("Closed List size: %d", len(CLOSED))
        # end while
        LOGGER.warning("nothing leads to solution")
        return None
