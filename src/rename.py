#!/usr/bin/env python
# encoding: utf-8

import glob
import argparse
import shutil
import os

def rename(src_dir, dest_dir, file_pattern):
    """Rename all files in the give directory by removing the first 10
    characters"""
    for src_file in glob.iglob(os.path.join(src_dir, file_pattern)):
        filename = os.path.basename(src_file)
        shutil.copy2(src_file, os.path.join(dest_dir, filename[11:]))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter,
                                     description='Rename files in a given directory by \nremoving the first 10 characters from their name')
    parser.add_argument('src_dir', type=str, help='source directory')
    parser.add_argument('dest_dir', type=str, help='destination directory')
    parser.add_argument('file_pattern', type=str, help='filename search pattern')

    args = parser.parse_args()

    rename(args.src_dir, args.dest_dir, args.file_pattern)
