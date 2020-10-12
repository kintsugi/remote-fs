import click
from shell import Shell

from .remote_filesystem import RemoteFilesystem


class SSHFS(RemoteFilesystem):
    def __init__(
        self,
        hostname,
        mount_point,
        **remote_fs_args,
    ):
        super(SSHFS, self).__init__(hostname, mount_point, **remote_fs_args)

    def parse_remote(self, remote_str: str):
        if "@" in remote_str:
            self.user, self.hostname = remote_str.split("@")
        else:
            self.hostname = remote_str

        if ":" in self.hostname:
            self.hostname, self.dir, *rest = self.hostname.split(":")

            if len(rest):
                dirlist = [self.dir]
                dirlist = dirlist + rest
                self.dir = ":".join(dirlist)

    def format_cmd(self):
        sshfs_cmd = "sshfs"
        if self.user:
            sshfs_cmd = f"{sshfs_cmd} {self.user}@"

        if not self.hostname:
            raise ValueError("host must not be None")
        sshfs_cmd = f"{sshfs_cmd}{self.hostname}:"

        if self.dir:
            sshfs_cmd = f'{sshfs_cmd}"{self.dir}"'

        if not self.mount_point:
            raise ValueError("mount_point must not be None")

        sshfs_cmd = f"{sshfs_cmd} {self.mount_point}"
        return sshfs_cmd

    def mount(self):
        mount_cmd = self.format_cmd()
        sh = Shell()
        sh.run(mount_cmd)
