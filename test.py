import datetime

from src.core.signsql2 import Sign2Sql
# 测试代码无需关注
from src.core.util import Util

if __name__ == '__main__':
    Sign2Sql.sql_init()
    Sign2Sql.creat_table()
    clock_time_list = Sign2Sql.select_all()
    curr_time = datetime.datetime.now()
    tdate = datetime.datetime.strftime(curr_time, '%Y-%m-%d')
    ttime = datetime.datetime.strftime(curr_time, '%H:%M:%S')
    print(tdate, ttime)
    for clock_time in clock_time_list:
        if tdate in clock_time:
            print("今日打卡时间", clock_time)
