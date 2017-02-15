"""
    ydf/exceptions
    ~~~~~~~~~~~~~~

    Contains custom exceptions raised by `ydf`.
"""


class InstructionError(Exception):
    """
    Base exception type for all instruction related errors.
    """


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
