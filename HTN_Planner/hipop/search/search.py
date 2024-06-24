from typing import Optional
import logging
import math
from collections import deque
import enum

from ..grounding.problem import Problem
from ..plan.plan import HierarchicalPartialPlan

LOGGER = logging.getLogger(__name__)


class TreeSearchAlgorithm(enum.Enum):
    BFS = "bfs"
    DFS = "dfs"


class TreeSearch:
    """Breadth-First Search.

    procedure BFS(G, root) is
        let Q be a queue
        label root as discovered
        Q.enqueue(root)
        while Q is not empty do
            v := Q.dequeue()
            if v is the goal then
                return v
            for all edges from v to w in G.adjacentEdges(v) do
                if w is not labeled as discovered then
                    label w as discovered
                    w.parent := v
                    Q.enqueue(w)
    """
    def __init__(self, problem: Problem):
        self.__problem = problem
        # queue structures
        self.__Q = deque()
        self.__discovered = []
        # initial plan
        plan = HierarchicalPartialPlan(problem, init=True)
        if self.__problem.has_root_task():
            root = self.__problem.root_task()
            plan.add_task(root)
        self.__Q.append(plan)
        self.__discovered.append(plan)

    def solve(self,
              algorithm: TreeSearchAlgorithm = TreeSearchAlgorithm.BFS,
              output_current_plan: bool = True, 
              output_new_plans: bool = True) -> Optional[HierarchicalPartialPlan]:

        # Stats
        revisited = 0
        pruned = 0
        iterations = 0

        while self.__Q:
            iterations += 1

            if algorithm == TreeSearchAlgorithm.BFS:
                v = self.__Q.popleft()
            elif algorithm == TreeSearchAlgorithm.DFS:
                v = self.__Q.pop()

            LOGGER.info("current plan: %d", id(v))
            if output_current_plan:
                v.write_dot('current-plan.dot')

            if not v.has_flaws():
                LOGGER.info("solution found; search statistics: ")
                LOGGER.info("- iterations: %d", iterations)
                LOGGER.info("- discovered: %d", len(self.__discovered))
                LOGGER.info("- revisited: %d", revisited)
                LOGGER.info("- pruned: %d", pruned)
                LOGGER.info("- Q rest: %d", len(self.__Q))
                return v

            LOGGER.info("flaws: AF=%d, OL=%d, Th=%d", 
                        len(v.abstract_flaws),
                        len(v.open_links),
                        len(v.threats))

            children = []
            prune = False

            # loop over threats
            for flaw in v.threats:
                resolvers = list(v.threat_resolvers(flaw))
                LOGGER.debug("Resolvers for flaw %s: %d",
                             flaw, len(resolvers))
                if not resolvers:
                    prune = True
                    break
                for w in resolvers:
                    if w not in self.__discovered:
                        LOGGER.debug("- new plan %d", id(w))
                        if output_new_plans:
                            w.write_dot(f'plan-{id(v)}.dot')
                        children.append(w)
                    else:
                        revisited += 1

            # loop over abstract flaws
            for flaw in v.abstract_flaws:
                # resolve threats first:
                if children: break

                resolvers = list(v.abstract_flaw_resolvers(flaw))
                LOGGER.debug("Resolvers for flaw %s: %d", 
                            flaw, len(resolvers))
                if not resolvers:
                    prune = True
                    break
                for w in resolvers:
                    if w not in self.__discovered:
                        LOGGER.debug("- new plan %d", id(w))
                        if output_new_plans:
                            w.write_dot(f'plan-{id(v)}.dot')
                        children.append(w)
                    else:
                        revisited += 1

            # loop over open links
            for flaw in v.open_links:
                # resolve threats first:
                if children:
                    break
                # if no abstract resolver, stop
                if prune:
                    break

                resolvers = list(v.open_link_resolvers(flaw))
                LOGGER.debug("Resolvers for flaw %s: %d",
                             flaw, len(resolvers))
                if not resolvers and not v.has_open_link_task_resolvers(flaw):
                    prune = True
                    break
                for w in resolvers:
                    if w not in self.__discovered:
                        LOGGER.debug("- new plan %d", id(w))
                        if output_new_plans:
                            w.write_dot(f'plan-{id(v)}.dot')
                        children.append(w)
                    else:
                        revisited += 1

            if prune:
                LOGGER.debug("deadend: pruning")
                pruned += len(children)
                continue

            # successors
            for w in children:
                self.__Q.append(w)
                self.__discovered.append(w)

            LOGGER.info("Q size: %d", len(self.__Q))
            LOGGER.info("Discovered size: %d", len(self.__discovered))
