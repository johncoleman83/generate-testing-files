#!/usr/bin/env python3
"""
THIS IS FOR GENERATING JavaScript FILES
INCLUDING MAIN.JS FILES AND OTHER FILES THAT
INCLUDE A PROTOTYPE
"""
import os
from shared.read_file import read_intranet_page


# name of file containing copied text from intranet
# generate this page manually with ctrl/command 'a', 'c', 'v')
intrapage = 'intrapage.txt'

# string to find a match to begin writing file and file extension

ALPHA = 'guillaume@ubuntu:~/'

# ALPHA is beginning and end of writing for main file
C = '$ cat'
M = 'main.js'


# first line to write to your files
firstline = '#!/usr/bin/env node\n/* '


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
    if not os.path.exists(f1):
        with open(f1, mode='w', encoding='utf-8') as fout:
            writeline = firstline + f1 + ' */\n' + prototype
            fout.write(writeline)
        os.chmod(f1, 500)
    if s2:
        try:
            i = line[s2:-1].index(',')
            f2 = line[s2:i]
        except:
            f2 = line[s2:-1]
        if not not os.path.exists(f2):
            with open(f2, mode='w', encoding='utf-8') as fout:
                writeline = '\n'
                fout.write(writeline)


def parsefile(intrapage_list):
    """
    parses intranet page, writes main files, and calls the function
    to write each file for each task
    """
    l = 0
    prototype = ''
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
            os.chmod(f, 500)
        elif 'File:' in line:
            writeyourfile(line, prototype)
        l += 1


def app():
    """
    Runs main programs
    """
    intrapage_list = read_intranet_page()
    parsefile(intrapage_list)
    print('*******************', '** SWEET SUCCESS **', '*******************',
          sep='\n')


if __name__ == '__main__':
    """
    RUNS THE MAIN APP
    """
    app()
