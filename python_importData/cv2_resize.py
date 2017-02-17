#coding=UTF-8
import cv2
import os

#创建文件夹
def mabey(new_dir):
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)

#裁剪图片（cv2）
def resize(dir,size,out_dir):
    image_list = []
    for root, dirs, files in os.walk(dir):
        for name in files:
            ext = os.path.splitext(name)[1][1:]
            if (ext.lower() == 'jpg'):
                path = root + os.sep + name
                image_list.append(path)
                img = cv2.imread(path)
                if img is None:
                    print("image read fail")
                    continue
                height, weight, channel = img.shape
                if height < 200 or weight < 200 or channel != 3:
                    continue
                # 你也可以转为灰度图片(channel=1)，加快训练速度
                # 把图片缩放为64x64
                img = cv2.resize(img, (size, size))
                new_file = os.path.join(out_dir, path)
                print new_file
                cv2.imwrite(new_file, img)
    return image_list
images = resize("test",50,"new")