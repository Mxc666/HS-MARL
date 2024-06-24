"""Classes related to initial belief model."""

from typing import Union, List
from .formula import AtomicFormula, NotFormula
LITERAL = Union[AtomicFormula, NotFormula]


class UnknownLiteral:

    """Unknown literal.

    :param formula: the unknown literal
    """

    def __init__(self, formula: AtomicFormula):
        self.__formula = formula

    @property
    def formula(self) -> AtomicFormula:
        """Get formula."""
        return self.__formula

    def __str__(self):
        return '(unknown ' + str(self.formula) + ')'


class OrBelief:

    """Choice belief.

    :param literals: possible initial believes
    """

    def __init__(self, literals: List[LITERAL]):
        self.__literals = literals

    @property
    def literals(self) -> List[LITERAL]:
        """Get choice literals."""
        return self.__literals

    def __str__(self):
        pddl = '(or'
        for literal in self.literals:
            pddl += ' ' + str(literal)
        pddl += ')'
        return pddl


class OneOfBelief:

    """Exclusive choice belief.

    :param literals: possible exclusive initial believes
    """

    def __init__(self, literals: List[LITERAL]):
        self.__literals = literals

    @property
    def literals(self) -> List[LITERAL]:
        """Get choice literals."""
        return self.__literals

    def __str__(self):
        pddl = '(oneof'
        for literal in self.literals:
            pddl += ' ' + str(literal)
        pddl += ')'
        return pddl
