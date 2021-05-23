import base64
import time
from aip import AipFace
import cv2

# 百度云密钥,请替换成自己的
APP_ID = "24227732"
API_KEY = "LRBtoX5Aw6WRfBfpun8vOkAU"
SECRET_KEY = "suXrTmiib95hQpV8YWPlfSi7QP5O7stx"
GROUP_ID = "group1"


# 人脸识别接口
class FaceInterface(object):
    def __init__(self):
        self.client = AipFace(APP_ID, API_KEY, SECRET_KEY)

    def addUser(self, user_id, face):
        """
        人脸注册
        :param user_id: 用户id
        :param face:   人脸图片
        :return:
        """
        image = self.image2base64(face)
        result = self.client.addUser(
            image=image, image_type="BASE64",
            group_id=GROUP_ID, user_id=user_id)
        print("addUser", result)
        if result['error_msg'] != 'SUCCESS':
            raise Exception(result['error_msg'])

    def updateUser(self, user_id, face):
        """
        人脸更新
        :param user_id:
        :param face:
        :return:
        """
        image = self.image2base64(face)
        result = self.client.updateUser(
            image=image, image_type="BASE64",
            group_id=GROUP_ID, user_id=user_id)
        print("updateUser", result)
        if result['error_msg'] != 'SUCCESS':
            raise Exception(result['error_msg'])

    def deleteUser(self, user_id):
        """
        删除用户
        :param user_id:
        :return:
        """
        result = self.client.deleteUser(group_id=GROUP_ID, user_id=user_id)
        print("faceDelete", result)
        if result['error_msg'] != 'SUCCESS':
            raise Exception(result['error_msg'])

    def search(self, face):
        """
        人脸查询
        :param face:
        :return:score相似度, user_id用户id
        """
        score = 0
        user_id = None
        image = self.image2base64(face)
        detect_result = self.client.detect(image, "BASE64")
        # detect()该函数会给出识别的人脸脸部的各类特征，返回值是一个字典，包含了识别的人脸中的各类特征
        # “face_probability”指的是函数判断的该图像是否为人脸特征的概率，为避免重复调用匹配接口，只有当概率大于0.8时才继续进行处理
        print("detect_result", detect_result)
        if detect_result['result']['face_list'][0]['face_probability'] > 0.8:
            # search()该函数会将图片与人脸库中的图片进行匹配，返回值是一个字典，包含了人脸的匹配结果
            # “userlist”指的是用户组中的所有预先上传过图片的用户，“score”是与该用户的匹配成度
            search_result = self.client.search(image, "BASE64", GROUP_ID)
            score = search_result['result']['user_list'][0]['score']
            user_id = search_result['result']['user_list'][0]['user_id']
        return score, user_id

    def math(self, face1, face2):
        """
        人脸比对
        :param face1: 第一张脸
        :param face2: 第二张脸
        :return: score相似度
        """
        result = self.client.match([
            {
                'image': self.image2base64(face1),
                'image_type': 'BASE64',
            },
            {
                'image': self.image2base64(face2),
                'image_type': 'BASE64',
            }
        ])
        print(result)
        if result['error_msg'] == 'SUCCESS':
            score = result['result']['score']
            return score
        else:
            return 0

    def image2base64(self, face):
        """
        图像格式转换
        :param face:
        :return:
        """
        return str(base64.b64encode(face), 'utf-8')

    def detect(self, image):
        """
        人脸检测
        :param image:
        :return:
        """
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        face_detector = cv2.CascadeClassifier("../config/haarcascade_frontalface_alt.xml")
        rect = face_detector.detectMultiScale(gray, 1.02, 5)
        return rect


if __name__ == '__main__':
    client = FaceInterface()
    face1 = open('../image/face.png', 'rb').read()
    face2 = open('../image/face2.jpg', 'rb').read()
    time_start = time.time()
    # 添加人脸
    # client.addUser("2016117250", face1)
    # 更新人脸
    # client.updateUser("2016117250", face1)
    # 查询人脸
    score, user_id = client.search(face1)
    print("相似度={}，用户ID={}".format(score, user_id))

    # client.deleteUser("2016117255")
    time_end = time.time()
    print('共计用时', time_end - time_start)
