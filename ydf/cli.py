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
@click.option('-b', '--build-variables',
              type=click.Path(dir_okay=False),
              help='YAML file containing build variables')
@click.option('-v', '--template-variables',
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
def main(yaml, build_variables, template_variables, template, search_path, output):
    """
    YAML to Dockerfile
    """
    # Always include the default template directory as the last fallback search location.
    search_path = search_path + (templating.DEFAULT_TEMPLATE_PATH,)

    # Run YAML file through template rendering, parameterized by optional variables YAML file.
    variables = yaml_ext.load_file(template_variables) if template_variables else {}
    yaml = templating.render(variables, yaml, search_path)

    # Run Dockerfile through template rendering, parameterized by YAML file.
    dockerfile = templating.render(yaml_ext.load(yaml), template, search_path)
    output.write(dockerfile)


if __name__ == '__main__':
    main()
