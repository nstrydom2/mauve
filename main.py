#! /usr/bin/env /Users/nstrydom/PycharmProjects/mauve/.venv/bin/python
import os
import argparse

from pathlib import Path
from zipfile import ZipFile


def rename_files(dir_path: Path):
    band_album = dir_path.name.split(' - ')

    for idx, file in enumerate(dir_path.glob('*.m4a')):
        fname = str(file.name).replace(' - '.join(band_album) + ' - ', '')
        os.rename(dir_path / file.name, dir_path / fname)


def unzip_files(dir_path: Path, cleanup=False):
    for file in dir_path.glob('*.zip'):
        with ZipFile(file, 'r') as zf:
            zf.extractall(dir_path)
            if cleanup:
                os.remove(file)


if __name__ == '__main__':
    argparse = argparse.ArgumentParser()
    argparse.add_argument('--directory', type=str)
    argparse.add_argument('--cleanup', action='store_true', default=False)
    args = argparse.parse_args()

    # process files
    dir_path = Path(args.directory)
    unzip_files(dir_path, args.cleanup)

    for album in dir_path.glob('*'):
        rename_files(album)
