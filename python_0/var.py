#encoding=utf-8
import tensorflow as tf

number = tf.Variable(1,name="name")
#定义一个常量
one = tf.constant(1)
#加起来
new_value = tf.add(number,one)
#更新
update = tf.assign(number,new_value)
# in`1it
'''下面两种方式都可以，推荐使用init2'''
#init1 = tf.initialize_all_variables()
init2 = tf.global_variables_initializer()

## method 1
#两种都可以
#sess = tf.Session()
#sess.run(init2)
#result = sess.run(new_value)
#print(result)
#sess.close()

# method 2
with tf.Session() as sess:
    sess.run(init2)
    result2 = sess.run(new_value)
    print(result2)

