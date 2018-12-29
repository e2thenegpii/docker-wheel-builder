
import argparse
import subprocess
from .os_release import os_release_parser

from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('specfile', help='The yaml list of packages to install', type=argparse.FileType())
    parser.add_argument('pip_args', help='Additional args to add to pip commands', nargs=argparse.REMAINDER)
    args = parser.parse_args()

    package_map = {
        'alpine': 'apk',
        'debian': 'apt',
        'ubuntu': 'apt',
        'linuxmint': 'apt',
    }

    manager_map = {
        'apt': ('apt update', 'apt install -y'),
        'apk': ('apk update', 'apk add'),
    }

    release = os_release_parser()
    update, command = manager_map[package_map[release.get('id', release.get('id_like'))]]

    subprocess.run(update, shell=True, check=True)
    for python_package, system_packages in load(args.specfile, Loader=Loader).items():
        subprocess.run(' '.join([command] + system_packages), shell=True, check=True)
        subprocess.run(' '.join(['pip wheel'] + [python_package] + args.pip_args), shell=True, check=True)

main()
