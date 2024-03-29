import click
@click.group()
@click.version_option()
def cli():
    """ CLI for spql """
    pass

@cli.command()
@click.argument(
    "name",
    type=str,
    required=True,
)
def hello(name):
    print(f"Hello, {name}")