import abc
import json
import os
from typing import Tuple

import click

from remote_fs.mount.settings import MountSettings


class RemoteFilesystem(abc.ABC):
    def __init__(self, settings: MountSettings):
        self.settings = settings
        self.hostname = settings.hostname
        self.mount_point = settings.mount_point
        self.user = settings.user
        self.dir = settings.dir
        self.options = settings.options

        if settings.remote:
            user, hostname, dir = self.parse_remote()

            if user:
                self.user = user
            if hostname:
                self.hostname = hostname
            if dir:
                self.dir = dir

    @abc.abstractmethod
    def parse_remote(self) -> Tuple[str, str, str]:
        raise NotImplementedError

    @abc.abstractmethod
    def validate(self) -> bool:
        raise NotImplementedError

    @abc.abstractmethod
    def mount(self):
        raise NotImplementedError
