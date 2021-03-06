"""
    ydf/exceptions
    ~~~~~~~~~~~~~~

    Contains custom exceptions raised by `ydf`.
"""


class InstructionError(Exception):
    """
    Base exception type for all instruction related errors.
    """


class ArgumentUnknownType(InstructionError):
    """
    Exception raised when an instruction is given an argument type that we cannot process.
    """

    def __init__(self, arg):
        msg = 'Unknown argument type {}'.format(type(arg).__name__)
        super(ArgumentUnknownType, self).__init__(msg)


class ArgumentInstructionConstraintError(InstructionError):
    """
    Exception raised when an argument constraint decorates on a function that is not a instruction.
    """

    def __init__(self, func, constraint):
        msg = 'Function "{}" uses constraint "{}" decorator but is not an instruction'.format(func, constraint)
        super(ArgumentInstructionConstraintError, self).__init__(msg)


class ArgumentMissingError(InstructionError):
    """
    Exception raised when creation of an instruction is missing a required argument.
    """

    def __init__(self, name, arg, desc):
        msg = '[{}] - Name: {} - Desc: {}'.format(name, arg, desc)
        super(ArgumentMissingError, self).__init__(msg)


class ArgumentFormatError(InstructionError):
    """
    Exception raised when creation of an instruction is given an argument in an incorrect format.
    """

    def __init__(self, name, arg):
        msg = 'Instruction "{}" has malformed argument "{}"'.format(name, arg)
        super(ArgumentFormatError, self).__init__(msg)


class ArgumentDisjointedError(InstructionError):
    """
    Exception raised when creation of an instruction has two arguments set when only one or another can be used.
    """

    def __init__(self, name, arg1, arg2):
        msg = '[{}] - Name: {} - Other: {}'.format(name, arg1, arg2)
        super(ArgumentDisjointedError, self).__init__(msg)


class ArgumentTypeError(InstructionError):
    """
    Exception raised when creation of an instruction is given an argument of the wrong type.
    """

    def __init__(self, name, arg, expected_type, received_type):
        msg = '[{}] - Name: {} - Expected: {} - Received: {}'.format(name, arg, expected_type.__name__,
                                                                     received_type.__name__)
        super(ArgumentTypeError, self).__init__(msg)


class ArgumentPatternError(InstructionError):
    """
    Exception raised when an argument does not match the expected regex pattern.
    """

    def __init__(self, name, arg, pattern):
        msg = '[{}] - Name: {} - Pattern: {}'.format(name, arg, pattern)
        super(ArgumentPatternError, self).__init__(msg)


class ArgumentNumericBoundsError(InstructionError):
    """
    Exception raised when an argument is given a numeric value that is not within the
    expected lower/upper bounds.
    """

    def __init__(self, name, arg, value, lower, upper):
        msg = '[{}] - Name: {} - Value: {} - Lower: {} - Upper: {}'.format(name, arg, value, lower, upper)
        super(ArgumentNumericBoundsError, self).__init__(msg)


class ArgumentCollectionLengthError(InstructionError):
    """
    Exception raised when an argument is a collection and is not of the expected size.
    """

    def __init__(self, name, arg, expected_length, received_length):
        msg = '[{}] - Name: {} - Expected: {} - Received: {}'.format(name, arg, expected_length, received_length)
        super(ArgumentCollectionLengthError, self).__init__(msg)


class ArgumentInstructionUnknownError(InstructionError):
    """
    Exception raised when an argument that requires a child instruction is given one that is unknown.
    """

    def __init__(self, name, arg):
        msg = '[{}] - Name: {}'.format(name, arg)
        super(ArgumentInstructionUnknownError, self).__init__(msg)
