import click


@click.command(name="add")
def main():
    """Add data to the database."""
    click.echo('add')