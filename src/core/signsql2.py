import os

from PyQt5 import QtSql
from PyQt5.QtSql import QSqlQuery
from src.core.constants import MAIN_SQL_PATH


class Sign2Sql:
    # 上课打卡时间
    @staticmethod
    def sql_init():
        database = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        database.setDatabaseName(MAIN_SQL_PATH)
        database.open()

    @staticmethod
    def creat_table():
        query = QSqlQuery()
        query.prepare('create table sign2 (id integer primary key autoincrement, time text)')
        if not query.exec_():
            query.lastError()
        else:
            print('create a table')

    @staticmethod
    def delete_table():
        query = QSqlQuery()
        query.prepare('DELETE FROM Sign2')
        if not query.exec_():
            query.lastError()
        else:
            print('delete a table')

    @staticmethod
    def insert(time):
        query = QSqlQuery()
        insert_sql = 'insert into sign2(time) values (?)'
        query.prepare(insert_sql)
        # query.addBindValue("NULL")
        query.addBindValue(time)
        if not query.exec_():
            print(query.lastError().text())
            return False
        else:
            return True

    @staticmethod
    def select_all():
        list = []
        query = QSqlQuery()
        query.prepare('select time from sign2')
        if not query.exec_():
            query.lastError()
        else:
            while query.next():
                time = query.value(0)
                print("@@" + time)
                list.append((time))
            return list
