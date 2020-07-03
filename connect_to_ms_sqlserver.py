# -*- coding: utf-8 -*-
import os
import pyodbc
server = os.environ.get("SQLSERVER-HOST")
database = 'dns'
username = 'dns'
password = os.environ.get("SQLSERVER-PASSWORD")
driver= '{ODBC Driver 13 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
cursor.execute("SELECT TOP 20 * form record")
row = cursor.fetchone()
while row:
    print str(row[0]) + " " + str(row[1])
    row = cursor.fetchone()