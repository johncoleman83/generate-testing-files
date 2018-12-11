#!/usr/bin/env python3
"""
THIS IS FOR GENERATING C LANGUAGE FILES
INCLUDING MAIN.C FILES AND OTHER FILES THAT
INCLUDE A PROTOTYPE
"""
import os
from shared.read_file import read_intranet_page
from shared.output_messages import print_success


# string to find a match to begin writing file and file extension
ALPHA = 'alex@/tmp/binary_trees$'
# ALPHA is beginning and end of writing for main file

# other variables to find the text from the main file
C = '$ cat'
M = 'main.c'


# first line to write to your files
firstline = '#include "binary_trees.h"\n/**\n *\n */\n'


def extractname(aline):
    """
    gets file name
    """
    s = aline.index(M)
    i = s
    while aline[i] != ' ':
        i -= 1
    i += 1
    filename = aline[i:s] + M
    return filename


def writeyourfile(line, prototype):
    """
    writes the file expected for each task
    """
    global firstline
    s1 = e1 = s2 = 0
    for i in range(len(line)):
        if line[i] == ':':
            s1 = i + 2
        if line[i] == ',':
            e1 = i
            s2 = i + 2
            break
        if line[i] == '\n':
            e1 = i
    f1 = line[s1:e1]
    with open(f1, mode='w', encoding='utf-8') as fout:
        writeline = firstline + prototype
        fout.write(writeline)
    if s2:
        f2 = line[s2:-1]
        with open(f2, mode='w', encoding='utf-8') as fout:
            writeline = '\n'
            fout.write(writeline)


def parsefile(intrapage_list):
    """
    parses intranet page, writes main files, and calls the function
    to write each file for each task
    """
    l = 0
    while l < len(intrapage_list):
        line = intrapage_list[l]
        if 'Prototype:' in line:
            prototype = line[11:]
        if ALPHA in line and C in line and M in line:
            f = extractname(line)
            with open(f, mode='w', encoding='utf-8') as fout:
                l += 1
                while ALPHA not in intrapage_list[l]:
                    line = intrapage_list[l]
                    fout.write(line)
                    l += 1
        elif 'File:' in line:
            writeyourfile(line, prototype)
            prototype = ''
        l += 1


def app():
    """
    Runs main programs
    """
    intrapage_list = read_intranet_page()
    parsefile(intrapage_list)
    print_success()

if __name__ == '__main__':
    """
    RUNS THE MAIN APP
    """
    app()
