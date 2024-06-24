from io import TextIOBase
from typing import Union, List
import logging

from ..plan.plan import HierarchicalPartialPlan
from ..grounding.problem import Problem

LOGGER = logging.getLogger(__name__)


def output_ipc2020_hierarchical(plan: HierarchicalPartialPlan,
                                problem: Problem,
                                out_stream: TextIOBase):
    out_stream.write("==>\n")
    index_map = {}
    step_index = 1
    
    # Action sequence
    seq_plan = list(plan.sequential_plan())
    for (index, step) in seq_plan:
        if problem.has_action(step.operator):
            index_map[index] = step_index
            out_stream.write(f"{step_index} {step.operator}\n")
            step_index += 1
    
    # Tasks
    for (index, step) in seq_plan:
        if problem.has_task(step.operator):
            index_map[index] = step_index
            step_index += 1
            if step.operator in ['__top', '(__top )']:
                root_task = index
    LOGGER.debug("index mapping: %s", index_map)
    
    # Root Task
    decomposition = plan.get_decomposition(root_task)
    root_subtasks = [index_map[x] for (x, s) in seq_plan 
                     if not problem.has_method(s.operator)
                     if x in decomposition.substeps]
    out_stream.write(f"root {' '.join(map(str, root_subtasks))}\n")
    
    # Hierarchy
    for (index, step) in seq_plan:
        if problem.has_task(step.operator):
            if index == root_task:
                continue
            decomposition = plan.get_decomposition(index)
            method = problem.method(decomposition.method)
            subtasks = [index_map[x] for (x, s) in seq_plan 
                        if x in decomposition.substeps
                        if not problem.has_method(s.operator)]
            out_stream.write(f"{index_map[index]} {step.operator} -> {method.name} ")
            out_stream.write(" ".join(map(str, subtasks)))
            out_stream.write("\n")
            step_index += 1
    
    # End
    out_stream.write("<==\n")

def output_ipc2020_flat(plan: List[str],
                        out_stream: TextIOBase):
    out_stream.write("==>\n")
    # Action sequence
    for step in range(len(plan)):
        out_stream.write(f"{step} {plan[step]}\n")
    # End
    out_stream.write("<==\n")
