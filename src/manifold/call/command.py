import click


@click.command(name="call")
def main():
    """Call variants in the graph."""
    click.echo('call')