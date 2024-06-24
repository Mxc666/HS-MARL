"""Classes related to the Domain variables and types."""

from typing import List


class Type:

    """PDDL type.

    :param name: type name
    :param type: supertype name
    """

    def __init__(self, name: str, supertype: str = 'object'):
        self.__name = name
        self.__type = supertype

    @property
    def name(self) -> str:
        """Get type name."""
        return self.__name

    @property
    def type(self) -> str:
        """Get super type."""
        return self.__type

    def __str__(self):
        if self.type:
            return "{} - {}".format(self.name, self.type)
        return self.name


class Constant(Type):

    """PDDL constant."""


class Variable(Type):

    """Variable used in predicates and similar constructs."""


class Predicate:

    """PDDL predicate.

    :param name: predicate name
    :param variables: predicate variables
    """

    def __init__(self, name: str, variables: List[Variable] = ()):
        self.__name = name
        self.__variables = variables

    @property
    def name(self) -> str:
        """Get name."""
        return self.__name

    @property
    def variables(self) -> List[Variable]:
        """Get variables."""
        return self.__variables

    def __str__(self):
        return f"{self.__name} {' '.join(map(str, self.__variables))}"

    def __lt__(self, other: 'Predicate'):
        return self.__name < other.__name