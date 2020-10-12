from remote_fs.fs.remote_filesystem import RemoteFilesystem


class MountState:
    def __init__(self, fs: RemoteFilesystem):
        self.fs = RemoteFilesystem
