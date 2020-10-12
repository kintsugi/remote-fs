import abc
import click
import os


class RemoteFilesystem(abc.ABC):
    def __init__(self, hostname, mount_point, user="", dir="", options=[]):
        self.hostname = hostname
        self.mount_point = mount_point
        self.user = user
        self.dir = dir
        self.options = options

    @abc.abstractmethod
    def parse_remote(
        self,
    ):
        raise NotImplementedError

    @abc.abstractmethod
    def mount(self):
        raise NotImplementedError

    def save(self, name, dir):
        basename = f"{name}.json"
        filename = os.path.join(dir, basename)
        print(filename)
