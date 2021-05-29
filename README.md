# BaiDuFace
基于百度人脸识别api打卡系统，分为管理员端、用户端

## 环境安装：
	pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/ --trusted-host=mirrors.aliyun.com/pypi/simple
    如果安装失败，考虑其他国内源
## 目录说明
- data
	- image： 存放图片
	- config: 存放配置文件、数据库文件
- src
	- core：存放非界面代码，如百度人脸识别
	- gui ：
		- admiwidget： 存放后台管理界面代码
		- userwidget： 存放打卡界面代码
	- demo： 存放示例代码

- docs： 存放各种文档
- run_admi.py: 后台管理运行入口
- run_user.py: 打卡界面运行入口
