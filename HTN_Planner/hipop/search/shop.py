import sys
import logging
from collections import defaultdict

from ..grounding.problem import Problem

LOGGER = logging.getLogger(__name__)

class SHOP():

    def __init__(self, problem: Problem,
                 no_duplicate_search: bool = False):
        self.__problem = problem
        self.__tdg = problem.tdg
        self.__nds = no_duplicate_search
        self.__stop_planning = False
        self.__goal = problem.goal

    def stop(self):
        self.__stop_planning = True

    def solve(self, state, tasks):
        """
         Searches for a plan that accomplishes tasks in state.
         Basically performs a DFS.
        :param state: Initial state of the search
        :return: the plan
        """
        self.__stop_planning = False
        return self.__seek_plan(state, tasks, [], 0,
                                defaultdict(list), defaultdict(list))

    def __seek_plan(self, state, tasks, branch, depth, seen, decomposed):
        if self.__stop_planning: return None

        LOGGER.debug("depth: %d", depth)
        LOGGER.debug("state: %s", state)
        LOGGER.debug("tasks: %s", tasks)
        LOGGER.debug("seen (%d): %s ", len(seen), seen)
        LOGGER.debug("current branch: %s", branch)
        if not tasks:
            # Test if plan reaches goal:
            pos_goal, neg_goal = self.__goal
            if pos_goal <= state and not bool(neg_goal & state):
                LOGGER.debug("returning plan: %s", branch)
                return branch
            else:
                return None

        current_task = tasks[0]
        LOGGER.debug("current task: %s", current_task)

        if self.__problem.has_task(current_task):
            return self.__seek_task(current_task, state, tasks, branch, depth, seen, decomposed)

        if self.__problem.has_action(current_task):
            return self.__seek_action(current_task, state, tasks, branch, depth, seen, decomposed)
    
    def __seek_action(self, current_action, state, tasks, branch, depth, seen, decomposed):
        action = self.__problem.action(current_action)
        LOGGER.debug("depth %d action %s", depth, action)
        if action.is_applicable(state):
            s1 = frozenset(action.apply(state))
            if self.__nds and s1 in seen:
                if action in seen[s1]:
                    LOGGER.debug("couple state-action already visited {}-{}".format(s1, action))
                    return None

            seen[s1].append(action)
            result = self.__seek_plan(s1, tasks[1:],
                                      branch + [action],
                                      depth, seen, decomposed)
            if result is None:
                seen[s1].pop()

            return result

        else:
            LOGGER.debug("action {} is NOT applicable".format(action))
            return None


    def __seek_task(self, current_task, state, tasks, branch, depth, seen, decomposed):
        methods = self.__tdg.successors(current_task)
        for method in methods:
            gmethod = self.__problem.method(method)
            if self.__stop_planning: return None
            LOGGER.debug("depth %d : method %s", depth, method)

            if not gmethod.is_applicable(state):
                LOGGER.debug("method %s not applicable in state %s",
                             method, state)
                continue

            if state in decomposed[method]:
                LOGGER.debug("method %s already decomposed in state %s",
                             method, state)
                continue

            substeps = list(gmethod.sorted_tasks)
            LOGGER.debug("# substeps: %s", substeps)

            decomposed[method].append(state)

            result = self.__seek_plan(state, substeps + tasks[1:],
                                      branch, depth+1, seen, decomposed)

            decomposed[method].pop()

            if result is not None:
                return result

        LOGGER.debug("no method leads to solution")
        return None
