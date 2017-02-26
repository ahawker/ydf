"""
    ydf/templating
    ~~~~~~~~~~~~~~

    Contains functions to be exported into the Jinja2 environment and accessible from templates.
"""

from ydf import meta


def to_docker_instruction(instruction):
    """
    Convert the given instruction object (parsed from YAML) to a Dockerfile instruction string.

    :param instruction: Python object representing a Dockerfile instruction.
    :return: String representation of the Dockerfile instruction.
    """
    name, arg = instruction.popitem()
    return meta.get_instruction(name, arg)(arg)
