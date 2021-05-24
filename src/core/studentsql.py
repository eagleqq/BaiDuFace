import os

from PyQt5 import QtSql
from PyQt5.QtSql import QSqlQuery


class StudentSql:

    @staticmethod
    def sql_init():
        database = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        database.setDatabaseName('data/config/data.db')
        database.open()

    @staticmethod
    def creat_table():
        query = QSqlQuery()
        query.prepare('create table student (studentId int primary key, name text,'
                      ' uploadFace blob)')
        if not query.exec_():
            query.lastError()
        else:
            print('create a table')

    @staticmethod
    def insert(studentId, name, uploadFace):
        query = QSqlQuery()
        insert_sql = 'insert into student values (?,?,?)'
        query.prepare(insert_sql)
        query.addBindValue(studentId)
        query.addBindValue(name)
        query.addBindValue(uploadFace)
        if not query.exec_():
            return False
        else:
            return True

    @staticmethod
    def select_all():
        student_list = []
        query = QSqlQuery()
        query.prepare('select studentId,name,uploadFace from student')
        if not query.exec_():
            query.lastError()
        else:
            while query.next():
                studentId = query.value(0)
                name = query.value(1)
                uploadFace = query.value(2)
                student_list.append((studentId, name, uploadFace))
            return student_list

    @staticmethod
    def select_by_id(id):
        query = QSqlQuery()
        query.prepare('select studentId,name,uploadFace from student where studentId == {}'.format(id))
        if not query.exec_():
            query.lastError()
            return None
        else:
            while query.next():
                studentId = query.value(0)
                name = query.value(1)
                uploadFace = query.value(2)
                return studentId, name, uploadFace

    @staticmethod
    def update_uploadFace_by_id(id, uploadFace):
        query = QSqlQuery()
        query.prepare('UPDATE student SET uploadFace = {} where studentId == {}'.format(uploadFace, id))
        if not query.exec_():
            query.lastError()
            return False
        else:
            return True
