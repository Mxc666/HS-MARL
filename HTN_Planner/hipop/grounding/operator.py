from typing import Union, Set, Tuple, Dict, Iterator, Iterable, Optional
from abc import ABC
import logging
from collections import defaultdict

import pddl

from ..plan.poset import Poset

from .logic import GOAL, TrueExpr, Expression, FalseExpr
from .objects import Objects
from .literals import Literals
from .errors import TypingAssignmentInconsistent, PreconditionUnsatisfiable, ContradictoryEffects

LOGGER = logging.getLogger(__name__)


def ground_term(fun: str, 
                args: Union[Iterable[pddl.Variable], Iterable[str]],
                assignment: Dict[str, str],
                objects: Optional[Objects]):
        
        params = []
        for a in args:
            if type(a) == str:
                name = a
                atype = 'object'
            else:
                name = a.name
                atype = a.type
            if name in assignment:
                name = assignment[name]
                if name not in objects.per_type(atype):
                    raise TypingAssignmentInconsistent(fun, name)
            params.append(name)
        return f"({fun} {' '.join(params)})"


class WithPrecondition(ABC):

    """An operator with preconditions.

    :param precondition: operator precondition formula
    :param assignment: operator arguments as a dict of variable -> object
    """

    def __init__(self,
                 precondition: Optional[GOAL],
                 assignment: Dict[str, str],
                 objects: Objects,
                 literals: Literals,
                 **kwargs):

        if not precondition:
            self._pre = TrueExpr()
        else:
            self._pre = literals.build(precondition, assignment, objects)
            trues, falses = literals.rigid_literals
            pre = self._pre.simplify(trues, falses)
            if isinstance(pre, FalseExpr):
                raise PreconditionUnsatisfiable(repr(self), self._pre)
            self._pre = pre

    @property
    def precondition(self) -> Expression:
        """Get precondition expression."""
        return self._pre

    @property
    def is_tautology(self) -> bool:
        return isinstance(self._pre, TrueExpr)

    @property
    def is_contradiction(self) -> bool:
        return isinstance(self._pre, FalseExpr)

    @property
    def support(self) -> Tuple[Set[int], Set[int]]:
        """Get precondition expression."""
        return self._pre.support

    def is_applicable(self, state: Set[int]) -> bool:
        """Test if operator is applicable in state."""
        #LOGGER.debug("is applicable %s in %s and not %s", state, self.__pos, self.__neg)
        if self.is_tautology:
            return True
        if self.is_contradiction:
            return False
        pos, neg = self._pre.support
        return (pos <= state) and not (neg & state)


class WithEffect(ABC):

    """An operator with one effect.

    :param effect: operator effect formula
    :param assignment: operator arguments as a dict of variable -> object
    """

    def __init__(self,
                 effect: pddl.AndFormula,
                 assignment: Dict[str, str],
                 literals: Literals,
                 objects: Objects,
                 **kwargs):

        self.__effect = literals.build(effect, assignment, objects)
        self.__adds, self.__dels = self.__effect.support
        inconsistent = self.__adds & self.__dels
        if inconsistent:
            LOGGER.debug("operator %s has inconistent effects %s; removing from dels", repr(self), inconsistent)
            self.__dels -= inconsistent

    @property
    def effect(self) -> Tuple[Set[str], Set[str]]:
        """Get effect expression."""
        return self.__adds, self.__dels

    def apply(self, state: Set[int]) -> Set[int]:
        """Apply operator to state and return a new state."""
        new_state = (state - self.__dels) | self.__adds
        return new_state


class GroundedOperator(ABC):

    """A Grounded Operator.

    :param operator: input PDDL operator
    :param assignment: operator arguments as a dict of variable -> object
    """

    def __init__(self,
                 operator: Union[pddl.Action, pddl.Task, pddl.Method],
                 assignment: Dict[str, str],
                 objects: Objects,
                 **kwargs):

        self.__name = operator.name
        self._assignment = assignment
        self.__pddl = operator
        self.__is_method = False
        # Grounded name
        self.__repr = ground_term(self.name,
                                  operator.parameters,
                                  assignment,
                                  objects)

    def __str__(self):
        return self.__repr

    def __repr__(self):
        return self.__repr

    @property
    def pddl(self):
        return self.__pddl

    @property
    def name(self) -> str:
        """Get operator name."""
        return self.__name

    @property
    def assignment(self):
        return self._assignment

class GroundedAction(WithPrecondition, WithEffect, GroundedOperator):

    """Planning Action.

    :param action: input PDDL action
    :param assignment: action arguments as a dict of variable -> object
    """

    def __init__(self,
                 action: pddl.Action,
                 assignment: Dict[str, str],
                 literals: Literals,
                 objects: Objects,
                 **kwargs):
        GroundedOperator.__init__(self, action, assignment, objects, **kwargs)
        WithPrecondition.__init__(self, action.precondition, assignment,
                                  literals=literals, objects=objects,
                                  **kwargs)
        WithEffect.__init__(self, action.effect, assignment, 
                            objects=objects, literals=literals,
                            **kwargs)
        self.__cost = 1
        LOGGER.debug("action %s pre %s eff %s", str(self), self.precondition, self.effect)

    @property
    def cost(self) -> int:
        """Get action name."""
        return self.__cost


class GroundedMethod(WithPrecondition, GroundedOperator):

    """Planning Hierarchical Method.

    :param method: input PDDL method
    :param assignment: method arguments as a dict of variable -> object
    """

    def __init__(self,
                 method: pddl.Method,
                 assignment: Optional[Dict[str, str]],
                 literals: Literals,
                 objects: Objects,
                 **kwargs):
        GroundedOperator.__init__(self, method, assignment, objects, **kwargs)
        WithPrecondition.__init__(self, method.precondition, assignment,
                                  literals=literals,
                                  objects=objects)
        self.__subtasks = dict()
        self.__network = Poset()

        self.__task = ground_term(method.task.name,
                                  method.task.arguments,
                                  assignment,
                                  objects)

        for taskid, task in method.network.subtasks:
            self.__subtasks[taskid] = ground_term(task.name,
                                                  task.arguments,
                                                  assignment,
                                                  objects)
            self.__network.add(taskid, self.__subtasks[taskid])

        for task, relation in method.network.ordering.items():
            self.__network.add_relation(task, relation, check_poset=False)

        mins = self.__network.minimal_elements()
        maxs = self.__network.maximal_elements()
        self.__network.add('__init', method.name)
        self.__network.add('__goal', method.name)
        for m in mins:
            self.__network.add_relation('__init', m, check_poset=False)
        for m in maxs:
            self.__network.add_relation(m, '__goal', check_poset=False)
        #self.__network.write_dot(f"{self}-tn.dot")
        LOGGER.debug("method %s pre %s", str(self), self.precondition)

    @property
    def task(self) -> str:
        return self.__task

    @property
    def task_network(self) -> Poset:
        return self.__network

    @property
    def subtasks(self) -> Iterator[str]:
        return self.__subtasks.values()

    def subtask(self, taskid: str) -> str:
        return self.__subtasks[taskid]

    @property
    def sorted_tasks(self) -> Iterator[str]:
        return (self.subtask(t) for t in self.task_network.topological_sort()
                if t not in ['__init', '__goal'])


class GroundedTask(GroundedOperator):
    """Planning Hierarchical Task."""
    pass
