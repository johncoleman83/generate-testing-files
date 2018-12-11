#!/usr/bin/env python3
"""
THIS IS FOR GENERATING A HEADER FILE
IN C LANGUAGE
"""
import os
from shared.read_file import read_intranet_page
from shared.output_messages import print_success


def writeyourfile(prototypes):
    """
    writes the file expected for each task
    """
    f1 = 'header.h'
    with open(f1, mode='w', encoding='utf-8') as fout:
        for prototype in prototypes:
            writeline = prototype
            fout.write(writeline)


def parsefile(intrapage_list):
    """
    parses intranet page, writes main files, and calls the function
    to write each file for each task
    """
    l = 0
    prototypes = []
    while l < len(intrapage_list):
        line = intrapage_list[l]
        if 'Prototype:' in line:
            prototypes.append(line[11:])
        l += 1
    return prototypes


def app():
    """
    Runs main programs
    """
    intrapage_list = read_intranet_page()
    prototypes = parsefile(intrapage_list)
    writeyourfile(prototypes)
    print_success()


if __name__ == '__main__':
    """
    RUNS THE MAIN APP
    """
    app()
