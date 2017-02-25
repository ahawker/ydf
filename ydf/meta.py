"""
    ydf/meta
    ~~~~~~~~

    Functionality for inspecting python objects.
"""

import collections
import sys


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
    return instructions[instruction_name.upper()][instruction_type]


def get_instructions(module_name=INSTRUCTIONS_MODULE_NAME, cached=True):
    """
    Get all functions within this module that are decorated with :func:`~ydf.instructions.instruction`.

    :param module_name: Name of the module to scan for instructions
    :param cached: Flag indicating if caller is OK with receiving cached instructions.
    """
    global INSTRUCTIONS_CACHE

    if INSTRUCTIONS_CACHE is None or not cached:
        module = sys.modules.get(module_name)
        if not module:
            raise ValueError('Module {} not found; you must import it prior to this call'.format(module_name))

        INSTRUCTIONS_CACHE = collections.defaultdict(dict)

        for func in (value for attr, value in ((a, getattr(module, a)) for a in dir(module)) if is_instruction(value)):
            INSTRUCTIONS_CACHE[func.instruction_name][func.instruction_type] = func

    return INSTRUCTIONS_CACHE
