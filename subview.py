#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
import os
import sys

REPLACE = True
ASK_DIR = True
EXTENTIONS = ["png", "jpg", "jpeg"]
SQL_FILE_NAME = "~/Documents/CELSYS/CLIPStudioPaintVer1_5_0/SubView/default.psv"
SOURCE_FOLDER_PATH = "~/Desktop/tmp"

imageFiles = []


def hearingDialog():
    def wrap():
        return folderDialog

    def folderDialog(message='Please select a directory'):
        import tkinter, tkinter.filedialog
        import os

        dirname = tkinter.filedialog.askdirectory(parent=commiter,initialdir="~/Desktop",title=message)
        if len(dirname) > 0:
            imageFiles.extend(getFiles(dirname))
        return

    def commitwrap():
        def commit():
            files = imageFiles
            if REPLACE:
                clearSubview()
            else:
                exists = getExists()
                files = [f for f in files if not f in exists]
            insertFiles(files)
            sys.exit()
        return commit

    from tkinter import Tk, Button
    imageFiles = []

    commiter = Tk()
    button1 = Button(commiter, text='commit', command=commitwrap())
    button1.pack()
    button2 = Button(commiter, text='append', command=wrap())
    button2.pack()
    button3 = Button(commiter, text='exit', command=lambda: sys.exit(1))
    button3.pack()

    commiter.mainloop()
    return


def storeDb(file_name, sql, data):
    '''store data to db
'''
    conn = sqlite3.connect(file_name)
    conn.text_factory = str
    cur = conn.cursor()
    cur.execute(sql, data)
    conn.commit()
    conn.close()
    return


def readDb(file_name, table_name):
    '''read data from table
'''
    conn = sqlite3.connect(file_name)
    sql = "select * from TABLENAME"
    sql = sql.replace("TABLENAME", table_name)
    c = conn.execute(sql)
    ary = c.fetchall()
    conn.close()
    return ary


def clearDb(file_name, table_name):
    '''truncate table in db
'''
    file_name = os.path.expanduser(SQL_FILE_NAME)
    conn = sqlite3.connect(file_name)
    sql = "delete from TABLENAME"
    sql = sql.replace("TABLENAME", table_name)
    c = conn.execute(sql)
    conn.commit()
    conn.close()
    return


def getFiles(path=SOURCE_FOLDER_PATH):
    '''get files list in directory
'''
    import glob
    filepath = os.path.expanduser(path)
    files = []
    for ext in EXTENTIONS:
        files.extend(glob.glob(filepath + "/*." + ext))
    return files


def getExists():
    '''get files list in table
'''
    sql_file = os.path.expanduser(SQL_FILE_NAME)

    ary = readDb(sql_file, "subviewimagecategory")
    ary = [f[1].encode('utf_8') for f in ary]    
    print(ary)
    return ary


def clearSubview():
    '''clear data in table
'''
    sql_file = os.path.expanduser(SQL_FILE_NAME)
    clearDb(sql_file, "subviewimagecategory")
    print("subview cleared")
    return
    

def insertFiles(ary=[]):
    '''store files to table
'''
    sql_file = os.path.expanduser(SQL_FILE_NAME)

    for filepath in ary:
        print(filepath)
        data = (filepath, 80, 1, 1)
        sql = """INSERT INTO subviewimagecategory (subviewfilepath, subviewscale, subviewpositionx, subviewpositiony) VALUES(?,?,?,?);"""
        storeDb(sql_file, sql, data)


if __name__ == '__main__':
    hearingDialog()
