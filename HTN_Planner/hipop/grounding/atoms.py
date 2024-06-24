from typing import Tuple, Iterator, List, Dict
from collections import defaultdict
import logging

LOGGER = logging.getLogger(__name__)


class Atoms:
    __atoms = defaultdict(dict)
    __predicates = defaultdict(dict)
    __counter = 0

    @classmethod
    def atoms(cls):
        return cls.__predicates.keys()

    @classmethod
    def atom(cls, predicate: str, *arguments: str) -> Tuple[int, str]:
        args = tuple(arguments)
        if args not in cls.__atoms[predicate]:
            cls.__atoms[predicate][args] = (
                cls.__counter, predicate)
            cls.__predicates[cls.__counter] = (predicate, args)
            LOGGER.debug("atom %s: %s %s", 
                         cls.__counter,
                         predicate, args)
            cls.__counter += 1
        return cls.__atoms[predicate][args]

    @classmethod
    def atoms_of(cls, predicate: str) -> Iterator[Tuple[int, str]]:
        return cls.__atoms[predicate].values()

    @classmethod
    def atom_to_predicate(cls, atom: int) -> Tuple[str, List[str]]:
        return cls.__predicates[atom]
