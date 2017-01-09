#encoding=utf-8
import tensorflow as tf
import numpy as np
'''
保存读取训练数据
created by tengxing on 2017.1.7
'''
##save to file
W = tf.Variable([[1,2,3],[4,5,6]],dtype=tf.float32,name="weights")
b = tf.Variable([[1,2,3]],dtype=tf.float32,name="biases")
## init
init = tf.global_variables_initializer();
##
saver = tf.train.Saver()
##session
with tf.Session() as sess:
    sess.run(init)
    save_path = saver.save(sess,"file/save_net.ckpt")
    print ("Save to path:",save_path)

##########################################
## restore from file
'''
W = tf.Variable(np.arange(6).reshape((2,3)),dtype=tf.float32,name="weights")
b = tf.Variable(np.arange(3).reshape((1,3)),dtype=tf.float32,name="biases")
#
saver = tf.train.Saver()
# init
init = tf.global_variables_initializer()
# sess
with tf.Session() as sess:
    sess.run(init)
    saver.restore(sess,"file/save_net.ckpt")
    print ("weights:",sess.run(W))
    print ("biases:",sess.run(b))
'''
