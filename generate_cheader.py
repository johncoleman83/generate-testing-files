#!/usr/bin/python3
"""
THIS IS FOR GENERATING A HEADER FILE
IN C LANGUAGE
"""
import os


# name of file containing copied text from intranet
# generate this page manually with ctrl/command 'a', 'c', 'v')
intrapage = 'intrapage.txt'


# main function
def app():
    intrapage_list = initialize()
    prototypes = parsefile(intrapage_list)
    writeyourfile(prototypes)
    print('*******************', '** SWEET SUCCESS **', '*******************',
          sep='\n')


# initialize file as list
def initialize():
    with open(intrapage, mode='r', encoding='utf-8') as fout:
        intrapage_list = fout.readlines()
    return intrapage_list


def writeyourfile(prototypes):
    f1 = 'header.h'
    with open(f1, mode='w', encoding='utf-8') as fout:
        for prototype in prototypes:
            writeline = prototype
            fout.write(writeline)


# parses list of lines from file and writes to new files one at a time
def parsefile(intrapage_list):
    l = 0
    prototypes = []
    while l < len(intrapage_list):
        line = intrapage_list[l]
        if 'Prototype:' in line:
            prototypes.append(line[11:])
        l += 1
    return prototypes


if __name__ == '__main__':
    app()
