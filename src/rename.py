#!/usr/bin/env python
# encoding: utf-8

import glob
import argparse
import os
import re

def rename(src_dir, dest_dir, file_pattern, search_pattern, replace):
    """Rename all files in the give directory by removing the first 10
    characters"""
    for src_file in glob.iglob(os.path.join(src_dir, file_pattern)):
        filename = os.path.basename(src_file)
        newfilename = re.sub(search_pattern, replace, filename)
        os.rename(src_file, os.path.join(dest_dir, newfilename))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter,
        description="Rename selected files in a directory using a regex to perform a\n"
                    "search/replace on the filename.\n\nFor example, to rename all JPG "
                    "files in /tmp/s, placing them into\n/tmp/d and removing the string "
                    "'iphone _' from the start of the filename:\n\n"
                    "    ./rename.py /tmp/s /tmp/d *.JPG '^iphone _' ''")
    parser.add_argument('src_dir', type=str,
        help='source directory')
    parser.add_argument('dest_dir', type=str,
        help='destination directory')
    parser.add_argument('file_pattern', type=str,
        help='filename search pattern')
    parser.add_argument('search_pattern', type=str,
        help='pattern to search for in filename')
    parser.add_argument('replace', type=str,
        help='string to replace search_pattern with')

    args = parser.parse_args()

    rename(args.src_dir, args.dest_dir, args.file_pattern,
        args.search_pattern, args.replace)
