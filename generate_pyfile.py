#!/usr/bin/env python3
"""
THIS IS FOR GENERATING PYTHON FILES
INCLUDING MAIN.PY FILES AND OTHER FILES THAT
INCLUDE A PROTOTYPE
"""
import os
from shared.read_file import read_intranet_page
from shared.output_messages import print_success
from shared.parser import extract_file_name

# string to find a match to begin writing file and file extension
ALPHA = 'alexa@ubuntu-xenial:0x00-linear_algebra$'
# ALPHA is beginning and end of writing for main file

# other variables to find the text from the main file
C = '$ cat'
MAIN = 'main.py'

# first line to write to your files
firstline = '#!/usr/bin/env python3\n"""\n'


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
            writeline = firstline + f1 + '\n"""\n' + prototype
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
        if ALPHA in line and C in line and MAIN in line:
            f = extract_file_name(line, MAIN)
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

# main function
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
