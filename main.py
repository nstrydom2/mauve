#! /usr/bin/env /Users/nstrydom/PycharmProjects/mauve/.venv/bin/python
import os
import argparse

from pathlib import Path
from zipfile import ZipFile


def rename_files(path: Path):
    band_album = path.name.split(' - ')

    for idx, file in enumerate(path.glob('*.m4a')):
        fname = str(file.name).replace(' - '.join(band_album) + ' -', '').lstrip()
        os.rename(path / file.name, path / fname)


def unzip_files(path: Path, cleanup=False):
    for file in path.glob('*.zip'):
        with ZipFile(file, 'r') as zf:
            zf.extractall(path)
            if cleanup:
                os.remove(file)


if __name__ == '__main__':
    argparse = argparse.ArgumentParser()
    argparse.add_argument('-d', '--directory', type=str,
                          help='Target directory to extract and process files', required=True)
    argparse.add_argument('-c', '--cleanup', action='store_true',
                          help='Cleanup original zip file when complete', required=False, default=False)
    args = argparse.parse_args()

    # process files
    dir_path = Path(args.directory)
    unzip_files(dir_path, args.cleanup)

    for album in dir_path.glob('*'):
        rename_files(album)
