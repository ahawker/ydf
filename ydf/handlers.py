"""
    ydf/handlers
    ~~~~~~~~~~~~

    Contains functionality for dealing with type handler functions.
"""

import functools


def handles(handles_type):
    """
    Decorate methods to indicate what python type they support instruction conversion from.

    :param handles_type: Type they support conversion from.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        wrapper.__handles_type__ = handles_type
        return wrapper
    return decorator


def get_type_handlers(cls):
    """
    Process the given :class:`~ydf.instructions.Instruction` derived class for type handler functions
    that are decorated with :func:`~ydf.handlers.handles`.

    :param cls: A :class:`~ydf.instructions.Instruction` derived class
    :return: A dict containing all functions decorated with :func:`~ydf.handlers.handles`
    """
    return dict(((handler.__handles_type__, handler)
                 for handler in (getattr(cls, attr)
                                 for attr in dir(cls)) if hasattr(handler, '__handles_type__')))
