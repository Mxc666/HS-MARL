from typing import Union, Set, Iterator
import math
import logging
import networkx
import networkx.drawing.nx_pydot as pydot
import numpy as np
from collections import defaultdict

from .atoms import Atoms
from .operator import GroundedAction

LOGGER = logging.getLogger(__name__)

class HAdd:

    def __init__(self, actions_reward, actions: Iterator[GroundedAction], init: Set[int], fluents: Set[int]):
        self.__actions_reward = actions_reward
        self.__hadd = dict()
        self.__parents = dict()
        self.__compute(actions, init, fluents)
        LOGGER.info("h_add computed for %d elements", len(self.__hadd))

    def write_dot(self, filename: str = "hadd-graph.dot"):
        graph = networkx.DiGraph()
        lit_to_pred = Atoms.atom_to_predicate
        self.__hadd['__init'] = 0
        for child, parent in self.__parents.items():
            if child == parent:
                graph.add_edge(parent, child, label=self.__hadd[child])
            elif type(parent) == list:
                for p in parent:
                    graph.add_edge(f"{p} {lit_to_pred(p)}", child, label=self.__hadd[p])
            else:
                graph.add_edge(parent, f"{child} {lit_to_pred(child)}", label=self.__hadd[child])
        pydot.write_dot(graph, filename)

    def __compute(self, actions: Iterator[GroundedAction], init: Set[int], fluents: Set[int]):
        """H_add computation from V. Vidal, 'YAHSP2: Keep It Simple, Stupid', IPC2011."""
        
        print('improved heuristic')
        literals = list(fluents)
        update = dict()
        lit_in_pre = defaultdict(list)
        pres = defaultdict(list)  # preconditions
        adds = defaultdict(list)  # effects
        costs = dict()
        
        new_action_reward = {}
        rank_ = -1
        action_reward = np.load(self.__actions_reward, allow_pickle=True).item()
        print('action_reward', action_reward)
        sorted_action_reward = sorted(action_reward.items(), key=lambda item:item[1], reverse = True)
        print('sorted_action_reward', sorted_action_reward)
        for val_ in sorted_action_reward:
            new_action_reward[val_[0]] = rank_
            rank_ -= 1
        

        # initiate actions's hadd
        for action in actions:
            aname = str(action)  # action name
            self.__hadd[aname] = math.inf
            pos, _ = action.support
            for lit in pos:
                lit_in_pre[lit].append(aname)
            adds[aname] = list(action.effect[0])  # effects
            pres[aname] = list(pos)  # preconditions  
            costs[aname] = action.cost
            update[aname] = (len(pres[aname]) == 0)
            if update[aname]:
                self.__parents[aname] = aname

        # initiate literals's hadd
        for atom in literals:
            if atom in init:
                self.__hadd[atom] = 0
                for action in lit_in_pre[atom]:
                    update[action] = True
                self.__parents[atom] = '__init'
            else:
                self.__hadd[atom] = math.inf

        # compute hadd
        loop = True
        while loop:
            loop = False
            for action in actions:
                aname = str(action)
                if update[aname]:
                    update[aname] = False
                    
                    # preconditions
                    c = sum(self.__hadd[p] for p in pres[aname])

                    if int(aname[7]) != int(aname[10]):  # r1 r2
                        c -= new_action_reward[str(aname[4])]

                    if c < self.__hadd[aname]:
                        self.__hadd[aname] = c
                        
                        for p in adds[aname]:
                            g = c + costs[aname]
                            if g < self.__hadd[p]:
                                self.__hadd[p] = g
                                
                                for action in lit_in_pre[p]:
                                    loop = True
                                    update[action] = True
                                self.__parents[p] = aname
                        self.__parents[aname] = pres[aname] if pres[aname] else aname

    def __call__(self, element: Union[int, str]) -> int:
        return self.__hadd[element]
    
