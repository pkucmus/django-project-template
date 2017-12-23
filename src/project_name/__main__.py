import os

import click


@click.group()
def cli():
    pass


@cli.command(
    add_help_option=False, context_settings=dict(ignore_unknown_options=True, )
)
@click.argument('management_args', nargs=-1, type=click.UNPROCESSED)
@click.pass_context
def django(ctx, management_args):
    os.environ.setdefault(
        'DJANGO_SETTINGS_MODULE',
        '{{ project_name }}.service.settings.common'
    )
    from django.core.management import execute_from_command_line
    execute_from_command_line(argv=[ctx.command_path] + list(management_args))


@cli.command(
    add_help_option=False, context_settings=dict(ignore_unknown_options=True, )
)
@click.argument('management_args', nargs=-1, type=click.UNPROCESSED)
@click.pass_context
def manage(ctx, management_args):
    ctx.forward(django)
