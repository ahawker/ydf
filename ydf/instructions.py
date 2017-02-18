"""
    ydf/instructions
    ~~~~~~~~~~~~~~~~

    Convert objects parsed from YAML to those that represent Dockerfile instructions.
"""

import collections
import functools

from ydf import meta


__all__ = []


FROM = 'FROM'
RUN = 'RUN'
CMD = 'CMD'
LABEL = 'LABEL'
EXPOSE = 'EXPOSE'
ENV = 'ENV'
ADD = 'ADD'
COPY = 'COPY'
ENTRYPOINT = 'ENTRYPOINT'
VOLUME = 'VOLUME'
USER = 'USER'
WORKDIR = 'WORKDIR'
ARG = 'ARG'
ONBUILD = 'ONBUILD'
STOPSIGNAL = 'STOPSIGNAL'
HEALTHCHECK = 'HEALTHCHECK'
SHELL = 'SHELL'


def get_instructions():
    """
    Get all functions within this module that are decorated with :func:`~ydf.instructions.instruction`.
    """
    instructions = collections.defaultdict(dict)
    for func in (value for key, value in globals().items() if meta.is_instruction(value)):
        instructions[func.instruction_name][func.instruction_type] = func
    return instructions


def instruction(name, type, desc):
    """
    Decorate a function to indicate that it is responsible for converting a python type to a Docker
    instruction.

    :param name: Name of docker instruction
    :param type: Type of python object it can convert
    :param desc: Short description of expected format for the python object.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return '{} {}'.format(name, func(*args, **kwargs))
        wrapper.instruction_name = name
        wrapper.instruction_type = type
        wrapper.instruction_desc = desc
        return wrapper
    return decorator
