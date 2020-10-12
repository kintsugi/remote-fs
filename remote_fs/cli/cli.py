import click

from .ctx import CLIContext
from .. import fs


@click.group()
@click.pass_context
@click.option(
    "--smbfs",
    "filesystem",
    flag_value="smbfs",
    default=False,
    help="mounts via mount_smbfs (darwin only)",
)
@click.option(
    "--sshfs", "filesystem", flag_value="sshfs", default=True, help="mounts via sshfs"
)
def cli(ctx, filesystem):
    cli_options = {"filesystem": filesystem}
    ctx.obj = CLIContext("remote-fs", cli_options=cli_options)


@cli.command()
@click.pass_context
@click.argument("mount_point", required=True)
@click.option("--save", required=False)
@click.option(
    "--remote", required=False, help="full hostname string, e.g. user@hostname:dir"
)
@click.option("--hostname", required=False)
@click.option("--user", required=False)
@click.option("--dir", required=False)
def mount(ctx, mount_point, save, remote, hostname, **kwargs):
    cli_ctx = ctx.obj
    cli_options = cli_ctx.options
    if cli_options.filesystem == "sshfs":
        filesystem = fs.SSHFS(hostname, mount_point, **kwargs)
    else:
        raise ValueError(f"{cli_options.filesystem} is not supported")

    if remote is not None:
        filesystem.parse_remote(remote)

    if save is not None:
        filesystem.save(save, cli_ctx.app_dir)
    else:
        filesystem.mount()


@cli.command()
@click.argument("mount_point")
def unmount(mount_point):
    click.echo(mount_point)
