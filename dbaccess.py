# -*- cording:utf-8 -*-

import psycopg2


def postquery(text):
    connection = psycopg2.connect("host=localhost dbname=messages user=postgres password=branbran")
    cursor = connection.cursor()
    cursor.execute("select * from sample where tag1 LIKE '%%%s%%' or tag2 LIKE '%%%s%%' or tag3 LIKE '%%%s%%'" % (text, text, text))
    res = cursor.fetchall()

    if len(res) == 0:
        cursor.execute("select * from sample where id='ng001'")
        res = cursor.fetchall()

    cursor.close()
    connection.close()

    return res
