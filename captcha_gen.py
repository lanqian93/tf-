# coding:utf-8
# description: 用于验证码的生成，生成训练集和测试集
import os
import random
import numpy as np
from PIL import Image
from captcha.image import ImageCaptcha


NUMBER = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
LOW_CASE = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
UP_CASE = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
           'V', 'W', 'X', 'Y', 'Z']

CAPTCHA_LIST = NUMBER + LOW_CASE + UP_CASE
CAPTCHA_LEN = 4
CAPTCHA_HEIGHT = 40
CAPTCHA_WIDTH = 80


def random_captcha_text(char_set=CAPTCHA_LIST, captcha_size=CAPTCHA_LEN):
    """
    随机生成定长字符串
    :param char_set: 备选字符串列表
    :param captcha_size: 字符串长度
    :return: 字符串
    """
    captcha_text = [random.choice(char_set) for _ in range(captcha_size)]
    return ''.join(captcha_text)


def gen_captcha_text_and_image(width=CAPTCHA_WIDTH, height=CAPTCHA_HEIGHT, save=None):
    """
    生成随机验证码
    :param width: 验证码图片宽度
    :param height: 验证码图片高度
    :param save: 是否保存（None）
    :return: 验证码字符串，验证码图像np数组
    """
    # image = ImageCaptcha(width=width, height=height)
    # # 验证码文本
    # captcha_text = random_captcha_text()
    # captcha = image.generate(captcha_text)
    # # 保存
    # if save:
    #     image.write(captcha_text, './img/' + captcha_text + '.jpg')
    # captcha_image = Image.open(captcha)
    # # 转化为np数组
    # captcha_image = np.array(captcha_image)
    # return captcha_text, captcha_image
    filePath = random.choice(os.listdir('./trainImage/'))
    captcha_name = filePath.split('/')[-1].strip('.jpg')
    captcha_image = Image.open('./trainImage/' + filePath)
    captcha_image = np.array(captcha_image)
    return captcha_name, captcha_image


if __name__ == '__main__':
    t, im = gen_captcha_text_and_image(save=True)
    print(t, im.shape)      # (40, 80, 3)



