import click
from jinja2 import Environment, FileSystemLoader, TemplateNotFound
import os
import sys

@click.command()
@click.option('--name', prompt='Project name', help='The name of the project')
@click.option('--version', prompt='Project version', default='', show_default=False)
@click.option('--description', prompt='Project description')
@click.option('--homepage', prompt='Project homepage', default='', show_default=False)
@click.option('--demo', prompt='Project demo URL', default='', show_default=False)
@click.option('--docs', prompt='Project documentation URL', default='', show_default=False)
@click.option('--author', prompt='Author name')
@click.option('--github', prompt='GitHub username', default='', show_default=False)
@click.option('--website', prompt='Author website', default='', show_default=False)
@click.option('--twitter', prompt='Twitter username', default='', show_default=False)
@click.option('--linkedin', prompt='LinkedIn username', default='', show_default=False)
@click.option('--patreon', prompt='Patreon username', default='', show_default=False)
@click.option('--license', prompt='License name', default='', show_default=False)
@click.option('--issues', prompt='Issues page URL', default='', show_default=False)
@click.option('--contributing', prompt='Contributing guide URL', default='', show_default=False)
@click.option('--install', prompt='Install command', default='', show_default=False)
@click.option('--usage', prompt='Usage command or instruction', default='', show_default=False)
@click.option('--test', prompt='Test command', default='', show_default=False)
@click.option('--use-html', is_flag=True, help='Include HTML in README.md output')
@click.option('--template', type=click.Choice(['default', 'minimal']), default='default')
def main(**kwargs):
    try:
        templates_dir = os.path.join(os.path.dirname(__file__), 'templates')
        env = Environment(loader=FileSystemLoader(templates_dir))
        template = env.get_template(f"{kwargs['template']}.md")

        readme_content = template.render(**kwargs)

        with open('README.md', 'w', encoding='utf-8', errors='replace') as f:
            f.write(readme_content)

        click.echo("✅ README.md has been generated successfully!")
        click.echo(f"📄 Path: {os.path.abspath('README.md')}")
    except TemplateNotFound:
        click.echo(f"❌ Error: Template '{kwargs['template']}.md' not found in {templates_dir}", err=True)
        sys.exit(1)
    except Exception as e:
        click.echo(f"❌ An error occurred: {str(e)}", err=True)
        sys.exit(1)

if __name__ == '__main__':
    main()
