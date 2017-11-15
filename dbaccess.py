# -*- cording:utf-8 -*-

import psycopg2


def postquery(text):
    connection = psycopg2.connect("host=localhost dbname=chatbot_api user=postgres password=branbran")
    cursor = connection.cursor()
    cursor.execute("select * from messages where tag1 LIKE '%%%s%%' or tag2 LIKE '%%%s%%' or tag3 LIKE '%%%s%%'" % (text, text, text))
    res = cursor.fetchall()

    if len(res) == 0:
        cursor.execute("select * from messages where id='ng001'")
        res = cursor.fetchall()

    cursor.close()
    connection.close()

    return res
