# -*- coding: utf-8 -*-

import mysql.connector

cnx = mysql.connector.connect(user='mysql', password='mysql',
                              host='127.0.0.1',
                              database='pdns')

curA = cnx.cursor(buffered=True)
curB = cnx.cursor(buffered=True)


# Query to get employees who joined in a period defined by two dates
query = (
  "select * from records where `type` = 'SOA'")


update_old_soa = (
  "UPDATE records SET content = %s "
  "WHERE id = %s")

# Select the employees getting a raise
curA.execute(query)

for (id, domain_id, name, type, content, ttl, prio, change_date,disabled, ordername, auth) in curA:
    print  "id=%d content=%s" %  id, content
    content = content.replace("ns1.xiangcloud.com.cn","ns.cnwindows.com")
    print  "after id=%d content=%s" %  id, content

    curB.execute(update_old_soa,(content,id))
    #cnx.commit()

cnx.close()