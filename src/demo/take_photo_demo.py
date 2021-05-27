import cv2

from src.core.faceinterface import FaceInterface


def capture_photo():
    """
    拍照demo
    """
    client = FaceInterface()
    capture = cv2.VideoCapture(0)
    while 1:
        ret, frame = capture.read()
        # cv.flip函数表示图像翻转，沿y轴翻转, 0: 沿x轴翻转, <0: x、y轴同时翻转
        frame = cv2.flip(frame, 1)
        rect = client.detect(frame)
        # 圈出人脸位置
        # for x, y, w, h in rect:
        #     cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.imshow('capture', frame)
        # 只有一张脸，自动拍照
        if len(rect) == 1:
            print(rect)
            x, y, w, h = rect[0]
            face = frame[y:y+h, x:x+w]
            cv2.imwrite('../../data/image/face4.png', face)
            break
    capture.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    capture_photo()
