#!/usr/bin/env python3
"""
THIS IS FOR GENERATING A HEADER FILE
IN C LANGUAGE
"""
import os


# name of file containing copied text from intranet
# generate this page manually with ctrl/command 'a', 'c', 'v')
intrapage = 'intrapage.txt'


def app():
    """
    Runs main programs
    """
    intrapage_list = initialize()
    prototypes = parsefile(intrapage_list)
    writeyourfile(prototypes)
    print('*******************', '** SWEET SUCCESS **', '*******************',
          sep='\n')


def initialize():
    """
    initializes intranet page as python object
    due to authentication steps, this step simply
    parses a file that was generated through copy and paste
    """
    with open(intrapage, mode='r', encoding='utf-8') as fout:
        intrapage_list = fout.readlines()
    return intrapage_list


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


if __name__ == '__main__':
    """
    RUNS THE MAIN APP
    """
    app()
