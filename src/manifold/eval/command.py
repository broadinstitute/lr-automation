import click


@click.command(name="eval")
def main():
    """Evaluate called variants against a truth dataset"""
    click.echo('eval')