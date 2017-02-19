"""
    ydf/arguments
    ~~~~~~~~~~~~~

    Decorators to define arguments with constraints.
"""

import functools
import re

from ydf import exceptions, meta


def required(name, required_type):
    """
    Decorate an instruction function to enforce a value presence and type constraint on the
    instruction argument.

    :param name: Argument name
    :param required_type: Argument type
    """
    def decorator(func):
        if not meta.is_instruction(func):
            raise exceptions.ArgumentInstructionConstraintError(func.__name__, required.__name__)

        @functools.wraps(func)
        def wrapper(arg):
            if not arg:
                raise exceptions.ArgumentMissingError(func.instruction_name, name, func.instruction_desc)
            if not isinstance(arg, required_type):
                raise exceptions.ArgumentTypeError(func.instruction_name, name, required_type, type(arg))
            return func(arg)
        return wrapper
    return decorator


def required_numeric_bounds(name, lower, upper):
    """
    Decorate an instruction function which consumes an integration to enforce a lower and upper bound
    on the value.

    :param name: Argument name
    :param lower: Lower bound of the argument value (inclusive)
    :param upper: Upper bound of the argument value (inclusive)
    """
    def decorator(func):
        if not meta.is_instruction(func):
            raise exceptions.ArgumentInstructionConstraintError(func.__name__, required_numeric_bounds.__name__)

        @functools.wraps(func)
        def wrapper(arg):
            if not (lower <= arg <= upper):
                raise exceptions.ArgumentNumericBoundsError(func.instruction_name, name, arg, lower, upper)
            return func(arg)
        return wrapper
    return decorator


def required_regex_match(name, pattern):
    """
    Decorate an instruction function which consumes a string to run a regex capture against it.

    :param name: Argument name
    :param pattern: Regex pattern
    """
    def decorator(func):
        if not meta.is_instruction(func):
            raise exceptions.ArgumentInstructionConstraintError(func.__name__, required_regex_match.__name__)

        @functools.wraps(func)
        def wrapper(arg):
            match = re.match(pattern, arg)
            if not match:
                raise exceptions.ArgumentPatternError(func.instruction_name, name, pattern)
            return func(match.groupdict())
        return wrapper
    return decorator


def required_dict_key(name, required_type):
    """
    Decorate an instruction function which consumes a dict to enforce a key presence and type constraint on the
    value within the instruction argument.

    :param name: Name of dict key
    :param required_type: Type of value at dict key
    """
    def decorator(func):
        if not meta.is_instruction(func):
            raise exceptions.ArgumentInstructionConstraintError(func.__name__, required_dict_key.__name__)

        @functools.wraps(func)
        def wrapper(arg):
            value = arg.get(name)
            if value is None:
                raise exceptions.ArgumentMissingError(func.instruction_name, name, func.instruction_desc)
            if not isinstance(value, required_type):
                raise exceptions.ArgumentTypeError(func.instruction_name, name, required_type, type(value))
            return func(arg)
        return wrapper
    return decorator


def optional_dict_key(name, required_type, mutually_exclusive_with=None):
    """
    Decorate an instruction function which consumes a dict to optionally enforce a key presence and type constraint
    on the value within the instruction argument.

    :param name: Name of the optional dict key
    :param required_type: If key is present, type of the value of within the dict
    :param mutually_exclusive_with: If present, raise if this key is also in the dict
    """
    def decorator(func):
        if not meta.is_instruction(func):
            raise exceptions.ArgumentInstructionConstraintError(func.__name__, optional_dict_key.__name__)

        @functools.wraps(func)
        def wrapper(arg):
            value = arg.get(name)
            if value is not None:
                if not isinstance(value, required_type):
                    raise exceptions.ArgumentTypeError(func.instruction_name, name, required_type, type(value))
                if mutually_exclusive_with is not None and mutually_exclusive_with in arg:
                    raise exceptions.ArgumentDisjointedError(func.instruction_name, name, mutually_exclusive_with)
            return func(arg)
        return wrapper
    return decorator
