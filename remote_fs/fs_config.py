import errno
import json
import os

from pathvalidate import sanitize_filename


class FilesystemConfig:
    def __init__(
        self,
        filesystem="",
        mount_point="",
        remote="",
        hostname="",
        user="",
        dir="",
        option=[],
    ):
        self.filesystem = filesystem
        self.mount_point = mount_point
        self.remote = remote
        self.hostname = hostname
        self.user = user
        self.dir = dir
        # NOTE: missing s on purpose
        self.options = option

    def args(self):
        return (
            self.hostname,
            self.mount_point,
            {"user": self.user, "dir": self.dir, "options": self.options},
        )

    def save(self, name, dir):
        self.name = name
        basename = sanitize_filename(f"{name}.json")
        filename = os.path.join(dir, basename)
        os.makedirs(dir, exist_ok=True)
        json.dump(self.__dict__, open(filename, "w"))

    def load(self, name, dir):
        basename = f"{name}.json"
        filename = os.path.join(dir, basename)
        if not os.path.exists(filename):
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), filename)
        self.__dict__.update(json.load(open(filename, "r")))

    @staticmethod
    def ls(dir):
        names = []
        for file in os.listdir(dir):
            if file.endswith(".json"):
                config_filename = os.path.join(dir, file)
                config_json = json.load(open(config_filename, "r"))
                names.append(config_json["name"])
        return names
