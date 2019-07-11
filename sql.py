import pymysql
import time


#триггер
def connect_sql():
    connection = pymysql.connect('0.0.0.0', 'user', 'password', 'db')

    try:
        with connection.cursor() as cursor:
            sql_query = "SELECT * FROM `stats`;"
            cursor.execute(sql_query)
            
            data = cursor.fetchone()
    
    finally:
        connection.close()

    return data

def update_sql():
    connection = pymysql.connect('0.0.0.0', 'user', 'password', 'db')

    try:
        with connection.cursor() as cursor:
            sql_update = "UPDATE `stats` SET `num`='0';"
            cursor.execute(sql_update)
            connection.commit()

    finally:
        connection.close()


#личный состав
def getListPlayers():
    connection = pymysql.connect('0.0.0.0', 'user', 'password', 'db')

    try:
        with connection.cursor() as cursor:
            sql_query = "SELECT * FROM `ls`;"
            cursor.execute(sql_query)
            data = cursor.fetchall()
    finally:
        connection.close()

    return data

def getListPropaga():
    connection = pymysql.connect('0.0.0.0', 'user', 'password', 'db')

    try:
        with connection.cursor() as cursor:
            sql_query = "SELECT `name` FROM `ls` INNER JOIN `testplayers` ON ((`ls`.`uid` = `testplayers`.`p_guid`) AND (TIMESTAMPDIFF(day,`testplayers`.`onlinetime`,now()) > 30))"
            cursor.execute(sql_query)
            data = cursor.fetchall()
    finally:
        connection.close()

    return data

def updateRow(idd,status,comment):
    connection = pymysql.connect('0.0.0.0', 'user', 'password', 'db')

    try:
        with connection.cursor() as cursor:
            sql_query = f"UPDATE `ls` SET `status`='{status}', `comment`='{comment}' WHERE `id`={int(idd)}"
            cursor.execute(sql_query)
            connection.commit()
    finally:
        connection.close()

def getListUpdate():
    connection = pymysql.connect('0.0.0.0', 'user', 'password', 'db')

    try:
        with connection.cursor() as cursor:
            sql_query = "INSERT INTO `ls` (`id`,`name`,`uid`) SELECT `testplayers`.`p_id`,`testplayers`.`p_name`,`testplayers`.`p_guid` FROM `testplayers` WHERE ((INSTR(`testplayers`.`p_name`,'[UTF]') > 0) AND (`testplayers`.`p_guid` NOT IN (SELECT `uid` FROM `ls`)))"
            cursor.execute(sql_query)
            connection.commit()
    finally:
        connection.close()



#зевсы
def getListZeus():
    connection = pymysql.connect('0.0.0.0', 'user', 'password', 'db')

    try:
        with connection.cursor() as cursor:
            sql_query = "SELECT * FROM `zeus`;"
            cursor.execute(sql_query)
            data = cursor.fetchall()
    finally:
        connection.close()

    return data

def addRowZeus(name,status,comment):
    connection = pymysql.connect('0.0.0.0', 'user', 'password', 'db')

    try:
        with connection.cursor() as cursor:
            sql_query = f"INSERT INTO `zeus` (`name`,`status`,`comment`) VALUES ('{name}','{status}','{comment}')"
            cursor.execute(sql_query)
            connection.commit()
    finally:
        connection.close()

def updateRowZeus(idd,status,comment):
    connection = pymysql.connect('0.0.0.0', 'user', 'password', 'db')

    try:
        with connection.cursor() as cursor:
            res = False
            sql_query = f"SELECT * FROM `zeus` WHERE `id`={int(idd)}"
            cursor.execute(sql_query)
            data = cursor.fetchall()
            if len(data) > 0:
                res = True
                sql_query = f"UPDATE `zeus` SET `status`='{status}', `comment`='{comment}' WHERE `id`={int(idd)}"
                cursor.execute(sql_query)
                connection.commit()
    finally:
        connection.close()

    return res

def minusScoreZeus(idd):
    connection = pymysql.connect('0.0.0.0', 'user', 'password', 'db')

    try:
        with connection.cursor() as cursor:
            kick = False
            sql_query = f"SELECT `name`,`score` FROM `zeus` WHERE `id`={int(idd)}"
            cursor.execute(sql_query)
            data = cursor.fetchone()
            if data[1] == 1:
                kick = True
            
            score = data[1] - 1
            sql_query = f"UPDATE `zeus` SET `score`={score} WHERE `id`={int(idd)}"
            cursor.execute(sql_query)
            connection.commit()
    finally:
        connection.close()

    res = [data[0],kick]
    return res



#пилоты
def pilotSpisok():
    connection = pymysql.connect('0.0.0.0', 'user', 'password', 'db')

    try:
        with connection.cursor() as cursor:
            sql_query = "SELECT `p_name`, LEFT(RIGHT(`p_dostup`,2),1) FROM `testplayers` WHERE (CAST(LEFT(RIGHT(`p_dostup`,2),1) AS UNSIGNED) > 1)"
            cursor.execute(sql_query)
            data = cursor.fetchall()
    finally:
        connection.close()

    return data

def pilot2():
    connection = pymysql.connect('0.0.0.0', 'user', 'password', 'db')

    try:
        with connection.cursor() as cursor:
            sql_query = "SELECT `p_name`, LEFT(RIGHT(`p_dostup`,2),1) FROM `testplayers` WHERE (CAST(LEFT(RIGHT(`p_dostup`,2),1) AS UNSIGNED) = 2)"
            cursor.execute(sql_query)
            data = cursor.fetchall()
    finally:
        connection.close()

    return data

def pilot3():
    connection = pymysql.connect('0.0.0.0', 'user', 'password', 'db')

    try:
        with connection.cursor() as cursor:
            sql_query = "SELECT `p_name`, LEFT(RIGHT(`p_dostup`,2),1) FROM `testplayers` WHERE (CAST(LEFT(RIGHT(`p_dostup`,2),1) AS UNSIGNED) = 3)"
            cursor.execute(sql_query)
            data = cursor.fetchall()
    finally:
        connection.close()

    return data

def pilot4():
    connection = pymysql.connect('0.0.0.0', 'user', 'password', 'db')

    try:
        with connection.cursor() as cursor:
            sql_query = "SELECT `p_name`, LEFT(RIGHT(`p_dostup`,2),1) FROM `testplayers` WHERE (CAST(LEFT(RIGHT(`p_dostup`,2),1) AS UNSIGNED) = 4)"
            cursor.execute(sql_query)
            data = cursor.fetchall()
    finally:
        connection.close()

    return data

def greenSpisok():
    connection = pymysql.connect('0.0.0.0', 'user', 'password', 'db')

    try:
        with connection.cursor() as cursor:
            sql_query = "SELECT `p_name` FROM `testplayers` WHERE (LEFT(`p_dostup`,2) = '[1')"
            cursor.execute(sql_query)
            data = cursor.fetchall()
    finally:
        connection.close()

    return data
