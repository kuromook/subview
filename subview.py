#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

SQL_FILE_NAME = "~/Documents/CELSYS/CLIPStudioPaintVer1_5_0/SubView/default.psv"
DST_FOLDER_PATH = "~/Desktop/tmp"
EXTENTIONS = ["png", "jpg", "jpeg"]


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
    '''read data from db
'''
    conn = sqlite3.connect(file_name)
    sql = "select * from TABLENAME"
    sql = sql.replace("TABLENAME", table_name)
    c = conn.execute(sql)
    ary = c.fetchall()
    conn.close()
    return ary


def getFiles(path=DST_FOLDER_PATH):
    '''get files list in directory
'''
    import glob, os
    filepath = os.path.expanduser(DST_FOLDER_PATH)
    files = []
    for ext in EXTENTIONS:
        files.extend(glob.glob(filepath + "/*." + ext))
    return files


def getExists():
    import os
    sql_file = os.path.expanduser(SQL_FILE_NAME)

    ary = readDb(sql_file, "subviewimagecategory")
    ary = [f[1].encode('utf_8') for f in ary]    
    print(ary)
    return ary


def insertFiles(ary=[]):
    '''store files to db
'''
    import os

    sql_file = os.path.expanduser(SQL_FILE_NAME)

    for filepath in ary:
        #filepath = str(filepath)
        print(filepath)
        data = (filepath, 80, 1, 1)
        sql = """INSERT INTO subviewimagecategory (subviewfilepath, subviewscale, subviewpositionx, subviewpositiony) VALUES(?,?,?,?);"""
        storeDb(sql_file, sql, data)
    return


exists = getExists()
files = getFiles()
files = [f for f in files if not f in exists]
insertFiles(files)