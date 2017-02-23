#coding=utf-8
from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf

mnist = input_data.read_data_sets("Mnist_data/", one_hot=True)

def loadGraph():
