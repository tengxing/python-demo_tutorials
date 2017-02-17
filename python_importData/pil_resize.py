#coding=UTF-8
from PIL import Image
import os

img = Image.open("test.jpg")

out = img.resize((120,120))

# 图片剪裁工具类 PIL
# 遍历指定目录下的JPG图片，返回list
# 裁剪为制定大小的图片
def walk_dir(dir,size):
    image_list = []
    for root, dirs, files in os.walk(dir):
        for name in files:
            ext = os.path.splitext(name)[1][1:]
            if (ext.lower() == 'jpg'):
                path = root + os.sep + name
                image_list.append(path)
                Image.open(path).resize((size, size)).save(path)
    return image_list

images=walk_dir("test",450)
print "已经裁剪图片数：{0}".format(len(images))





