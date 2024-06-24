"""Description of a PDDL problem."""

from typing import List, Union

from .formula import AtomicFormula, NotFormula, AndFormula
from .domain import Constant
from .belief import UnknownLiteral, OrBelief, OneOfBelief
from .hierarchy import Method

LITERAL = Union[AtomicFormula, NotFormula]
INITELT = Union[AtomicFormula, NotFormula, UnknownLiteral,
                OrBelief, OneOfBelief]
GOAL = Union[AtomicFormula, NotFormula, AndFormula]


class Problem:

    """PDDL problem.

    :param name: problem name
    :param domain: domain name
    :param init: initial state
    :param goal: goal state
    :param htn: HTN task to decompose
    :param requirements: list of requirements
    :param objects: list of objects of the problem
    """

    def __init__(self,
                 name: str,
                 domain: str,
                 init: List[INITELT],
                 goal: GOAL = None,
                 htn: Method = None,
                 requirements: List[str] = (),
                 objects: List[Constant] = ()):
        self.__name = name
        self.__domain = domain
        self.__init = init
        self.__goal = goal
        self.__htn = htn
        self.__requirements = requirements
        self.__objects = objects

    @property
    def name(self) -> str:
        """Get name."""
        return self.__name

    @property
    def domain(self) -> str:
        """Get domain."""
        return self.__domain

    @property
    def init(self) -> List[INITELT]:
        """Get initial state."""
        return self.__init

    @property
    def goal(self) -> GOAL:
        """Get goal literals."""
        return self.__goal

    @property
    def requirements(self) -> List[str]:
        """Get list of requirements."""
        return self.__requirements

    @property
    def objects(self) -> List[Constant]:
        """Get problem objects."""
        return self.__objects

    @property
    def htn(self) -> Method:
        """Get HTN goal."""
        return self.__htn
