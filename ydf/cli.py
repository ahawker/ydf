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
@click.option('-v', '--variables',
              type=click.Path(dir_okay=False),
              help='YAML file containing variables to be exposed to YAML file and template during rendering')
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
def main(yaml, variables, template, search_path, output):
    """
    YAML to Dockerfile
    """
    yaml = yaml_ext.load(yaml.read())
    env = templating.environ(search_path)
    rendered = env.get_template(template).render(templating.render_vars(yaml))
    output.write(rendered)


if __name__ == '__main__':
    main()
