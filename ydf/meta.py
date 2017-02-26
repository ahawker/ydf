"""
    ydf/meta
    ~~~~~~~~

    Functionality for inspecting python objects to find instruction definitions.
"""

import collections
import importlib
import sys

from ydf import exceptions


INSTRUCTIONS_CACHE = None
INSTRUCTIONS_MODULE_NAME = 'ydf.instructions'


def is_instruction(func):
    """
    Check the given function to see if it's an instruction.

    A instruction is a function that is decorated with :func:`~ydf.instructions.instruction`.

    :param func: Object to check
    :return: `True` if object is an instruction function, `False` otherwise
    """
    return callable(func) and hasattr(func, 'instruction_name')


def get_instruction_arg_type(arg):
    """
    Determine the in instruction_type from the instruction argument.

    :param arg: Argument object to pass to the instruction
    :return: A type object that maps to the instruction argument runtime type
    """
    if isinstance(arg, collections.Mapping):
        return dict
    if isinstance(arg, (list, tuple)):
        return list
    if isinstance(arg, str):
        return str
    if isinstance(arg, int):
        return int
    if isinstance(arg, type(None)):
        return type(None)

    raise exceptions.ArgumentUnknownType(arg)


def get_instruction(instruction_name, instruction_type, module_name=INSTRUCTIONS_MODULE_NAME, cached=True):
    """
    Get the function that is decorated with :func:`~ydf.instructions.instruction` for the given
    instruction name and type.

    :param instruction_name: Name of instruction to search for
    :param instruction_type: Type of instruction arguments
    :param module_name: Name of the module to scan for instructions
    :param cached: Flag indicating if caller is OK with receiving cached instructions.
    :return:
    """
    instructions = get_instructions(module_name, cached)

    instruction_name = instruction_name.upper()
    instruction_type = get_instruction_arg_type(instruction_type)
    return instructions[instruction_name][instruction_type]


def get_instructions(module_name=INSTRUCTIONS_MODULE_NAME, cached=True):
    """
    Get all functions within this module that are decorated with :func:`~ydf.instructions.instruction`.

    :param module_name: Name of the module to scan for instructions
    :param cached: Flag indicating if caller is OK with receiving cached instructions.
    """
    global INSTRUCTIONS_CACHE

    if INSTRUCTIONS_CACHE is None or not cached:
        if module_name not in sys.modules:
            importlib.import_module(module_name)
        module = sys.modules[module_name]

        INSTRUCTIONS_CACHE = collections.defaultdict(dict)

        for func in (val for attr, val in ((a, getattr(module, a)) for a in dir(module)) if is_instruction(val)):
            instruction_name = func.instruction_name.upper()
            instruction_type = func.instruction_type
            INSTRUCTIONS_CACHE[instruction_name][instruction_type] = func

    return INSTRUCTIONS_CACHE
