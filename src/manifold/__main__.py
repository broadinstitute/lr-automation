import click

# porcelain
from .add import command as add
from .call import command as call
from .filter import command as filter
from .remove import command as remove
from .view import command as view
from .version import command as version

# plumbing
from .party import command as party


@click.group(name="manifold")
def main_entry():
    pass


# porcelain
main_entry.add_command(add.main)
main_entry.add_command(call.main)
main_entry.add_command(filter.main)
main_entry.add_command(remove.main)
main_entry.add_command(view.main)
main_entry.add_command(version.main)

# plumbing
main_entry.add_command(party.main)


if __name__ == '__main__':
    main_entry()