# -*- coding: utf-8 -*-
# @Time    : 2022/7/31 21:16
# @Author  : xiaosong
# @File    : generateGraphValidateCode.py
# @Software: PyCharm
import os
import random
# from vueExercise.settings import digit, letter
import time

from PIL import Image, ImageDraw, ImageFont, ImageFilter

from vueExercise.settings import MEDIA_ROOT

# 字母
_letter_cases = "abcdefghijklmnopqrstuvwxyz"
_upper_cases = _letter_cases.upper()
# 数字
_numbers = ''.join(map(str, range(3, 10)))
init_chars = ''.join((_letter_cases, _upper_cases, _numbers))


# 生成
def geneGraphValidateCode():
    # 图片参数
    size = (90, 38)
    candidateCharList = init_chars
    # candidateList = digit + letter
    img_type = 'JPG'
    mode = 'RGB'
    bg_color = (255, 255, 255)
    fg_color = (0, 0, 255)
    font_size = 18
    font_type = "Monaco.ttf"
    length = 4
    draw_lines = True
    n_line = (1, 2)
    draw_points = True
    point_chance = 2
    """
    @todo: 生成验证码图片,返回验证码字符串、PIL图片、图片名字
    @param size: 图片的大小，格式（宽，高），默认为(120, 30)
    @param candidateCharList: 允许的字符集合，格式字符串
    @param img_type: 图片保存的格式，默认为GIF，可选的为GIF，JPEG，TIFF，PNG
    @param mode: 图片模式，默认为RGB
    @param bg_color: 背景颜色，默认为白色
    @param fg_color: 前景色，验证码字符颜色，默认为蓝色#0000FF
    @param font_size: 验证码字体大小
    @param font_type: 验证码字体，默认为 ae_AlArabiya.ttf
    @param length: 验证码字符个数
    @param draw_lines: 是否划干扰线
    @param n_lines: 干扰线的条数范围，格式元组，默认为(1, 2)，只有draw_lines为True时有效
    @param draw_points: 是否画干扰点
    @param point_chance: 干扰点出现的概率，大小范围[0, 100]
    @return: [0]: PIL Image实例
    @return: [1]: 返回验证码字符串、PIL图片、图片名字
    """

    width, height = size
    # 创建图像
    verifyCodeImg = Image.new(mode, size, bg_color)
    # 创建可用于绘制给定图像的对象。
    # 对verifyCodeImg进行绘制
    draw = ImageDraw.Draw(verifyCodeImg)

    def get_chars():
        """生成指定长度的字符串，返回列表格式"""
        return random.sample(candidateCharList, length)

    def create_line():
        # 绘制干扰线条
        line_num = random.randint(*n_line)
        for i in range(line_num):
            # 起始点
            begin = (random.randint(0, size[0]), random.randint(0, size[1]))
            # 结束点
            end = (random.randint(0, size[0]), random.randint(0, size[1]))
            draw.line([begin, end], fill=(0, 0, 0))

    def create_points():
        """绘制干扰点"""
        # 大小限制在[0, 100]
        chance = min(100, max(0, int(point_chance)))
        for w in range(width):
            for h in range(height):
                tmp = random.randint(0, 100)
                if tmp > 100 - chance:
                    draw.point((w, h), fill=(0, 0, 0))

    def create_strs():
        """绘制验证码字符"""
        c_chars = get_chars()
        # 每个字符前后以空格隔开
        strs = ' %s ' % ' '.join(c_chars)
        # 使用字体
        # font = ImageFont.load()
        font = ImageFont.truetype("arial.ttf", font_size)
        font_width, font_height = font.getsize(strs)
        draw.text(((width - font_width) / 3, (height - font_height) / 3), strs, font=font, fill=fg_color)
        # 显示图片
        # ImageShow.show(verifyCodeImg)
        # 返回验证码的字符
        return ''.join(c_chars)

    # 实现步骤
    if draw_lines:
        create_line()
    if draw_points:
        create_points()

    verifyCodeStrs = create_strs()
    # print(verifyCodeStrs)
    # 图形扭曲参数
    params = [1 - float(random.randint(1, 2)) / 100,  # 0.99-0.98
              0,
              0,
              0,
              1 - float(random.randint(1, 10)) / 100,
              float(random.randint(1, 2)) / 500,
              0.001,
              float(random.randint(1, 2)) / 500
              ]
    # 创建扭曲
    verifyCodeImg = verifyCodeImg.transform(size, Image.Transform.PERSPECTIVE, params)
    # 滤镜，边界加强（阈值更大）
    verifyCodeImg = verifyCodeImg.filter(ImageFilter.EDGE_ENHANCE)
    # ImageShow.show(verifyCodeImg)
    verifyCodeImgName = str(time.time()).replace('.', '') + '.jpeg'
    verifyCodeImgPath = os.path.join(MEDIA_ROOT, verifyCodeImgName)
    verifyCodeImg.save(verifyCodeImgPath)
    return verifyCodeImgPath, verifyCodeStrs, verifyCodeImgName


if __name__ == "__main__":
    imgPath, codeStrs, name = geneGraphValidateCode()
    # print(img)
    # print(strs)
    print(str(time.time()).replace('.', ''))
