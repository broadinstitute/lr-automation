import click


@click.command(name="remove")
def main():
    """Remove data from the database."""
    click.echo('remove')