"""
    ydf/templating
    ~~~~~~~~~~~~~~

    Contains functions to be exported into the Jinja2 environment and accessible from templates.
"""

import jinja2
import os

from ydf import instructions, __version__


DEFAULT_TEMPLATE_NAME = 'default.tpl'
DEFAULT_TEMPLATE_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'templates')


def _render_vars(yaml_vars):
    """
    Build a dict containing all variables accessible to a template during the rendering process.

    This is a merge of the YAML variables parsed from the file + build variables defined by :mod:`~ydf` itself.

    :param yaml_vars: Parsed from the parsed YAML file.
    :return: Dict of all variables available to template.
    """
    return dict(ydf=dict(version=__version__), **(yaml_vars or {}))


def _environ(path=DEFAULT_TEMPLATE_PATH, **kwargs):
    """
    Build a Jinja2 environment for the given template directory path and options.

    :param path: Path to search for Jinja2 template files
    :param kwargs: Options to configure the environment
    :return: :class:`~jinja2.Environment` instance
    """
    kwargs.setdefault('trim_blocks', True)
    kwargs.setdefault('lstrip_blocks', True)

    env = jinja2.Environment(loader=jinja2.FileSystemLoader(path), **kwargs)
    env.globals[instructions.convert_instruction.__name__] = instructions.convert_instruction

    return env


def render(yaml_vars, template=DEFAULT_TEMPLATE_NAME, path=DEFAULT_TEMPLATE_PATH):
    """
    Render a template.

    :param yaml_vars: Mapping of variables parsed from a YAML file.
    :param template: Name of template file to render
    :param path: Path on disk to search for templates to render
    :return: The rendered template.
    """
    env = _environ(path)
    return env.get_template(template).render(_render_vars(yaml_vars))
