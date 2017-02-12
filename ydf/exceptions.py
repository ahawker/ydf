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

    def __init__(self, name, arg):
        msg = 'Instruction "{}" is missing argument "{}"'.format(name, arg)
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
        msg = 'Instruction "{}" supports "{}" or "{}" arguments not both'.format(name, arg1, arg2)
        super(ArgumentDisjointedError, self).__init__(msg)


class ArgumentTypeError(InstructionError):
    """
    Exception raised when creation of an instruction is given an argument of the wrong type.
    """

    def __init__(self, name, arg, expected_type, unexpected_type):
        msg = 'Instruction "{}" expects argument "{}" of type "{}" but got "{}"'.format(name, arg,
                                                                                        expected_type.__name__,
                                                                                        unexpected_type.__name__)
        super(ArgumentTypeError, self).__init__(msg)
