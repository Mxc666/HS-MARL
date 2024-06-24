import logging
from typing import Optional, Dict, Iterator, Tuple, Set, List, Callable
from collections import defaultdict, namedtuple, deque
import networkx
import math
import numpy as np

from .operator import GroundedOperator, GroundedAction, GroundedTask, GroundedMethod
from .hadd import HAdd

LOGGER = logging.getLogger(__name__)

TDGHeuristic = namedtuple('h_TDG', ['cost', 'modifications', 'hadd_max'])

class TaskDecompositionGraph:

    def __init__(self, methods_reward, actions: Dict[str, GroundedAction],
                 methods: Dict[str, GroundedMethod],
                 tasks: Dict[str, GroundedTask],
                 hadd: HAdd):

        self.__methods_reward = methods_reward
        self.__graph = networkx.DiGraph()
        self.__useless = set()

        self.__graph.add_nodes_from(tasks, type='task')
        self.__graph.add_nodes_from(methods, shape='rectangle', type='method')
        self.__graph.add_nodes_from(actions, type='action')
        for name, method in methods.items():
            if method.task in tasks:
                self.__graph.add_edge(method.task, name)
            else:
                LOGGER.debug("USELESS: method %s has no task %s", name, method.task)
                self.__useless.add(name)
            for subtask in method.subtasks:
                if subtask in tasks or subtask in actions:
                    self.__graph.add_edge(name, subtask)
                else:
                    LOGGER.debug("USELESS: method %s has no subtask %s",
                                name, subtask)
                    self.__useless.add(name)
        
        # TODO: prune cycles (see Behnke et al., 2020)

        # Optimistic task effects (see Angelic Planning) and Heuristics
        self.__task_effects = defaultdict(lambda: (set(), set()))
        self.__hadd = hadd
        self.__heuristics = defaultdict(lambda: TDGHeuristic(0, 0, math.inf))
        for name, action in actions.items():
            self.__task_effects[name] = action.effect
            self.__heuristics[name] = TDGHeuristic(cost=action.cost, modifications=1, 
                                                   hadd_max=self.__hadd(name))
            self.__graph.nodes[name]['label'] = f"{name}\n{self.__heuristics[name]}"

    def __len__(self):
        return self.__graph.number_of_nodes()

    def __iter__(self):
        return self.__graph.__iter__()

    def successors(self, node: str) -> Iterator[str]:
        return self.__graph.successors(node)

    def task_effects(self, task: str) -> Tuple[Set[int], Set[int]]:
        return self.__task_effects[task]

    def heuristics(self, node: str) -> TDGHeuristic:
        return self.__heuristics[node]

    @property
    def cycles(self) -> Iterator[List[str]]:
        return networkx.simple_cycles(self.__graph)

    def has_cycles(self) -> bool:
        try:
            cycle = networkx.find_cycle(self.__graph)
            LOGGER.debug("Found cycle %s", cycle)
        except networkx.NetworkXNoCycle:
            return False
        return True

    def __traverse_graph(self, fun: Callable[[str], None]):
        reverse_scc = networkx.condensation(self.__graph).reverse()
        sorted_scc = deque(networkx.topological_sort(reverse_scc))
        while sorted_scc:
            scc = sorted_scc.popleft()
            members = reverse_scc.nodes[scc]['members']
            # iterate until fix point
            update = True
            while update:
                LOGGER.debug("Traversing TDG: updating SCC %s once", scc)
                update = False
                for node in members:
                    updated = fun(node)
                    if updated: update = True

    def remove_useless(self, useless: Iterator[str]):
        LOGGER.debug("Initialy useless: %d", len(self.__useless))
        self.__useless |= set(useless)
        LOGGER.debug("Added useless: %d", len(self.__useless))
        def fun(node: str) -> bool:
            if node in self.__useless: return False
            # Actions
            if self.__graph.nodes[node]['type'] == 'action':
                pass
            # Methods
            elif self.__graph.nodes[node]['type'] == 'method':
                if any(x in self.__useless for x in self.__graph.successors(node)):
                    LOGGER.debug("Pruning %s: some subtask is useless", node)
                    self.__useless.add(node)
                    return True
            # Tasks
            elif self.__graph.nodes[node]['type'] == 'task':
                if all(x in self.__useless for x in self.__graph.successors(node)):
                    LOGGER.debug("Pruning %s: all methods are useless", node)
                    self.__useless.add(node)
                    return True
            # TODO: loop on SCC to remove correctly useless nodes
            return False

        self.__traverse_graph(fun)
        LOGGER.debug("Recursively useless: %d", len(self.__useless))
        self.__remove_nodes(list(self.__useless))

    def __compute_heuristics_node(self, node: str) -> bool:
        # Actions
        if self.__graph.nodes[node]['type'] == 'action':
            return False
        # Methods
        elif self.__graph.nodes[node]['type'] == 'method':
            # Compute task effects and heuristics
            adds, dels = set(), set()
            h_c, h_m, h_add = 0, 0, 0
            for subtask in self.__graph.successors(node):
                a, d = self.__task_effects[subtask]
                adds |= a
                dels |= d
                h_c += self.__heuristics[subtask].cost
                h_m += self.__heuristics[subtask].modifications
                h_add += self.__heuristics[subtask].hadd_max
        # Tasks
        elif self.__graph.nodes[node]['type'] == 'task':
            # Compute task effects and heuristics
            adds, dels = set(), set()
            h_c, h_m, h_add = math.inf, math.inf, 0

            if self.__methods_reward != 'NONE':
                method_reward = np.load(self.__methods_reward, allow_pickle=True).item()
                method_key = list(method_reward.keys())
            for method in self.__graph.successors(node):
                a, d = self.__task_effects[method]
                adds |= a
                dels |= d
                h_c = min(h_c, self.__heuristics[method].cost)
                h_m = min(h_m, self.__heuristics[method].modifications)
                if self.__methods_reward == 'NONE':
                    h_add = max(h_add, self.__heuristics[method].hadd_max)
                else:
                    if method[1]!='_' and str(method[2]) in method_key:
                        h_add = max(h_add, self.__heuristics[method].hadd_max - method_reward[str(method[2])])
                    else:
                        h_add = max(h_add, self.__heuristics[method].hadd_max)
        # Update heuristics
        update = False
        if (node not in self.__task_effects) or ((adds, dels) != self.__task_effects[node]):
            self.__task_effects[node] = (adds, dels)
            update = True
        htdg = TDGHeuristic(
            cost=h_c, modifications=h_m, hadd_max=h_add)
        if (node not in self.__heuristics) or (htdg != self.__heuristics[node]):
            self.__heuristics[node] = htdg
            update = True
        self.__graph.nodes[node]['label'] = f"{node}\n{self.__heuristics[node]}"
        return update

    def compute_heuristics(self):
        self.__traverse_graph(self.__compute_heuristics_node)
        LOGGER.debug("Heuristics computed")
        LOGGER.debug("Root task heuristics: %s", self.__heuristics['(__top )'])
        LOGGER.debug("Task macro effects:")
        for node, effects in self.__task_effects.items():
            if self.__graph.nodes[node]['type'] == 'task':
                LOGGER.debug("- %s: %s", node, effects)

    def htn(self, root_task: str):
        reachables = networkx.single_source_shortest_path_length(self.__graph, root_task)
        unreachables = [n for n in self.__graph.nodes if n not in reachables]
        self.__remove_nodes(unreachables)

    def __remove_nodes(self, nodes: Iterator[str]):
        self.__graph.remove_nodes_from(nodes)
        for n in nodes:
            try:
                del self.__task_effects[n]
                del self.__heuristics[n]
            except KeyError:
                pass
            self.__useless.discard(n)

    def write_dot(self, filename: str):
        import networkx.drawing.nx_pydot as pydot
        for u in self.__useless:
            if u in self.__graph.nodes:
                self.__graph.nodes[u]['color'] = 'red'
                self.__graph.nodes[u]['style'] = 'filled'
        pydot.write_dot(self.__graph, filename)
