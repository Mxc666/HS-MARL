"""PDDL parsing functions."""

import antlr4
from .parser.PDDLLexer import PDDLLexer
from .parser.PDDLParser import PDDLParser
from .visitor import PDDLVisitor
from .domain import Domain
from .problem import Problem
from .logger import LOGGER


def parse_pddl_file(file: str):
    """Parse a PDDL file and returns the parsed tree."""
    input_stream = antlr4.FileStream(file)
    lexer = PDDLLexer(input_stream)
    stream = antlr4.CommonTokenStream(lexer)
    return PDDLParser(stream)


def parse_pddl_str(pddl: str):
    """Parse a PDDL string and returns the parsed tree."""
    input_stream = antlr4.InputStream(pddl)
    lexer = PDDLLexer(input_stream)
    stream = antlr4.CommonTokenStream(lexer)
    return PDDLParser(stream)


def parse_domain(pddl: str,
                 file_stream: bool = False) -> Domain:
    """Parse a PDDL domain.

    :param pddl: PDDL domain input
    :param verbose: display the parsed tree
    :return: the PDDL domain object
    """
    if file_stream:
        parser = parse_pddl_file(pddl)
    else:
        parser = parse_pddl_str(pddl)
    tree = parser.domain()
    LOGGER.debug(tree.toStringTree(recog=parser))
    vis = PDDLVisitor()
    return vis.visitDomain(tree)


def parse_problem(pddl: str,
                  file_stream: bool = False) -> Problem:
    """Parse a PDDL problem.

    :param pddl: PDDL problem input
    :param verbose: display the parsed tree
    :return: the PDDL problem object
    """
    if file_stream:
        parser = parse_pddl_file(pddl)
    else:
        parser = parse_pddl_str(pddl)
    tree = parser.problem()
    LOGGER.debug(tree.toStringTree(recog=parser))
    vis = PDDLVisitor()
    return vis.visitProblem(tree)
