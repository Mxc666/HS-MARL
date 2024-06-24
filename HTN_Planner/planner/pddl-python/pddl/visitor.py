"""PDDL Parser visitor."""

from collections import defaultdict
import itertools

from .parser.PDDLVisitor import PDDLVisitor as AbstractPDDLVisitor

from .domain import Domain, Type, Constant, Variable, Predicate, Action
from .problem import Problem
from .formula import AtomicFormula, NotFormula, AndFormula
from .formula import ForallFormula, WhenEffect
from .belief import UnknownLiteral, OrBelief, OneOfBelief
from .hierarchy import Task, Method, TaskNetwork
from .logger import LOGGER


class PDDLVisitor(AbstractPDDLVisitor):

    """PDDL Visitor implementation."""

    def __init__(self):
        """Construct the Visitor."""
        AbstractPDDLVisitor.__init__(self)
        self.task_index = 0

    def index_task(self):
        """Compute task index if tasks not indexed in input file."""
        i = self.task_index
        self.task_index += 1
        return i

    def visitDomain(self, ctx):
        ops = [self.visit(o) for o in ctx.operators]
        return Domain(ctx.name.text,
                      requirements=(self.visit(ctx.requirements)
                                    if ctx.requirements else frozenset()),
                      types=(self.visit(ctx.types) if ctx.types
                             else frozenset()),
                      constants=(self.visit(ctx.constants)
                                 if ctx.constants else frozenset()),
                      predicates=(self.visit(ctx.predicates)
                                  if ctx.predicates else frozenset()),
                      actions={a.name: a for a in ops
                               if isinstance(a, Action)},
                      tasks={a.name: a for a in ops if isinstance(a, Task)},
                      methods={a.name: a for a in ops
                               if isinstance(a, Method)})

    def visitRequireDef(self, ctx):
        return frozenset(k.text for k in ctx.keys)

    def visitTypesDef(self, ctx):
        return self.visit(ctx.types)

    def visitTypedList(self, ctx):
        typed_list = []
        if ctx.supertype:
            typed_list = [Type(t.text, ctx.supertype.text) for t in ctx.types]
        else:
            typed_list = [Type(t.text) for t in ctx.types]
        if ctx.typedList():
            typed_list += self.visit(ctx.typedList())
        return typed_list

    def visitTypedObjList(self, ctx):
        typed_list = []
        if ctx.objtype:
            typed_list = [Constant(t.text, ctx.objtype.text)
                          for t in ctx.names]
        else:
            typed_list = [Constant(t.text) for t in ctx.names]
        if ctx.typedObjList():
            typed_list += self.visit(ctx.typedObjList())
        return typed_list

    def visitTypedVarList(self, ctx):
        typed_list = []
        if ctx.vartype:
            typed_list = [Variable(t.text, ctx.vartype.text)
                          for t in ctx.names]
        else:
            typed_list = [Variable(t.text) for t in ctx.names]
        if ctx.typedVarList():
            typed_list += self.visit(ctx.typedVarList())
        return typed_list

    def visitConstantsDef(self, ctx):
        return self.visit(ctx.typedObjList())

    def visitPredicatesDef(self, ctx):
        return [self.visit(p) for p in ctx.predicateDef()]

    def visitPredicateDef(self, ctx):
        return Predicate(self.visit(ctx.predicate),
                         self.visit(ctx.typedVarList()))

    def visitNameDef(self, ctx) -> str:
        if ctx.NAME():
            if ctx.name.text is None:
                LOGGER.error("None name in %s", ctx)
            return ctx.name.text
        if ctx.EQUALS():
            return '='
        return ''

    def visitStructureDef(self, ctx):
        if ctx.actionDef():
            return self.visit(ctx.actionDef())
        if ctx.taskDef():
            return self.visit(ctx.taskDef())
        if ctx.methodDef():
            return self.visit(ctx.methodDef())
        return None

    def visitActionDef(self, ctx):
        parameters = self.visit(ctx.parameters) if ctx.parameters else ()
        preconditions = self.visit(
            ctx.precondition) if ctx.precondition else AndFormula([])
        #sortof = AndFormula([AtomicFormula('__sortof', [p.name, p.type]) for p in parameters])
        return Action(ctx.name.text,
                      parameters=parameters,
                      precondition=preconditions,#AndFormula([preconditions, sortof]),
                      effect=(self.visit(ctx.effect) if ctx.effect else ()),
                      observe=(self.visit(ctx.observe)
                               if ctx.observe else None))

    def visitTaskDef(self, ctx):
        return Task(ctx.name.text,
                    parameters=(self.visit(ctx.parameters)
                                if ctx.parameters else ()))

    def visitMethodDef(self, ctx):
        parameters = self.visit(ctx.parameters) if ctx.parameters else ()
        preconditions = self.visit(
            ctx.precondition) if ctx.precondition else AndFormula([])
        #sortof = AndFormula(
        #    [AtomicFormula('__sortof', [p.name, p.type]) for p in parameters])
        if ctx.tn is None:
            tn = None
            constraints = AndFormula([])
        else:
            tn, constraints = self.visit(ctx.tn)
        return Method(ctx.name.text,
                      self.visit(ctx.task),
                      parameters=parameters,
                      precondition=AndFormula([preconditions, constraints]),#, sortof]),
                      tn=tn)

    def visitTaskNetworkDef(self, ctx):
        subtasks = self.visit(ctx.subtasks)
        ordering = defaultdict(list)
        if ctx.ORDERED():
            subtasks_i, subtasks_j = itertools.tee(subtasks)
            next(subtasks_j, None)
            for s_i, s_j in zip(subtasks_i, subtasks_j):
                ordering[s_i[0]].append(s_j[0])
        elif ctx.ORDERING():
            order = self.visit(ctx.orderingDefs())
            for head, tail in order:
                for task in tail:
                    ordering[head].append(task)
        return TaskNetwork(subtasks, ordering), (self.visit(ctx.constraints) if ctx.constraints else AndFormula([]))

    def visitOrderingDefs(self, ctx):
        return [self.visit(o) for o in ctx.order]

    def visitOrderingDef(self, ctx):
        return (ctx.head.text, [t.text for t in ctx.tail])

    def visitSubtasksDef(self, ctx):
        return [self.visit(s) for s in ctx.tasks]

    def visitSubtaskDef(self, ctx):
        return ((f'task{self.index_task()}'
                 if ctx.taskId is None else ctx.taskId.text),
                self.visit(ctx.atomicFormula()))

    def visitConstraintDefs(self, ctx):
        if ctx.AND():
            return AndFormula([self.visit(constraint)
                               for constraint in ctx.constraintDef()])
        return self.visit(ctx.constraintDef(0))

    def visitConstraintDef(self, ctx):
        if ctx.NOT():
            return NotFormula(self.visit(ctx.constraintDef()))
        if ctx.EQUALS():
            return AtomicFormula('=', [ctx.left.text, ctx.right.text])
        return ()

    def visitGoalDef(self, ctx):
        if ctx.literal():
            return self.visit(ctx.literal())
        if ctx.atomicFormula():
            return self.visit(ctx.atomicFormula())
        if ctx.FORALL():
            return ForallFormula(self.visit(ctx.variables), self.visit(ctx.gd))
        if ctx.AND():
            return AndFormula([self.visit(gd) for gd in ctx.ands])
        return AndFormula([])

    def visitLiteral(self, ctx):
        if ctx.NOT():
            return NotFormula(self.visit(ctx.atomicFormula()))
        return self.visit(ctx.atomicFormula())

    def visitAtomicFormula(self, ctx):
        return AtomicFormula(self.visit(ctx.predicate),
                             [self.visit(t) for t in ctx.arguments])

    def visitTerm(self, ctx):
        if ctx.NAME():
            return ctx.name.text
        return ctx.variable.text

    def visitEffectDef(self, ctx):
        if ctx.AND():
            return AndFormula([self.visit(gd) for gd in ctx.ands])
        if ctx.cEffect():
            return AndFormula([self.visit(ctx.cEffect(0))])
        return AndFormula([])

    def visitCEffect(self, ctx):
        if ctx.FORALL():
            # TODO
            return ()
        if ctx.WHEN():
            return WhenEffect(self.visit(ctx.goalDef()),
                              self.visit(ctx.condEffect()))
        return self.visit(ctx.literal())

    def visitCondEffect(self, ctx):
        if ctx.AND():
            return AndFormula([self.visit(gd) for gd in ctx.ands])
        return AndFormula([self.visit(ctx.literal(0))])

    def visitObserveDef(self, ctx):
        return self.visit(ctx.atomicFormula())

    def visitProblem(self, ctx):
        return Problem(
            ctx.pname.text,
            ctx.dname.text,
            self.visit(ctx.init()),
            goal=(self.visit(ctx.goal()) if ctx.goal() else None),
            htn=(self.visit(ctx.htn) if ctx.htn else None),
            requirements=(self.visit(ctx.requirements)
                          if ctx.requirements else []),
            objects=(self.visit(ctx.objects) if ctx.objects else [])
        )

    def visitObjectDeclaration(self, ctx):
        return self.visit(ctx.typedObjList())

    def visitInit(self, ctx):
        return [self.visit(x) for x in ctx.initEl()]

    def visitInitEl(self, ctx):
        if ctx.UNKNOWN():
            return UnknownLiteral(self.visit(ctx.atomicFormula()))
        if ctx.OR():
            return OrBelief([self.visit(x) for x in ctx.choices])
        if ctx.ONEOF():
            return OneOfBelief([self.visit(x) for x in ctx.xchoices])
        return self.visit(ctx.literal(0))

    def visitGoal(self, ctx):
        return self.visit(ctx.goalDef())

    def visitHtnDef(self, ctx):
        if ctx.tn is None:
            tn = None
            constraints = ()
        else:
            tn, constraints = self.visit(ctx.tn)
        return Method('__top_method', AtomicFormula('__top'),
                      parameters=(self.visit(ctx.parameters)
                                  if ctx.parameters else ()),
                      precondition=constraints,
                      tn=tn)
