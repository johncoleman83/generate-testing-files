#!/usr/bin/env python3
"""
THIS IS FOR PARSING DATA FROM RAW STRINGS
"""

# extracts filename from line from file
def extract_file_name(aline, MAIN):
    """
    gets file name
    """
    s = aline.index(MAIN)
    i = s
    while aline[i] != ' ':
        i -= 1
    i += 1
    filename = aline[i:s] + MAIN
    return filename
