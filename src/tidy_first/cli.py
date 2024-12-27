import click

from tidy_first import tidyings


@click.command
def cli():
    for tidying_module in tidyings.ALL_TIDYINGS:
        click.echo(f'Running tidying "{tidying_module.__doc__}"')
        tidying_module.run()


if __name__ == "__main__":
    cli()
