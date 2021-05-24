import os

from PyQt5 import QtSql
from PyQt5.QtSql import QSqlQuery


class SignSql:

    @staticmethod
    def sql_init():
        database = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        database.setDatabaseName('data/config/data.db')
        database.open()

    @staticmethod
    def creat_table():
        query = QSqlQuery()
        query.prepare('create table sign (classId int, name text,'
                      ' signTime text, signOK blob')
        if not query.exec_():
            print(query.lastError().text())
            print("err")
        else:
            print('create a table')

    @staticmethod
    def insert(classId, name, signTime, signOK):
        query = QSqlQuery()
        insert_sql = 'insert into sign values (?,?,?,?)'
        query.prepare(insert_sql)
        query.addBindValue(classId)
        query.addBindValue(name)
        query.addBindValue(signTime)
        query.addBindValue(signOK)
        if not query.exec_():
            print(query.lastError().text())
            return False
        else:
            return True

    @staticmethod
    def select_all():
        query = QSqlQuery()
        query.prepare('select classId,name,signTime,signOK from sign')
        if not query.exec_():
            query.lastError()
        else:
            while query.next():
                classId = query.value(0)
                name = query.value(1)
                signTime = query.value(2)
                signOK = query.value(3)
                print(classId, name, signTime, signOK)

    @staticmethod
    def select_by_id(classId):
        result = []
        query = QSqlQuery()
        query.prepare('select classId,name,signTime,signOK from sign where classId == {}'.format(classId))
        if not query.exec_():
            query.lastError()
            return None
        else:
            while query.next():
                classId = query.value(0)
                name = query.value(1)
                signTime = query.value(2)
                signOK = query.value(3)
                result.append((classId, name, signTime, signOK))
            return result