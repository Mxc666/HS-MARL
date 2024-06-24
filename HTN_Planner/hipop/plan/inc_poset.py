from typing import TypeVar, Generic, Iterator, List, Dict, Set, Union, Optional, Tuple
from copy import deepcopy
import logging
import networkx
from networkx.algorithms import isomorphism
import networkx.drawing.nx_pydot as nx_pydot

LOGGER = logging.getLogger(__name__)

from .poset import Poset, T

class IncrementalPoset(Poset):

    def __init__(self, graph: Optional[networkx.DiGraph] = None):
        Poset.__init__(self)
        self.__L = dict()
        self.__reachable = dict()
        self.__treeEdge = dict()

    def copy(self):
        new_poset = IncrementalPoset()
        new_poset._graph = deepcopy(self._graph)
        new_poset.__L = self.__L.copy()
        new_poset.__reachable = deepcopy(self.__reachable)
        new_poset.__treeEdge = deepcopy(self.__treeEdge)
        return new_poset

    def add(self, element: T, operator: str = "", **kwargs) -> bool:
        self.__L[element] = 0
        self.__reachable[element] = set()
        self.__treeEdge[element] = set()
        return Poset.add(self, element, operator, **kwargs)

    def remove(self, element: T):
        # TODO: incremental removing
        raise networkx.NetworkXNotImplemented()

    def add_relation(self, x: T, y: Union[T, List[T]],
                     relation: Optional[str] = '<',
                     **kwargs) -> bool:
        if Poset.add_relation(self, x, y, relation, **kwargs):
            # Update reachability
            r = self.__reachable[x]
            if y not in r:
                r |= self.__reachable[y]
                r.add(y)
                for n in self._graph.nodes:
                    r = self.__reachable[n]
                    if (x in r) and (y not in r):
                        r |= self.__reachable[y]
                        r.add(y)
            return True
        return False

    def __follow(self, u: T, path: List[T]):
        if u in path:
            LOGGER.debug("Cycle detected in poset: %s %s", u, path)
            return False
        for v in self._graph.successors(u):
            if self.__L[u] < self.__L[v]:
                pass
            else:
                self.__L[v] = self.__L[u] + 1
                if not self.__follow(v, path + [u]):
                    return False
        return True

    def _add_edge(self, x: T, y: T, relation: str) -> bool:
        if self.__L[x] < self.__L[y]:
            Poset._add_edge(self, x, y, relation)
            return True
        else:
            self.__L[y] = self.__L[x] + 1
            if self.__follow(y, [x]):
                Poset._add_edge(self, x, y, relation)
                return True
        return False

    def is_poset(self):
        return True

    def is_less_than(self, x: T, y: T) -> bool:
        """Return True if x is strictly less than y in the poset."""
        return y in self.__reachable[x]

    def has_bottom(self) -> bool:
        """Return True if the poset has a unique minimal element."""
        mins = self.minimal_elements()
        return len(mins) == 1

    def minimal_elements(self) -> Iterator[T]:
        """Return the list of the minimal elements of the poset."""
        m = min(self.__L.values())
        return set(k for k, v in self.__L.items() if v == m)

    def topological_sort(self) -> Iterator[T]:
        return sorted(self.__L, key=self.__L.get)
