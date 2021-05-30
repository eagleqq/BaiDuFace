import os

from PyQt5 import QtSql
from PyQt5.QtSql import QSqlQuery
from src.core.constants import MAIN_SQL_PATH


class AdminSql:
    # 管理员信息表操作
    @staticmethod
    def sql_init():
        database = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        database.setDatabaseName(MAIN_SQL_PATH)
        database.open()

    @staticmethod
    def creat_table():
        query = QSqlQuery()
        query.prepare('create table admin (id int primary key, name text, password text,'
                      ' className text, saveName blob, savePassword blob)')
        if not query.exec_():
            query.lastError()
        else:
            print('create a table')

    @staticmethod
    def insert(id, name, password, className):
        query = QSqlQuery()
        insert_sql = 'insert into admin values (?,?,?,?,?,?)'
        query.prepare(insert_sql)
        query.addBindValue(id)
        query.addBindValue(name)
        query.addBindValue(password)
        query.addBindValue(className)
        query.addBindValue(False)
        query.addBindValue(False)
        if not query.exec_():
            return False
        else:
            return True

    @staticmethod
    def select_all():
        query = QSqlQuery()
        query.prepare('select id,name,password from admin')
        if not query.exec_():
            query.lastError()
        else:
            while query.next():
                id = query.value(0)
                name = query.value(1)
                password = query.value(2)
                print(id, name, password)

    @staticmethod
    def select_by_id(id):
        query = QSqlQuery()
        query.prepare('select id,name,password,className,saveName,savePassword from admin where id == {}'.format(id))
        if not query.exec_():
            query.lastError()
            return None
        else:
            while query.next():
                id = query.value(0)
                name = query.value(1)
                password = query.value(2)
                className = query.value(3)
                saveName = query.value(4)
                savePassword = query.value(5)
                return id, name, password, className, saveName, savePassword

    @staticmethod
    def set_saveName(saveName):
        print(saveName)
        query = QSqlQuery()
        query.prepare('UPDATE admin SET saveName = {} WHERE id = 0'.format(saveName))
        if not query.exec_():
            err = query.lastError()
            print(err.text())
            return False
        else:
            return True

    @staticmethod
    def set_savePassword(savePassword):
        query = QSqlQuery()
        query.prepare('UPDATE admin SET savePassword = {} WHERE id = 0'.format(savePassword))
        if not query.exec_():
            query.lastError()
            return False
        else:
            return True

    @staticmethod
    def update(name, password, className):
        query = QSqlQuery()
        query.prepare('UPDATE admin SET name = "{}",password = "{}",className = "{}"  WHERE id = 0'.format(name, password, className))
        if not query.exec_():
            query.lastError()
            return False
        else:
            return True

if __name__ == '__main__':
    AdminSql.sql_init()
    AdminSql.creat_table()