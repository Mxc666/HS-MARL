from typing import TypeVar, Generic, Iterator, List, Dict, Set, Union, Optional, Tuple
from copy import deepcopy
import logging
import networkx
from networkx.algorithms import isomorphism
import networkx.drawing.nx_pydot as nx_pydot

T = TypeVar('T')
LOGGER = logging.getLogger(__name__)

class Poset(Generic[T]):

    def __init__(self):
        self._graph = networkx.DiGraph()

    def copy(self) -> 'Poset':
        new_poset = Poset()
        new_poset._graph = deepcopy(self._graph)
        return new_poset

    def __eq__(self, poset):
        if (len(self._graph.edges) != len(poset._graph.edges)):
            return False
        if (len(self._graph.nodes) != len(poset._graph.nodes)):
            return False
        if not isomorphism.faster_could_be_isomorphic(self._graph, poset._graph):
            return False
        DiGM = isomorphism.DiGraphMatcher(self._graph, poset._graph,
                                          node_match=isomorphism.categorical_node_match(
                                              'operator', ""),
                                          edge_match=isomorphism.categorical_edge_match('relation', frozenset()))
        isomorph = DiGM.is_isomorphic()
        #LOGGER.debug("isomorph: %s, mapping :%s", isomorph, DiGM.mapping)
        #self.write_dot("self-poset.dot")
        #poset.write_dot("other-poset.dot")
        return isomorph

    def __len__(self):
        return self._graph.number_of_nodes()

    def subposet(self, nodes) -> 'Poset':
        new_poset = Poset()
        new_poset._graph = self._graph.subgraph(nodes)
        return new_poset

    @property
    def nodes(self) -> T:
        return self._graph.nodes

    @property
    def edges(self) -> Tuple[T, T]:
        return self._graph.edges

    def add(self, element: T, operator: str = "", **kwargs) -> bool:
        self._graph.add_node(element, operator=operator, label=f"[{element}] {operator}", **kwargs)
        return True

    def remove(self, element: T):
        self._graph.remove_node(element)

    def _add_edge(self, x: T, y: T, relation: str) -> bool:
        if self._graph.has_edge(x, y):
            rel = self._graph[x][y]['label']
            rel.add(relation)
        else:
            if isinstance(relation, set):
                rel = relation
            else:
                rel = set()
                rel.add(relation)
            self._graph.add_edge(x, y, label=rel)
        attrs = self._graph[x][y]
        attrs['relation'] = frozenset(attrs['label'])
        return True

    def add_relation(self, x: T, y: Union[T, List[T]],
                     relation: Optional[str] = '<',
                     check_poset: bool = False) -> bool:
        if type(y) is list:
            for el in y:
                if not self.add_relation(x, el, relation, check_poset):
                    return False
        else:
            if not self._add_edge(x, y, relation):
                return False
            if check_poset:
                return self.is_poset()
            return True

    def is_poset(self) -> bool:
        return (networkx.is_directed_acyclic_graph(self._graph)
                and
                networkx.number_of_selfloops(self._graph) == 0)

    def cardinality(self) -> int:
        return self._graph.number_of_nodes()

    def is_less_than(self, x: T, y: T) -> bool:
        """Return True if x is strictly less than y in the poset."""
        return networkx.has_path(self._graph, x, y)

    def is_greater_than(self, x: T, y: T) -> bool:
        """Return True if x is strictly greater than y in the poset."""
        return self.is_less_than(y, x)

    def has_bottom(self) -> bool:
        """Return True if the poset has a unique minimal element."""
        ins = self._graph.in_degree(self._graph.nodes)
        return len(list(filter(lambda x: x[1] == 0, ins))) == 1

    def has_top(self) -> bool:
        """Return True if the poset has a unique maximal element."""
        outs = self._graph.out_degree(self._graph.nodes)
        return len(list(filter(lambda x: x[1] == 0, outs))) == 1

    def is_bounded(self) -> bool:
        """Return True if the poset is bounded, and False otherwise."""
        return self.has_bottom() and self.has_top()

    def maximal_elements(self) -> Iterator[T]:
        """Return the list of the maximal elements of the poset."""
        outs = self._graph.out_degree(self._graph.nodes)
        return map(lambda x: x[0], filter(lambda x: x[1] == 0, outs))

    def minimal_elements(self) -> Iterator[T]:
        """Return the list of the minimal elements of the poset."""
        ins = self._graph.in_degree(self._graph.nodes)
        return map(lambda x: x[0], filter(lambda x: x[1] == 0, ins))

    def top(self) -> T:
        """Return the top element of the poset, if it exists."""
        maxs = list(self.maximal_elements())
        if len(maxs) == 1:
            return maxs[0]
        else:
            return None

    def bottom(self) -> T:
        """Return the bottom element of the poset, if it exists."""
        mins = list(self.minimal_elements())
        if len(mins) == 1:
            return mins[0]
        else:
            return None

    def topological_sort(self) -> Iterator[T]:
        return networkx.topological_sort(self._graph)

    def write_dot(self, filename: str):
        nx_pydot.write_dot(self._graph, filename)
