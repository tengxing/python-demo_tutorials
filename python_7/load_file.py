#encoding=utf-8
import pickle as p#记得导入pickle,用它来加载数据
import os
import tensorflow as tf


filename = os.path.join("data","contact")#我把数据文本放在项目下的data文件夹下
X = None
Y = None
with open(filename, 'rb')as f:
    #从字典结构的数据文本加载数据，加载出来的数据保留了字典结构
    datadict = p.load(f)
    #获得所有的图像数据，是个6000*3*32*32的一维数组
    X = datadict['data']
    #获得所有图像的label，是个6000大小的一维数组
    Y = datadict['labels']
    print ("data数据X数组的大小:", X.shape)
    #将6000*3*32*32一维数组转换为(6000,3*32*32)的二维数组
    X = X.reshape(6000, -1)
#将X加入tf队列
valuequeue = tf.train.input_producer(X,shuffle=False)
valuelabel = tf.train.input_producer(Y,shuffle=False)
#每次出队一个
value = valuequeue.dequeue()
label = valuelabel.dequeue()
#label是字符串类型的，需要转成tf.int32类型
result.label = tf.string_to_number(label,tf.int32)
#Convert from [depth, height, width] to [height, width, depth].
#value存入的时候就是数组，所以取出来就是数组，没必要像label从字符串转，现在reshape3*32*32的三维矩阵
image = tf.reshape(value,[result.depth, result.height, result.width])
result.uint8image = tf.transpose(image, [1, 2, 0])

