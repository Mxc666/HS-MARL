"""HDDL domain classes."""

from typing import List, Union, Tuple, Dict
from .formula import AtomicFormula, AndFormula, NotFormula
from .variable import Variable


class Task:

    """HDDL task.

    :param name: task name
    :param parameters: task parameters
    """

    def __init__(self,
                 name: str,
                 parameters: List[Variable] = ()):
        self.__name = name
        self.__parameters = parameters
        self.__methods = []

    @property
    def name(self) -> str:
        """Get name."""
        return self.__name

    @property
    def methods(self) -> List['Method']:
        """Get task methods."""
        return self.__methods

    def add_method(self, method: 'Method'):
        """Add a method to the task.

        :param method: a method
        """
        if method.task.name != self.name:
            msg = "Method {} does not refine task {}"
            raise AttributeError(msg.format(method.name, self.name))
        self.__methods.append(method)

    @property
    def parameters(self) -> List[Variable]:
        """Get parameters."""
        return self.__parameters


class Method:

    """HDDL method.

    Also used to represent a problem HTN.

    :param name: method name
    :param task: task implemented by the method
    :param parameters: method parameters
    :param precondition: method precondition
    :param tn: method task network
    """

    def __init__(self, name: str, task: AtomicFormula,
                 parameters: List[Variable] = None,
                 precondition: Union[AtomicFormula,
                                     NotFormula, AndFormula] = None,
                 tn: 'TaskNetwork' = None):
        self.__name = name
        self.__task = task
        self.__parameters = parameters
        self.__precondition = precondition
        self.__tn = tn

    @property
    def name(self) -> str:
        """Get name."""
        return self.__name

    @property
    def task(self) -> AtomicFormula:
        """Get task predicate."""
        return self.__task

    @property
    def parameters(self) -> List[Variable]:
        """Get parameters."""
        return self.__parameters

    @property
    def precondition(self) -> Union[AtomicFormula, NotFormula, AndFormula]:
        """Get precondition."""
        return self.__precondition

    @property
    def network(self) -> 'TaskNetwork':
        """Get task network."""
        return self.__tn


class TaskNetwork:

    """Task network model.

    :param subtasks: subtasks of the method, as a list of (id, formula) pairs
    :param ordering: ordering relation between subtasks, as a dict where keys
        are task ids, and values are the task ids ordered after the key
    """

    def __init__(self,
                 subtasks: List[Tuple[str, AtomicFormula]],
                 ordering: Dict[str, List[str]]):
        self.__subtasks = subtasks
        self.__ordering = ordering

    @property
    def subtasks(self) -> List[Tuple[str, AtomicFormula]]:
        """Get subtasks."""
        return self.__subtasks

    @property
    def ordering(self) -> Dict[str, List[str]]:
        """Get subtasks ordering."""
        return self.__ordering
