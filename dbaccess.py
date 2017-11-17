# -*- cording:utf-8 -*-

import psycopg2


def post_query(text):
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


def ng_query(text):
    connection = psycopg2.connect("host=localhost dbname=chatbot_api user=postgres password=branbran")
    cursor = connection.cursor()
    cursor.execute("select * from messages where id='%s'" % text)  # NGの回答をひっぱる
    res = cursor.fetchall()

    cursor.close()
    connection.close()

    return res
