from typing import Optional, Tuple, Any
import logging
import math
from collections import deque
import enum
from operator import itemgetter
from sortedcontainers import SortedKeyList

from ..grounding.problem import Problem
from ..plan.plan import HierarchicalPartialPlan
from ..plan.flaws import Threat, OpenLink, AbstractFlaw

LOGGER = logging.getLogger(__name__)


class OpenLinkHeuristic(enum.Enum):
    LIFO = 'lifo'
    SORTED = 'sorted'
    LOCAL = 'local'
    EARLIEST = 'earliest'
    SORTED_EARLIEST = 'sorted-earliest'
    LOCAL_EARLIEST = 'local-earliest'


class PlanHeuristic(enum.Enum):
    DEPTH = 'depth'
    BECHON = 'bechon'
    HADD_MAX = 'hadd-max'


class HaddVariant(enum.Enum):
    HADD = 'hadd'
    HADD_REUSE = 'hadd-reuse'
    HADD_AREUSE = 'hadd-areuse'

class GreedySearch:
    def __init__(self, problem: Problem,
                ol_heuristic: OpenLinkHeuristic = OpenLinkHeuristic.LIFO,
                plan_heuristic: PlanHeuristic = PlanHeuristic.DEPTH,
                hadd_variant: HaddVariant = HaddVariant.HADD,
                inc_poset: bool = False):
        '''
        problem: htn problem (grounding)
        ol_heuristic: Open Link Heuristic, default = OpenLinkHeuristic.LIFO, args = sorted
        plan_heuristic: Plan Heuristic, default = depth, args = hadd-max
        hadd_variant: Hadd Variant, default = hadd, args = hadd-reuse
        '''

        self.__ol_heuristic = ol_heuristic  # open link heuristic
        self.__plan_heuristic = plan_heuristic  # plan heuristic
        self.__hadd_bare = problem.hadd
        # self.__htdg: TDGHeuristic = namedtuple('h_TDG', ['cost', 'modifications', 'hadd_max'])
        self.__htdg = problem.tdg.heuristics  # Task Decomposition Graph (TDG) self.__heuristics[node]
        self.__hadd_variant = hadd_variant  # hadd variant
        
        # queue structures
        # open queue is (plan, sorted_flaws, h)
        # plan is raw plan, sorted_flaws is sorted plan (open links, (threats, abstract flaws))
        self.__OPEN = SortedKeyList(key=itemgetter(2))
        self.__CLOSED = list()  # list, self.__CLOSED.append(plan)
        self.__iterations = 0
        
        # initial plan
        plan = HierarchicalPartialPlan(problem, 
                                       init=True, 
                                       goal=True,
                                       inc_poset=inc_poset)
        # goal task
        if problem.has_root_task():
            root = problem.root_task()
            plan.add_task(root)  # add goal task
            
        sorted_flaws = self.__sort_flaws(plan)  # sorted flaws, included (open links, (threats, abstract flaws))
        h = self.__compute_heuristic(plan, 0) # compute heuristic, return a tuple
        self.__OPEN.add((plan, sorted_flaws, h))
        self.__CLOSED.append(plan)

    def __hadd(self, ol: OpenLink, plan: Optional[HierarchicalPartialPlan] = None) -> int:
        if self.__hadd_variant == HaddVariant.HADD_REUSE:
            if plan.has_ol_direct_resolvers(ol):
                return 0
        if self.__hadd_variant == HaddVariant.HADD_AREUSE:
            causal_links = plan.has_ol_direct_resolvers(ol)
            if bool(causal_links) and any(not plan.is_threatened(cl) for cl in causal_links):
                return 0
        return self.__hadd_bare(ol.atom)

    # update flaws (open links, (threats, abstract flaws))
    def __sort_flaws(self, plan: HierarchicalPartialPlan) -> SortedKeyList:
        flaws_queue = SortedKeyList(key=itemgetter(1))

        # First, test OL resolvability:
        for ol in plan.open_links:
            if not plan.is_ol_resolvable(ol):
                return None

        # return a sorted flaws
        if len(plan.threats) > 0:
            for threat in plan.threats:
                flaws_queue.add((threat, 0))

        else:
            seq_plan = list(map(itemgetter(0), plan.sequential_plan()))  # Return a sequential version of the plan.
            LOGGER.debug("sorting flaws on %s", seq_plan)
            
            first, second = 0, 0 
            max_ol = - math.inf  # initial max open link
            for ol in plan.open_links:  # for each open link
                if not plan.has_ol_direct_resolvers(ol): continue

                if self.__ol_heuristic == OpenLinkHeuristic.EARLIEST:  # earliest
                    first = seq_plan.index(ol.step)
                elif self.__ol_heuristic == OpenLinkHeuristic.LIFO:
                    first = plan.open_links.index(ol)
                elif self.__ol_heuristic == OpenLinkHeuristic.LOCAL or self.__ol_heuristic == OpenLinkHeuristic.LOCAL_EARLIEST:  # local / local earliest
                    first = - ol.step
                elif self.__ol_heuristic == OpenLinkHeuristic.SORTED or self.__ol_heuristic == OpenLinkHeuristic.SORTED_EARLIEST:  # sorted / sorted earliest
                    first = - self.__hadd(ol, plan)
                elif self.__ol_heuristic == OpenLinkHeuristic.LOCAL_EARLIEST or self.__ol_heuristic == OpenLinkHeuristic.SORTED_EARLIEST: # local earliest / sorted earliest
                    second = seq_plan.index(ol.step)

                max_ol = max(max_ol, first)  # update max open link, int type
                flaws_queue.add((ol, (first, second)))  # update open links
              
            for s in seq_plan:  # a sequential version of the plan.
                try:
                    i = plan.abstract_flaws.index(s)
                    flaws_queue.add((plan.abstract_flaws[i], (max_ol+1, 0)))  # update abstract flaws
                    break
                except ValueError:
                    pass

        return flaws_queue

    # compute heuristic, return a tuple
    def __compute_heuristic(self, 
                            plan: HierarchicalPartialPlan,
                            parent_heuristic: Any) -> Any: 
        
        '''
        h = self.__compute_heuristic(plan, 0)
        parent_heuristic = 0
        '''
        
        if self.__plan_heuristic == PlanHeuristic.DEPTH:  # plan heuristic is depth
            return parent_heuristic - 1


        # paper: We order the nodes in the Open list following hadd:
        hadd = 0
        # 1. we sum the hadd values of the literals in open links, and the hmaxadd of abstract flaw tasks
        for ol in plan.open_links: # (step, preconditions, bool(pos/ neg))
            hadd += self.__hadd(ol, plan)  # add open link's hadd

        htdg_c = 0 # use htdg_c to estimate the cumulative costs of the primitive actions in the plan.
        htdg_m = 0
        htdg_add = 0
        for af in plan.abstract_flaws:  # iterate TDGHeuristic = namedtuple('h_TDG', ['cost', 'modifications', 'hadd_max'])
            htdg = self.__htdg(af.task)
            htdg_c += htdg.cost  # cost
            htdg_m += htdg.modifications  # 0/ 1
            htdg_add += htdg.hadd_max  # hadd max

        h = hadd + htdg_c  # hadd + cost
        effort = len(plan.open_links) + hadd + htdg_m  # open links length + hadd + modifications

        if self.__plan_heuristic == PlanHeuristic.BECHON:
            
            # hadd + cost, open links length + hadd + modifications, - self.__OPEN's length
            return (h, effort, - self.__iterations) 

        if self.__plan_heuristic == PlanHeuristic.HADD_MAX:  # hadd max
            
            # hadd max + hadd, open links length + hadd + modifications
            return (htdg_add + hadd, effort) 

    # paper: Algorithm1: Solve algorithm
    def solve(self,
              output_current_plan: bool = True,
              ) -> HierarchicalPartialPlan:

        # Stats
        revisited = 0
        pruned = 0

        while self.__OPEN:  # while OPEN not empty do

            self.__iterations += 1  # open length
            prune = False

            plan, flaws, h = self.__OPEN.pop(0)  # n <- OPEN.pop()

            LOGGER.info("current plan: %d, %d flaws, h=%s", id(plan), len(flaws), h)
            if output_current_plan is not None:
                plan.write_dot('current-plan.dot')

            if not plan.has_flaws():  # if n.flaws is not None
                LOGGER.info("solution found; search statistics: ")
                LOGGER.info("- iterations: %d", self.__iterations)
                LOGGER.info("- closed: %d", len(self.__CLOSED))
                LOGGER.info("- revisited: %d", revisited)
                LOGGER.info("- pruned: %d", pruned)
                LOGGER.info("- opened: %d", len(self.__OPEN))
                return plan

            LOGGER.info("flaws: AF=%d, OL=%d, Th=%d",
                        len(plan.abstract_flaws),
                        len(plan.open_links),
                        len(plan.threats))

            flaw, rank = flaws.pop(0) # f <- n.flaws.pop() , open links, (first, second)
            LOGGER.info("current flaw: %s, key=%s",
                        flaw, rank)
            
            # get resolvers
            # 1. threat resolvers
            if isinstance(flaw, Threat):
                resolvers = list(plan.threat_resolvers(flaw))
                if not resolvers:
                    prune = True
                    
            # 2. abstract flaw resolvers
            elif isinstance(flaw, AbstractFlaw):
                resolvers = list(plan.abstract_flaw_resolvers(flaw))
                if not resolvers:
                    prune = True

            # 3. open link resolvers
            elif isinstance(flaw, OpenLink):
                resolvers = list(plan.open_link_resolvers(flaw))
                if not resolvers and not plan.has_open_link_task_resolvers(flaw):
                    prune = True

            LOGGER.debug("Resolvers for flaw %s: %d", 
                            flaw, len(resolvers))
                
            if prune:
                pruned += 1
                LOGGER.debug("pruning...")
                continue
            
            # for r in resolvers(f, n.plan) do
            for r in resolvers:
                if r in self.__CLOSED:
                    LOGGER.debug("resolver already closed")
                    revisited += 1
                else:
                    self.__CLOSED.append(r)
                    sorted_flaws = self.__sort_flaws(r)
                    if sorted_flaws is None:
                        LOGGER.debug("no sorted flaws for plan %d: removing", id(r))
                        pruned += 1
                        continue
                    h_r = self.__compute_heuristic(r, h)
                    LOGGER.debug("- new plan %d with %d flaws; h=%s",
                                 id(r), len(sorted_flaws), h_r)
                    self.__OPEN.add((r, sorted_flaws, h_r))  # OPEN <- r

            if flaws:
                self.__OPEN.add((plan, flaws, h))

            LOGGER.info("Open List size: %d", len(self.__OPEN))
            LOGGER.info("Closed List size: %d", len(self.__CLOSED))
