"""
    ydf/meta
    ~~~~~~~~

    Functionality for inspecting python objects.
"""


def is_instruction(func):
    """
    Check the given function to see if it's an instruction.

    A instruction is a function that is decorated with :func:`~ydf.instructions.instruction`.

    :param func: Object to check
    :return: `True` if object is an instruction function, `False` otherwise
    """
    return callable(func) and hasattr(func, 'instruction_name')
