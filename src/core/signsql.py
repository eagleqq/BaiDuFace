import os

from PyQt5 import QtSql
from PyQt5.QtSql import QSqlQuery
from src.core.constants import MAIN_SQL_PATH


class SignSql:
    # 打卡记录数据库表操作
    @staticmethod
    def sql_init():
        database = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        database.setDatabaseName(MAIN_SQL_PATH)
        database.open()

    @staticmethod
    def creat_table():
        query = QSqlQuery()
        query.prepare('create table sign (ClassId text, name text, signTime text,'
                      ' signOK blob)')
        if not query.exec_():
            query.lastError()
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
        list = []
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
                list.append((classId, name, signTime, signOK))
            return list

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

    @staticmethod
    def select_by_time(time):
        result = []
        query = QSqlQuery()
        query.prepare('select classId,name,signTime,signOK from sign')
        if not query.exec_():
            query.lastError()
            return None
        else:
            while query.next():
                classId = query.value(0)
                name = query.value(1)
                signTime = query.value(2)
                signOK = query.value(3)
                if signTime.startswith(time):
                    result.append((classId, name, signTime, signOK))
            return result
