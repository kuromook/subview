#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

SOURCE_FOLDER_PATH = "~/Desktop/images"
RENAMED_FILE_NAME = "rename"


def getFiles(path=SOURCE_FOLDER_PATH):
    filepath = os.path.expanduser(path)
    files = os.listdir(filepath)
    return files


def sortWithMinus(files):
    import re
    patternM = re.compile(r'.*_-\d{2,3}\.(png|jpg|jpeg)') 
    patternP = re.compile(r'.*_\d{2,3}\.(png|jpg|jpeg)') 
    minusFiles = [f for f in files if patternM.match(f)]
    positiveFIles = [f for f in files if patternP.match(f)]
    minusFiles.reverse()
    minusFiles.extend(positiveFIles)
    return minusFiles


def renameFiles(files, path=SOURCE_FOLDER_PATH):
    filepath = os.path.expanduser(path)
    n = 1
    for f in files:
        number = "{0:04d}".format(n)
        print(str(n) + " " + f)
        n += 1
        name, ext = os.path.splitext(f)
        os.rename(filepath + "/" + f, filepath + "/" + RENAMED_FILE_NAME + number + ext)

def folderDialog(message='Please select a directory'):
    import tkinter, tkinter.filedialog
    import os

    dirname = tkinter.filedialog.askdirectory(initialdir="~/Desktop",title=message)
    if len(dirname) > 0:
        return dirname


dirname = folderDialog()
print(dirname)
files = getFiles(dirname)
files = sortWithMinus(files)
renameFiles(files,dirname)