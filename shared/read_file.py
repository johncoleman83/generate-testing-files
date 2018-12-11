#!/usr/bin/env python3
"""
THIS IS FOR READING INTRANET PAGE LIST
"""

# name of file containing copied text from intranet
# generate this page manually with ctrl/command 'a', 'c', 'v')
intrapage = 'intrapage.txt'

# reads intranet page and returns list of lines
def read_intranet_page():
    """
    initializes intranet page as python object
    due to authentication steps, this step simply
    parses a file that was generated through copy and paste
    this is used as an alternative to requests module
    with beautiful soup to avoid having to go through
    auth loops and avoid having to parse HTML tags
    """
    with open(intrapage, mode='r', encoding='utf-8') as fout:
        intrapage_list = fout.readlines()
    return intrapage_list
