from src.core.leavesql import LeaveSql
from src.core.signsql import SignSql
from src.core.studentsql import StudentSql


class Util:

    @staticmethod
    def get_all_num():
        StudentSql.sql_init()
        StudentSql.creat_table()
        students = StudentSql.select_all()
        if students is None:
            return 0
        return len(StudentSql.select_all())

    @staticmethod
    def get_arrive_num():
        all_num = 0
        StudentSql.sql_init()
        StudentSql.creat_table()
        students = StudentSql.select_all()
        SignSql.sql_init()
        SignSql.creat_table()
        sign_msgs = SignSql.select_all()
        for student in students:
            for sign_msg in sign_msgs:
                if student[0] != sign_msg[0]:
                    print(student[0], type(student[0]))
                    print(sign_msg[0], type(sign_msg[0]))
                if student[0] == sign_msg[0] and sign_msg[3]:
                    all_num += 1
                    break
        return all_num

    @staticmethod
    def get_leave_num():
        leave_num = 0
        leave_list = []
        LeaveSql.sql_init()
        LeaveSql.creat_table()
        results = LeaveSql.select_all()
        for result in results:
            if result[0] not in leave_list:
                leave_list.append(result[0])
                leave_num += 1
        return leave_num
