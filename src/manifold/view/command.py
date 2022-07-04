import click


@click.command(name="view")
def main():
    """View data in the graph."""
    click.echo('view')