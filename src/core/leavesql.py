import os

from PyQt5 import QtSql
from PyQt5.QtSql import QSqlQuery
from src.core.constants import MAIN_SQL_PATH


class LeaveSql:

    @staticmethod
    def sql_init():
        database = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        database.setDatabaseName(MAIN_SQL_PATH)
        database.open()

    @staticmethod
    def creat_table():
        query = QSqlQuery()
        query.prepare('create table leave (ClassId text, name text, startTime blob,'
                      ' endTime blob, agree blob)')
        if not query.exec_():
            query.lastError()
        else:
            print('create a table')

    @staticmethod
    def delete_table():
        query = QSqlQuery()
        query.prepare('DELETE FROM leave')
        if not query.exec_():
            query.lastError()
        else:
            print('delete a table')

    @staticmethod
    def insert(classId, name, startTime, endTime, agree):
        query = QSqlQuery()
        insert_sql = 'insert into leave values (?,?,?,?,?)'
        query.prepare(insert_sql)
        query.addBindValue(classId)
        query.addBindValue(name)
        query.addBindValue(startTime)
        query.addBindValue(endTime)
        query.addBindValue(agree)
        if not query.exec_():
            print(query.lastError().text())
            return False
        else:
            return True

    @staticmethod
    def select_all():
        list = []
        query = QSqlQuery()
        query.prepare('select classId,name,startTime,endTime,agree from leave')
        if not query.exec_():
            query.lastError()
        else:
            while query.next():
                classId = query.value(0)
                name = query.value(1)
                startTime = query.value(2)
                endTime = query.value(3)
                agree = query.value(4)
                list.append((classId, name, startTime, endTime, agree))
            return list

    @staticmethod
    def select_by_id(classId):
        result = []
        query = QSqlQuery()
        query.prepare('select classId,name,startTime,endTime,agree from leave where classId == {}'.format(classId))
        if not query.exec_():
            query.lastError()
            return None
        else:
            while query.next():
                classId = query.value(0)
                name = query.value(1)
                startTime = query.value(2)
                endTime = query.value(3)
                agree = query.value(4)
                result.append((classId, name, startTime, endTime, agree))
            return result

    @staticmethod
    def update_agree_by_id_startTime(id, startTime, agree):
        query = QSqlQuery()
        query.prepare('UPDATE leave SET agree = {} where classId == {} and startTime == "{}"'.format(agree, id, startTime))
        if not query.exec_():
            query.lastError()
            return False
        else:
            return True