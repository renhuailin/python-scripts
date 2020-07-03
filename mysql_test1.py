# -*- coding: utf-8 -*-

import mysql.connector

cnx = mysql.connector.connect(user='eclouduser', password='eclouduser123',
                              host='172.16.69.220',
                              database='bss_db')

cursor = cnx.cursor()
f = open('Records.csv','r')
line = f.readlines()
num = 0
s_dirct = {}
for s in line[0].split("\r"):
    #if num > 100 :
    #    break;
    s_list = s.split(',')
    s_dirct['host'] =  s_list[1]
    s_dirct['domain'] =  s_list[2]
    s_dirct['zone'] =  s_list[3]
    s_dirct['ip'] =  s_list[4]
    s_dirct['ttl'] =  s_list[5]
    s_dirct['intpreference'] =  s_list[6]
    s_dirct['mailexchanger'] =  s_list[7]
    s_dirct['txt'] =  s_list[8]
    s_dirct['domainname'] =  s_list[9]
    s_dirct['types'] =  s_list[10]
    num+=1

    add_employee = ("INSERT INTO `temp_records`"
               "( `host`, `domain`, `zone`, `ip`, `ttl`, `intpreference`, `mailexchanger`, `txt`, `domainname`, `types`)"
               "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")

    data_employee = (s_list[1],s_list[2],s_list[3],s_list[4],s_list[5],s_list[6],s_list[7],s_list[8],s_list[9],s_list[10])
    # Insert new employee
    cursor.execute(add_employee, data_employee)
    emp_no = cursor.lastrowid
    print emp_no
f.close()

cnx.commit()
cnx.close()