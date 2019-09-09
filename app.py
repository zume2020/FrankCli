import click

@click.command()
@click.option('--i', help='Initialize FrankCli.')
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Hey zume, How was the Day!',
              help='About your Day.')
def hello(count, name, i):
    """A Simple Command Line Diary."""
    # click.echo(name)

if __name__ == '__main__':
    hello()