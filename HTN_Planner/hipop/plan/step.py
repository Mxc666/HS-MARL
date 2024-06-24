class Step:
    def __init__(self, start: int, end: int, operator: str):
        self.__start = start
        self.__end = end
        self.__operator = operator

    @property
    def start(self) -> int:
        return self.__start

    @property
    def end(self) -> int:
        return self.__end

    @property
    def operator(self) -> str:
        return self.__operator

    def __str__(self) -> str:
        return f"step [{self.start}] {self.operator} [{self.end}]"

    def __eq__(self, other: 'Step'):
        return (self.__start == other.__start
                and self.__end == other.__end
                and self.__operator == other.__operator)