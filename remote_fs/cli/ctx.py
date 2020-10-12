import click

from .options import CLIOptions


class CLIContext:
    def __init__(self, app_name, cli_options={"filesystem": ""}):
        self.app_name = app_name
        if not self.app_name:
            raise ValueError("app_name must not be empty")
        self.app_dir = click.get_app_dir(self.app_name)
        self.options = CLIOptions(**cli_options)
