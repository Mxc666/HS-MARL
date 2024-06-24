"""Classes related to the Domain description."""

from typing import List, Optional, Dict, Iterator
from .formula import AtomicFormula, AndFormula, WhenEffect
from .variable import Type, Constant, Variable, Predicate
from .hierarchy import Task, Method


class Action:

    """PDDL action.

    :param name: action name
    :param parameters: action parameters
    :param precondition: action precondition
    :param effect: action state effect
    :param observe: action observation effect
    """

    def __init__(self, name: str,
                 parameters: List[Variable] = (),
                 precondition: AndFormula = None,
                 effect: AndFormula = None,
                 observe: AtomicFormula = None):
        self.__name = name
        self.__parameters = parameters
        self.__precondition = precondition
        self.__effect = effect
        self.__observe = observe

    @property
    def name(self) -> str:
        """Get name."""
        return self.__name

    @property
    def parameters(self) -> List[Variable]:
        """Get parameters."""
        return self.__parameters

    @property
    def precondition(self) -> AndFormula:
        """Get precondition."""
        return self.__precondition

    @property
    def effect(self) -> AndFormula:
        """Get effect."""
        return self.__effect

    @property
    def observe(self) -> Optional[AtomicFormula]:
        """Get observation effect."""
        return self.__observe


class Domain:

    """PDDL domain.

    :param name: domain name
    :param requirements: list of domain requirements
    :param types: domain types
    :param constants: domain constants
    :param predicates: domain predicates
    :param actions: domain actions
    :param tasks: domain tasks
    :param methods: domain methods
    """

    def __init__(self, name: str,
                 requirements: List[str] = (),
                 types: List[Type] = (),
                 constants: List[Constant] = (),
                 predicates: List[Predicate] = (),
                 actions: Dict[str, Action] = dict(),
                 tasks: Dict[str, Task] = dict(),
                 methods: Dict[str, Method] = dict()):
        self.__name = name
        self.__requirements = requirements
        self.__types = types
        self.__constants = constants
        self.__predicates = {p.name: p for p in predicates}
        self.__actions = actions
        self.__tasks = tasks
        self.__methods = methods
        for method in self.__methods.values():
            self.__tasks[method.task.name].add_method(method)

    @property
    def name(self) -> str:
        """Get name."""
        return self.__name

    @property
    def requirements(self) -> List[str]:
        """Get list of requirements."""
        return self.__requirements

    @property
    def types(self) -> List[Type]:
        """Get set of types."""
        return self.__types

    @property
    def constants(self) -> List[Constant]:
        """Get set of constants."""
        return self.__constants

    @property
    def predicates(self) -> List[Predicate]:
        """Get predicates."""
        return self.__predicates.values()

    def get_predicate(self, predicate: str) -> Predicate:
        """Get predicate by name."""
        return self.__predicates[predicate]

    @property
    def actions(self) -> Iterator[Action]:
        """Get actions."""
        return self.__actions.values()

    def get_action(self, action: str) -> Action:
        """Get action by name."""
        return self.__actions[action]

    def has_action(self, action: str) -> bool:
        """Return true if action exists."""
        return action in self.__actions

    @property
    def tasks(self) -> Iterator[Task]:
        """Get tasks."""
        return self.__tasks.values()

    def get_task(self, task: str) -> Action:
        """Get task by name."""
        return self.__tasks[task]

    def has_task(self, task: str) -> bool:
        """Return true if task exists."""
        return task in self.__tasks

    @property
    def methods(self) -> Iterator[Method]:
        """Get methods."""
        return self.__methods.values()

    def get_method(self, method: str) -> Method:
        """Get method by name."""
        return self.__methods[method]

    def has_method(self, method: str) -> bool:
        """Return true if method exists."""
        return method in self.__methods
