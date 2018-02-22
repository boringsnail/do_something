# -*- coding:UTF-8 -*-
import MySQLdb
db = MySQLdb.connect(host ='localhost',user = 'root',passwd ='1234' ,db ='test')
cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

sql = """CREATE TABLE EMPLOYEE(LAST_NAME CHAR(20)，AGE IHN,SEX CHAR(1),INCOME FLOAT)"""
cursor.execute(sql)
