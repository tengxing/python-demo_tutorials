#encoding=utf-8
import tensorflow.examples.tutorials.mnist.input_data as input_data
#mnist数据
#load data
mnist = input_data.read_data_sets("Mnist_data/", one_hot=True)

print "训练数据量：",mnist.train.images.shape
print "训练标签量：",mnist.train.labels.shape
print "验证数据量：",mnist.validation.images.shape
print "验证标签量：",mnist.validation.labels.shape
print "测试数据量：",mnist.test.images.shape
print "测试标签量：",mnist.test.labels.shape
##CSV数据
import tensorflow.contrib.learn.python.learn.datasets.base as base
iris_data,iris_label = base.load_iris()
house_data,house_label = base.load_boston()
print house_data.shape,house_label.shape
print iris_data.shape,iris_label.shape
#cifar10数据
#暂时不能用
import tensorflow.models.image.cifar10.cifar10 as cifar10
cifar10.maybe_download_and_extract()
images, labels = cifar10.distorted_inputs()
print images
print labels