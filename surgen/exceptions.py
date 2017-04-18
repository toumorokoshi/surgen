class SurgenException(Exception):
    pass


class ProcedureNotFound(SurgenException):
    pass


class TargetDriverNotFound(SurgenException):
    pass
