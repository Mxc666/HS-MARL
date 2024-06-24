"""Writing functions to export a model as a PDDL file.

Uses *jinja2* to define PDDL templates.
"""

from jinja2 import Template

from .domain import Domain
from .problem import Problem

DOMAIN_TEMPLATE = Template("""
(define (domain {{ domain.name }})
    {% if domain.requirements %}(:requirements
        {%- for x in domain.requirements %}{{ x }}{% endfor %}){% endif %}
    {% if domain.types %}(:types
        {%- for x in domain.types %} {{ x }}{% endfor %}){% endif %}
    {% if domain.constants %}(:constants
        {%- for x in domain.constants %} {{ x }}{% endfor %}){% endif %}
    {% if domain.predicates %}(:predicates {% for x in domain.predicates %}
        ({{ x.name }}{% for v in x.variables %} {{ v }}{% endfor %})
        {%- endfor %}
    ){% endif %}
    {% for t in domain.tasks %}
    (:task {{ t.name }}
        {% if t.parameters %}:parameters (
            {%- for v in t.parameters %} {{ v }}{% endfor %} ){% endif %}
    )
    {% endfor %}
    {% for m in domain.methods %}
    (:method {{ m.name }}
        {% if m.parameters %}:parameters (
            {%- for v in m.parameters %} {{ v }}{% endfor %} ){% endif %}
        :task {{ m.task }}
        {% if m.precondition %}:precondition {{ m.precondition }}{% endif %}
        :subtasks (and {% for s in m.network.subtasks %}
            ({{ s[0] }} {{ s[1] }}){% endfor %}
        )
        :ordering (and {% for head, tail in m.network.ordering.items() %}
            {% for t in tail %}({{ head }} < {{ t }})
            {%- endfor %}{% endfor %}
        )
    )
    {% endfor %}
    {% for a in domain.actions %}
    (:action {{ a.name }}
        {% if a.parameters %}:parameters (
            {%- for v in a.parameters %} {{ v }}{% endfor %} ){% endif %}
        {% if a.precondition %}:precondition {{ a.precondition }}{% endif %}
        {% if a.effect %}:effect ({{ a.effect }}){% endif %}
        {% if a.observe %}:observe ({{ a.observe }}){% endif %}
    )
    {% endfor %}
)
""")

PROBLEM_TEMPLATE = Template("""
(define (problem {{ problem.name }})
    (:domain {{ problem.domain }})
    {% if problem.requirements %}(:requirements
        {%- for x in problem.requirements %} {{ x }}{% endfor %}){% endif %}
    {% if problem.objects %}(:objects
        {%- for x in problem.objects %} {{ x }}{% endfor %}){% endif %}
    {% if problem.htn %}(:htn
        {% if problem.htn.parameters %}:parameters (
            {%- for v in problem.htn.parameters %} {{ v }}{% endfor -%}
            ){% endif %}
        :subtasks (and {% for s in problem.htn.network.subtasks %}
            ({{ s[0] }} {{ s[1] }}){% endfor %}
        )
        :ordering (and
            {%- for head, tail in problem.htn.network.ordering.items() %}
            {% for t in tail %}({{ head }} < {{ t }})
            {%- endfor %}{% endfor %}
        )
    ){% endif %}
    (:init (and {% for i in problem.init %}
        {{ i }}{% endfor %}
        )
    )
    {% if problem.goal %}(:goal
        {{ problem.goal }}
    ){% endif %}
)
""")


def write_domain(domain: Domain) -> str:
    """Render a domain as a PDDL string.

    :param domain: domain model
    :return: domain in PDDL syntax
    """
    return DOMAIN_TEMPLATE.render(domain=domain)


def write_problem(problem: Problem) -> str:
    """Render a problem as a PDDL string.

    :param problem: problem model
    :return: problem in PDDL syntax
    """
    return PROBLEM_TEMPLATE.render(problem=problem)
