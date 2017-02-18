"""
    ydf/instructions
    ~~~~~~~~~~~~~~~~

    Convert objects parsed from YAML to those that represent Dockerfile instructions.
"""

import collections
import functools
import json

from ydf import arguments, descriptions, formatting, meta


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


@arguments.required_regex_match(name='string', pattern='(?P<image>\w+)(?P<delimiter>[:@])?(?P<tag_or_digest>\w+)?')
@arguments.required(name='capture', required_type=dict)
@instruction(name=FROM, type=str, desc=descriptions.FROM_STR)
def from_str(arg):
    """
    Convert a :class:`~str` to a `FROM` instruction.

    :param arg: String that represents instruction arguments.
    :return: Fully-qualified `FROM` instruction string.
    """
    image, delimiter, tag_or_digest = (arg.get(k) for k in ('image', 'delimiter', 'tag_or_digest'))
    return formatting.str_join_with_conditional_delimiter((image, tag_or_digest), delimiter)


@arguments.optional_dict_key(name='digest', required_type=str, mutually_exclusive_with='tag')
@arguments.optional_dict_key(name='tag', required_type=str, mutually_exclusive_with='digest')
@arguments.required_dict_key(name='image', required_type=str)
@arguments.required(name='dict', required_type=dict)
@instruction(name=FROM, type=dict, desc=descriptions.FROM_DICT)
def from_dict(arg):
    """
    Convert a :class:`~dict` to a `FROM` instruction.

    :param arg: Dict that represents instruction arguments.
    :return: Fully-qualified `FROM` instruction string.
    """
    image, tag, digest = (arg.get(k) for k in ('image', 'tag', 'digest'))
    delimiter = ':' if tag else '@'
    return formatting.str_join_with_conditional_delimiter((image, tag, digest), delimiter)


@arguments.required(name='string', required_type=str)
@instruction(name=RUN, type=str, desc=descriptions.RUN_STR)
def run_str(arg):
    """
    Convert a :class:`~str` to a `RUN` instruction.

    :param arg: String that represents instruction arguments.
    :return: Fully-qualified `RUN` instruction.
    """
    return arg


@arguments.required(name='list', required_type=list)
@instruction(name=RUN, type=list, desc=descriptions.RUN_LIST)
def run_list(arg):
    """
    Convert a :class:`~list` to a `RUN` instruction.

    :param arg: List that represents instruction arguments.
    :return: Fully-qualified `RUN` instruction.
    """
    indent = len(run_list.instruction_name) + 1
    return formatting.list_with_conditional_line_breaks(arg, indent=indent, quote_escape=True)


@arguments.optional_dict_key(name='params', required_type=list)
@arguments.required_dict_key(name='executable', required_type=str)
@arguments.required(name='dict', required_type=dict)
@instruction(name=RUN, type=dict, desc=descriptions.RUN_DICT)
def run_dict(arg):
    """
    Convert a :class:`~dict` to a `RUN` instruction.

    :param arg: Dict that represents instruction arguments.
    :return: Fully-qualified `RUN` instruction.
    """
    executable = arg['executable']
    params = arg.get('params', [])
    return json.dumps([executable, *params])


@arguments.required(name='string', required_type=str)
@instruction(name=CMD, type=str, desc=descriptions.CMD_STR)
def cmd_str(arg):
    """
    Convert a :class:`~str` to a `CMD` instruction.

    :param arg: String that represents instruction arguments.
    :return: Fully-qualified `CMD` instruction.
    """
    return arg


@arguments.required(name='list', required_type=list)
@instruction(name=CMD, type=list, desc=descriptions.CMD_LIST)
def cmd_list(arg):
    """
    Convert a :class:`~list` to a `CMD` instruction.

    :param arg: List that represents instruction arguments.
    :return: Fully-qualified `CMD` instruction.
    """
    return json.dumps(arg)


