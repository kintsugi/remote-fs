import abc
import json
import os
from typing import Tuple

import click

from .fs_config import FilesystemConfig


class FilesystemAbstract(abc.ABC):
    def __init__(self, config: FilesystemConfig):
        self.config = config
        self.hostname = config.hostname
        self.mount_point = config.mount_point
        self.user = config.user
        self.dir = config.dir
        self.options = config.options

        if config.remote:
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
