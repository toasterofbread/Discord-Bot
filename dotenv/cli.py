import os
import sys
from subprocess import Popen
from typing import Any, Dict, List  # noqa

try:
    import click
except ImportError:
    sys.stderr.write('It seems python-dotenv is not installed with cli option. \n'
                     'Run pip install "python-dotenv[cli]" to fix this.')
    sys.exit(1)

from .main import dotenv_values, get_key, set_key, unset_key
from .version import __version__


@click.group()
@click.option('-f', '--file', default=os.path.join(os.getcwd(), 'database.py'),
              type=click.Path(exists=True),
              help="Location of the database.py file, defaults to database.py file in current working directory.")
@click.option('-q', '--quote', default='always',
              type=click.Choice(['always', 'never', 'auto']),
              help="Whether to quote or not the variable values. Default mode is always. This does not affect parsing.")
@click.version_option(version=__version__)
@click.pass_context
def cli(ctx, file, quote):
    # type: (click.Context, Any, Any) -> None
    '''This script is used to set, get or unset values from a database.py file.'''
    ctx.obj = {}
    ctx.obj['FILE'] = file
    ctx.obj['QUOTE'] = quote


@cli.command()
@click.pass_context
def list(ctx):
    # type: (click.Context) -> None
    '''Display all the stored key/value.'''
    file = ctx.obj['FILE']
    dotenv_as_dict = dotenv_values(file)
    for k, v in dotenv_as_dict.items():
        click.echo('%s=%s' % (k, v))


@cli.command()
@click.pass_context
@click.argument('key', required=True)
@click.argument('value', required=True)
def set(ctx, key, value):
    # type: (click.Context, Any, Any) -> None
    '''Store the given key/value.'''
    file = ctx.obj['FILE']
    quote = ctx.obj['QUOTE']
    success, key, value = set_key(file, key, value, quote)
    if success:
        click.echo('%s=%s' % (key, value))
    else:
        exit(1)


@cli.command()
@click.pass_context
@click.argument('key', required=True)
def get(ctx, key):
    # type: (click.Context, Any) -> None
    '''Retrieve the value for the given key.'''
    file = ctx.obj['FILE']
    stored_value = get_key(file, key)
    if stored_value:
        click.echo('%s=%s' % (key, stored_value))
    else:
        exit(1)


@cli.command()
@click.pass_context
@click.argument('key', required=True)
def unset(ctx, key):
    # type: (click.Context, Any) -> None
    '''Removes the given key.'''
    file = ctx.obj['FILE']
    quote = ctx.obj['QUOTE']
    success, key = unset_key(file, key, quote)
    if success:
        click.echo("Successfully removed %s" % key)
    else:
        exit(1)


@cli.command(context_settings={'ignore_unknown_options': True})
@click.pass_context
@click.argument('commandline', nargs=-1, type=click.UNPROCESSED)
def run(ctx, commandline):
    # type: (click.Context, List[str]) -> None
    """Run command with environment variables present."""
    file = ctx.obj['FILE']
    dotenv_as_dict = dotenv_values(file)
    if not commandline:
        click.echo('No command given.')
        exit(1)
    ret = run_command(commandline, dotenv_as_dict)  # type: ignore
    exit(ret)


def run_command(command, env):
    # type: (List[str], Dict[str, str]) -> int
    """Run command in sub process.

    Runs the command in a sub process with the variables from `env`
    added in the current environment variables.

    Parameters
    ----------
    command: List[str]
        The command and it's parameters
    env: Dict
        The additional environment variables

    Returns
    -------
    int
        The return code of the command

    """
    # copy the current environment variables and add the vales from
    # `env`
    cmd_env = os.environ.copy()
    cmd_env.update(env)

    p = Popen(command,
              universal_newlines=True,
              bufsize=0,
              shell=False,
              env=cmd_env)
    _, _ = p.communicate()

    return p.returncode


if __name__ == "__main__":
    cli()