@arguments.optional_dict_key(name='params', required_type=list)
@arguments.required_dict_key(name='executable', required_type=str)
@arguments.required(name='dict', required_type=dict)
@instruction(name=CMD, type=dict, desc=descriptions.CMD_LIST)
def cmd_dict(arg):
    """
    Convert a :class:`~dict` to a `CMD` instruction.

    :param arg: Dict that represents instruction arguments.
    :return: Fully-qualified `CMD` instruction.
    """
    executable = arg['executable']
    params = arg.get('params', [])
    return json.dumps([executable, *params])


@arguments.required(name='dict', required_type=dict)
@instruction(name=LABEL, type=dict, desc=descriptions.LABEL_DICT)
def label_dict(arg):
    """
    Convert a :class:`~dict` to a `LABEL` instruction.

    :param arg: Dict that represents instruction arguments.
    :return: Fully-qualified `LABEL` instruction.
    """
    indent = len(label_dict.instruction_name) + 1
    return formatting.dict_with_conditional_line_breaks(arg, indent=indent)


@arguments.required(name='int', required_type=int)
@instruction(name=EXPOSE, type=int, desc=descriptions.EXPOSE_INT)
def expose_int(arg):
    """
    Convert a :class:`~int` to a `EXPOSE` instruction.

    :param arg: Int that represents instruction arguments.
    :return: Fully-qualified `EXPOSE` instruction.
    """
    return str(arg)


@arguments.required(name='list', required_type=list)
@instruction(name=EXPOSE, type=list, desc=descriptions.EXPOSE_LIST)
def expose_list(arg):
    """
    Convert a :class:`~list` to a `EXPOSE` instruction.

    :param arg: List that represents instruction arguments.
    :return: Fully-qualified `EXPOSE` instruction.
    """
    return formatting.str_join_with_conditional_delimiter(arg, delimiter=' ')


@arguments.required(name='str', required_type=str)
@instruction(name=ENV, type=str, desc=descriptions.ENV_STR)
def env_str(arg):
    """
    Convert a :class:`~str` to a `ENV` instruction.

    :param arg: String that represents an instruction arguments.
    :return: Fully-qualified `ENV` instruction.
    """
    return arg


@arguments.required(name='dict', required_type=dict)
@instruction(name=ENV, type=dict, desc=descriptions.ENV_DICT)
def env_dict(arg):
    """
    Convert a :class:`~dict` to a `ENV` instruction.

    :param arg: Dict that represents an instruction arguments.
    :return: Fully-qualified `ENV` instruction.
    """
    indent = len(env_dict.instruction_name) + 1
    return formatting.dict_with_conditional_line_breaks(arg, indent=indent)


@arguments.required(name='str', required_type=str)
@instruction(name=ADD, type=str, desc=descriptions.ADD_STR)
def add_str(arg):
    """
    Convert a :class:`~str` to a `ADD` instruction.

    :param arg: String that represents an instruction arguments.
    :return: Fully-qualified `ADD` instruction.
    """
    return arg


@arguments.required(name='list', required_type=list)
@instruction(name=ADD, type=list, desc=descriptions.ADD_LIST)
def add_list(arg):
    """
    Convert a :class:`~list` to a `ADD` instruction.

    :param arg: List that represents an instruction arguments.
    :return: Fully-qualified `ADD` instruction.
    """
    return json.dumps(arg)


@arguments.required(name='str', required_type=str)
@instruction(name=COPY, type=str, desc=descriptions.COPY_STR)
def copy_str(arg):
    """
    Convert a :class:`~str` to a `COPY` instruction.

    :param arg: String that represents an instruction arguments.
    :return: Fully-qualified `COPY` instruction.
    """
    return arg


@arguments.required(name='list', required_type=list)
@instruction(name=COPY, type=list, desc=descriptions.COPY_LIST)
def copy_list(arg):
    """
    Convert a :class:`~list` to a `COPY` instruction.

    :param arg: List that represents an instruction arguments.
    :return: Fully-qualified `COPY` instruction.
    """
    return json.dumps(arg)
