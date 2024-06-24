from typing import Tuple, Iterator, List, Dict, Any, Callable, Set
from collections import defaultdict
import logging

import pddl

from .logic import GOAL, Atom, Not, And, TrueExpr, FalseExpr, Expression
from .atoms import Atoms
from .objects import Objects, iter_objects

LOGGER = logging.getLogger(__name__)


class Literals:
    def __init__(self, domain: pddl.Domain, problem: pddl.Problem, 
                 objects: Objects, filter_rigid: bool = True,
                 equality: bool = False):
        # Build all Atoms
        atoms_per_predicate = defaultdict(set)
        for predicate in sorted(domain.predicates):
            for args in iter_objects(predicate.variables, objects.per_type, {}):
                atom, _ = Atoms.atom(predicate.name, *[a[1] for a in args])
                atoms_per_predicate[predicate.name].add(atom)
            LOGGER.debug("predicate %s: %s", predicate.name, atoms_per_predicate[predicate.name])
        LOGGER.info("Predicates: %d", len(atoms_per_predicate))
        LOGGER.info("Atoms: %d", len(Atoms.atoms()))
        # Fluents
        if filter_rigid:
            self.__fluents = set()
            for action in domain.actions:
                expr = self.__build_expression(action.effect, {}, objects,
                                           lambda x, *args: x)
                pos, neg = expr.support
                self.__fluents |= pos
                self.__fluents |= neg
        if not filter_rigid:
            self.__fluents = set(pred.name for pred in domain.predicates)
        LOGGER.info("Fluents: %d", len(self.__fluents))
        LOGGER.debug("Fluents: %s", self.__fluents)
        self.__rigid = set(
            pred.name for pred in domain.predicates) - self.__fluents
        if equality:
            self.__rigid.add('=')
        LOGGER.info("Rigid relations: %d", len(self.__rigid))
        LOGGER.debug("Rigid relations: %s", self.__rigid)
        # Rigid Literals
        rigid_atoms = set(a for a in Atoms.atoms()
                          if Atoms.atom_to_predicate(a)[0] in self.__rigid)
        LOGGER.info("Rigid atoms: %d", len(rigid_atoms))
        LOGGER.debug("Rigid atoms: %s", rigid_atoms)
        pb_init = set(Atoms.atom(lit.name, *lit.arguments)[0] for lit in problem.init)
        LOGGER.debug("Problem init state: %s", pb_init)
        if equality:
            equals = set(Atoms.atom('=', o, o)[0] for o in objects)
            diffs = set(Atoms.atom('=', o, u)[0]
                        for o in objects for u in objects if u != o)
        else:
            equals = set()
            diffs = set()
        rigid_atoms |= equals | diffs
        self.__rigid_literals = (((pb_init | equals) & rigid_atoms),
                                 (rigid_atoms - pb_init) - equals)
        LOGGER.info("Rigid literals: %d", sum(map(len, self.__rigid_literals)))
        LOGGER.debug("Rigid literals: %s", self.__rigid_literals)
        # Init State
        self.__init_literals = (
            pb_init - self.__rigid_literals[0]), (Atoms.atoms() - rigid_atoms - pb_init)
        LOGGER.info("Init state literals: %d", sum(
            map(len, self.__init_literals)))
        LOGGER.debug("Init state literals: %s", self.__init_literals)

    @property
    def rigid_relations(self) -> Set[str]:
        return self.__rigid

    @property
    def rigid_literals(self) -> Tuple[Set[int], Set[int]]:
        return self.__rigid_literals

    @property
    def varying_relations(self) -> Set[str]:
        return self.__fluents

    @property
    def varying_literals(self) -> Set[int]:
        a, b = self.__init_literals
        return a | b

    @property
    def init(self) -> Tuple[Set[int], Set[int]]:
        return self.__init_literals

    def __assign(self, args: List[str], assignment: Dict[str, str], 
                 complete: bool = True) -> List[str]:
        result = []
        for a in args:
            if a in assignment:
                result.append(assignment[a])
            elif complete and a[0] == '?':
                # a is a variable
                raise KeyError()
            else:
                result.append(a)
        return result

    def __build_expression(self, formula: GOAL,
                         assignment: Dict[str, str],
                         objects: Objects,
                         atom_factory: Callable[[List[str]], Any]) -> Expression:
        if isinstance(formula, pddl.AtomicFormula):
            atom = atom_factory(formula.name, 
                                *self.__assign(formula.arguments,
                                             assignment, False))
            return Atom(atom)
        if isinstance(formula, pddl.NotFormula):
            return Not(self.__build_expression(formula.formula, assignment, objects, atom_factory))
        if isinstance(formula, pddl.AndFormula):
            return And(*[self.__build_expression(f, assignment, objects, atom_factory)
                        for f in formula.formulas])
        if isinstance(formula, pddl.WhenEffect):
            LOGGER.error("conditional effects not supported!")
            return FalseExpr()
        if isinstance(formula, pddl.ForallFormula):
            return And(*[self.__build_expression(formula.goal,
                                                 dict(assign, **assignment),
                                                 objects, atom_factory)
                         for assign in iter_objects(formula.variables, objects.per_type, dict())])
        return TrueExpr()

    def build(self, formula: GOAL,
              assignment: Dict[str, str],
              objects: Objects) -> Expression:
        def atom_factory(x, *args):
            a, _ = Atoms.atom(x, *args)
            return a
        return self.__build_expression(formula, assignment, objects, atom_factory)

    def build_partial(self, formula: GOAL,
                      assignment: Dict[str, str],
                      objects: Objects,
                      atom_factory: Callable[[List[str]], Any]) -> Expression:
        return self.__build_expression(formula, assignment, objects, atom_factory)

    def extract(self, fun: Callable[[Any, GOAL], Any], formula: GOAL) -> Any:
        def list_extract(fun, formula, result):
            if isinstance(formula, pddl.AtomicFormula):
                result = fun(result, formula)
            if isinstance(formula, pddl.NotFormula):
                result = list_extract(fun, formula.formula, result)
            if isinstance(formula, pddl.AndFormula):
                for f in formula.formulas:
                    result = list_extract(fun, f, result)
            return result
        return list_extract(fun, formula, [])
