#!/usr/bin/env python
# -*- coding: utf-8 -*-


SQL_FILE_NAME = "~/Documents/CELSYS/CLIPStudioPaintVer1_5_0/SubView/default.psv"
DST_FOLDER_PATH = "~/Desktop/tmp"
EXTENTIONS = ["png", "jpg", "jpeg"]


def storeDb(file_name, sql, data):
    import sqlite3
    '''store data to db
'''
    conn = sqlite3.connect(file_name)
    conn.text_factory = str
    cur = conn.cursor()
    cur.execute(sql, data)
    conn.commit()
    conn.close()
    return


def getFiles(path=DST_FOLDER_PATH):
    '''get files list in directory
'''
    import glob, os
    filepath = os.path.expanduser(DST_FOLDER_PATH)
    files = []
    for ext in EXTENTIONS:
        files.extend(glob.glob(filepath + "/*." + ext))
    return files


def insertFiles(ary=[]):
    '''store files to db
'''
    import sqlite3
    import os

    sql_file = os.path.expanduser(SQL_FILE_NAME)

    for filepath in ary:
        filepath = str(filepath)
        print(filepath)
        data = (filepath, 80, 1, 1)
        sql = """INSERT INTO subviewimagecategory (subviewfilepath, subviewscale, subviewpositionx, subviewpositiony) VALUES(?,?,?,?);"""
        storeDb(sql_file, sql, data)
    return

files = getFiles()
insertFiles(files)