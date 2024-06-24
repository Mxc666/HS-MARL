from abc import ABC
from typing import Union, Dict, Iterable, Tuple, List
from collections import defaultdict
import pddl
import logging

from .objects import iter_objects

LOGGER = logging.getLogger(__name__)
GOAL = Union[pddl.AndFormula, pddl.AtomicFormula,
             pddl.ForallFormula, pddl.NotFormula,
             pddl.WhenEffect]


class Expression(ABC):
    def evaluate(self, trues):
        LOGGER.error("not implemented")
    def simplify(self, trues, falses):
        LOGGER.error("not implemented")
    @property
    def support(self):
        LOGGER.error("not implemented")
    def __repr__(self):
        return str(self)

class TrueExpr(Expression):
    def evaluate(self, trues):
        return True
    def simplify(self, trues, falses):
        return TrueExpr()
    @property
    def support(self):
        return set(), set()
    def __str__(self):
        return 'T'

class FalseExpr(Expression):
    def evaluate(self, trues):
        return False
    def simplify(self, trues, falses):
        return FalseExpr()
    @property
    def support(self):
        return set(), set()
    def __str__(self):
        return 'F'

class Atom(Expression):
    def __init__(self, atom):
        self.__atom = atom
    def evaluate(self, trues):
        return self.__atom in trues
    def simplify(self, trues, falses):
        if self.__atom in trues:
            return TrueExpr()
        if self.__atom in falses:
            return FalseExpr()
        return self
    @property
    def support(self):
        return set({self.__atom}), set()
    def __str__(self):
        return f"[{self.__atom}]"

class And(Expression):
    def __init__(self, *expressions):
        self.__expressions = expressions
    def evaluate(self, trues):
        return all((e.evaluate(trues) for e in self.__expressions))
    def simplify(self, trues, falses):
        exprs = list(e.simplify(trues, falses) for e in self.__expressions)
        if any((isinstance(e, FalseExpr) for e in exprs)):
            return FalseExpr()
        if all((isinstance(e, TrueExpr) for e in exprs)):
            return TrueExpr()
        return And(*exprs)
    @property
    def support(self):
        pos = set()
        neg = set()
        for e in self.__expressions:
            p, n = e.support
            pos |= p
            neg |= n
        return pos, neg
    def __str__(self):
        return f"({'&'.join(map(str, self.__expressions))})"


class Not(Expression):
    def __init__(self, expression):
        self.__expression = expression
    def evaluate(self, trues):
        return not self.__expression.evaluate(trues)
    def simplify(self, trues, falses):
        expr = self.__expression.simplify(falses, trues)
        if isinstance(expr, TrueExpr):
            return TrueExpr()
        if isinstance(expr, FalseExpr):
            return FalseExpr()
        return self
    @property
    def support(self):
        pos, neg = self.__expression.support
        return neg, pos
    def __str__(self):
        return f"(~{self.__expression})"
