class GroundingImpossibleError(Exception):
    def __init__(self, what: str, why: str):
        self.__what = what
        self.__why = why

    @property
    def message(self):
        return f"Grounding of {self.__what} impossible for {self.__why}"


class ContradictoryEffects(GroundingImpossibleError):
    pass

class TypingAssignmentInconsistent(GroundingImpossibleError):
    pass

class PreconditionUnsatisfiable(GroundingImpossibleError):
    pass

class RequirementException(Exception):
    def __init__(self, requirement):
        self.__requirement = requirement

    @property
    def message(self):
        return f"Requirement {self.__requirement}"

class RequirementNotSupported(RequirementException):
    @property
    def message(self):
        return f"{RequirementException.message(self)} not supported"


class RequirementMissing(RequirementException):
    @property
    def message(self):
        return f"{RequirementException.message(self)} missing"
