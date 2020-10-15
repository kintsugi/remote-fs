
# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


import os.path

readme = ''
here = os.path.abspath(os.path.dirname(__file__))
readme_path = os.path.join(here, 'README.rst')
if os.path.exists(readme_path):
    with open(readme_path, 'rb') as stream:
        readme = stream.read().decode('utf8')


setup(
    long_description=readme,
    name='remote-fs',
    version='0.1.2',
    description='A tool to manage your remote filesystems (sshfs, mount_smbfs)',
    python_requires='==3.*,>=3.0.0',
    project_urls={"homepage": "https://github.com/kintsugi/remote-fs"},
    author='kintsu',
    author_email='k@kintsu.io',
    license='MIT',
    packages=['remote_fs', 'remote_fs.cli'],
    package_dir={"": "."},
    package_data={},
    install_requires=['click==7.*,>=7.1.2', 'pathvalidate==2.*,>=2.3.0', 'setuptools==50.*,>=50.3.0', 'shell==1.*,>=1.0.1'],
    extras_require={"dev": ["black==20.*,>=20.8.0.b1", "dephell==0.*,>=0.8.3", "neovim==0.*,>=0.3.1", "neovim-remote==2.*,>=2.4.0", "pylint==2.*,>=2.6.0", "pynvim==0.*,>=0.4.2", "rope==0.*,>=0.18.0", "twine==3.*,>=3.2.0"]},
)
