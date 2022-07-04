import click


# Version number is automatically set via bumpversion.  Do not modify.
__version__ = "0.0.9"


@click.command(name="version")
def main():
    """Display the current version."""
    click.echo(f'manifold {__version__}')