import configparser
from src.core.constants import STUDENT_LOGIN_INFO_PATH

class LoginData:
    # 登陆信息缓存   username + password
    def __init__(self, path=STUDENT_LOGIN_INFO_PATH):
        self.path = path
        self.config = configparser.ConfigParser()

    def setInfo(self, username, password):
        # 添加一个select
        self.config.add_section("login_info")
        print(self.config.sections())
        # 往select添加key和value
        self.config.set("login_info", "username", username)
        self.config.set("login_info", "password", password)
        self.config.write(open(self.path, 'w'))  # 删除原文件重新写入

    def getInfo(self):
        """
        获取用户名，密码
        :return:
        """
        try:
            self.config.read(self.path, encoding='utf-8')
            # 获取特定section
            items = self.config.items('login_info')  # 返回结果为元组
            print(items)
            username = items[0][1]
            password = items[1][1]
            return username, password
        except Exception as e:
            print("解析文件异常{}".format(str(e)))
            return None, None


if __name__ == '__main__':
    ld = LoginData(STUDENT_LOGIN_INFO_PATH)
    # ld.setInfo("123", "456")
    username, pwd = ld.getInfo()
    print(username, pwd)
