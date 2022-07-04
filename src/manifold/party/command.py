import click


@click.command(name="party", hidden=True)
def main():
    """Have a party!"""
    click.echo('party')