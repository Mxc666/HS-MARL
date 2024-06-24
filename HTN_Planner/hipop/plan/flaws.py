class FlawUnresolvable(Exception):
    pass

class AbstractFlaw:
    def __init__(self, step: int, task: str):
        self.__step = step
        self.__task = task

    @property
    def step(self) -> int:
        return self.__step

    @property
    def task(self) -> str:
        return self.__task

    def __int__(self) -> int:
        return self.__step

    def __str__(self) -> str:
        return f"AbstractFlaw [{self.step}] {self.task}"

    def __eq__(self, other: 'AbstractFlaw') -> bool:
        return int(self) == int(other)

    def __hash__(self) -> int:
        return self.__step
    

class OpenLink:
    def __init__(self, step: int, atom: int, value: bool):
        self.__step = step
        self.__atom = atom
        self.__value = value
    
    @property
    def step(self) -> int:
        return self.__step

    @property
    def atom(self) -> int:
        return self.__atom

    @property
    def value(self) -> bool:
        return self.__value

    def __str__(self) -> str:
        return f"OL step {self.step} literal {'' if self.value else 'not '}{self.atom}"

    def __bool__(self) -> bool:
        return self.value

    def __eq__(self, other) -> bool:
        return (self.__step == other.__step
                and self.__atom == other.__atom
                and self.__value == other.__value)

    def __hash__(self) -> int:
        return tuple.__hash__((self.step, self.atom))


class Threat:
    def __init__(self, step: int, link: 'CausalLink'):
        self.__step = step
        self.__link = link

    @property
    def step(self) -> int:
        return self.__step

    @property
    def link(self) -> 'CausalLink':
        return self.__link

    def __str__(self) -> str:
        return f"Threat {self.step} on {self.link}"

    def __eq__(self, other: 'Threat') -> bool:
        return (self.__step == other.__step
                and self.__link == other.__link)
