"""
    ydf/cli
    ~~~~~~~

    Defines the command-line interface.
"""

import click
import sys

from ydf import templating, yaml_ext


@click.command('ydf')
@click.argument('yaml',
                type=click.Path(dir_okay=False))
@click.option('-t', '--template',
              type=str,
              default=templating.DEFAULT_TEMPLATE_NAME,
              help='Name of Jinja2 template used to build Dockerfile')
@click.option('-s', '--search-path',
              type=click.Path(file_okay=False, resolve_path=True),
              multiple=True,
              default=[templating.DEFAULT_TEMPLATE_PATH],
              help='File system path to search for templates')
@click.option('-o', '--output',
              type=click.File('w'),
              default=sys.stdout,
              help='Dockerfile generated from translation')
def main(yaml, template, search_path, output):
    """
    YAML to Dockerfile.
    """
    search_path = search_path + (templating.DEFAULT_TEMPLATE_PATH,)
    yaml = yaml_ext.load_file(yaml)
    dockerfile = templating.render(yaml, template, search_path)
    output.write(dockerfile)


if __name__ == '__main__':
    main()
