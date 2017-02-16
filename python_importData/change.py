#coding=UTF-8
from PIL import Image
import os

img = Image.open("test.jpg")

out = img.resize((120,120))

# 遍历指定目录下的JPG图片，返回list
def walk_dir(dir):
    image_list = []
    directory_list = []
    for root, dirs, files in os.walk(dir):
        for name in files:
            ext = os.path.splitext(name)[1][1:]
            if (ext.lower() == 'jpg'):
                path = root + os.sep + name
                print root
                image_list.append(path)
                directory_list.append(root+os.sep)
               # new_path = "new"+path+os.sep
                #
                Image.open(path).resize((128,128)).save("new/"+root+name)


    return image_list

images=walk_dir("test")
print len(images)

def walk_dir_directory_dir(image_dir):
    image_list = []
    directory_list = []
    for root, dirs, files in os.walk(image_dir):
        for name in files:
            ext = os.path.splitext(name)[1][1:]
            if (ext.lower() == 'jpg'):
                path = root + os.sep + name
                image_list.append(path)
                directory_list.append(root+os.sep)
                #new_path = "new"+path+os.sep
                #
                #Image.open(path).resize((32,32)).save("new/"+root+name)


    return image_list,directory_list

def resize(input_dir,output_dir):
   images,directory =  walk_dir_directory_dir(input_dir)
   print len(images)

   for image in images:

       print "dd"
       print image
       Image.open(image).resize((32, 32)).save(output_dir+"/"+image)
resize("1","new")