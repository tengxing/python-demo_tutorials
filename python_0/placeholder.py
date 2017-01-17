#encoding=utf-8
import tensorflow as tf

##定义占位符
a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)

init = tf.global_variables()

with tf.Session() as sess:
    sess.run(init)
    mul = tf.mul(a,b)
    print sess.run(mul,feed_dict={a:2.,b:2.})