#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
import os

SQL_FILE_NAME = "~/Documents/CELSYS/CLIPStudioPaintVer1_5_0/SubView/default.psv"
DST_FOLDER_PATH = "~/Desktop/tmp"
EXTENTIONS = ["png", "jpg", "jpeg"]
REPLACE = True
ASK_DIR = True

def folderDialog():
    import tkinter, tkinter.filedialog
    import os

    root = tkinter.Tk()

    dirname = tkinter.filedialog.askdirectory(parent=root,initialdir="~/Desktop",title='Please select a directory')
    if len(dirname) > 0:
        return dirname
    else:
        import sys
        sys.exit()
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
    SQL_FILE_NAME = "~/Documents/CELSYS/CLIPStudioPaintVer1_5_0/SubView/default.psv"
    file_name = os.path.expanduser(SQL_FILE_NAME)
    conn = sqlite3.connect(file_name)
    sql = "delete from TABLENAME"
    sql = sql.replace("TABLENAME", table_name)
    c = conn.execute(sql)
    conn.commit()
    conn.close()
    return


def getFiles(path=DST_FOLDER_PATH):
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
        #filepath = str(filepath)
        print(filepath)
        data = (filepath, 80, 1, 1)
        sql = """INSERT INTO subviewimagecategory (subviewfilepath, subviewscale, subviewpositionx, subviewpositiony) VALUES(?,?,?,?);"""
        storeDb(sql_file, sql, data)
def main():
    dirname = folderDialog() if ASK_DIR else DST_FOLDER_PATH
    print(dirname)
    files = getFiles(dirname)

    if REPLACE:
        clearSubview()
    else:
        exists = getExists()
        files = [f for f in files if not f in exists]
    insertFiles(files)

if __name__ == '__main__':
    main()