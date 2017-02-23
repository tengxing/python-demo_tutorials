#coding=utf-8
from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf

mnist = input_data.read_data_sets("Mnist_data/", one_hot=True)


print 'unload'

# 加载Graph
def loadGraph(dir):
    print()
    f = tf.gfile.FastGFile(dir,'rb')
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(f.read())
    persisted_graph =tf.import_graph_def(graph_def,name='')
    return persisted_graph

graph = loadGraph('graph/soft.ph')


with tf.Session(graph=graph) as sess:
    #sess.run(tf.initialize_all_variables())
    #sess.run(init) #加载时候不需要进行初始化
    softmax_tensor = sess.graph.get_tensor_by_name('layer/final_result:0')
    x = sess.graph.get_tensor_by_name('input/x_input:0')
    y_ = sess.graph.get_tensor_by_name('input/y_input:0')
    name = sess.graph.get_tensor_by_name('tengxing:0')
    Weights = sess.graph.get_tensor_by_name('layer/W/Weights:0')
    biases = sess.graph.get_tensor_by_name('layer/b/biases:0')

    #W = tf.Variable(tf.zeros([784, 10]), name='Weights')
    #b = tf.Variable(tf.zeros([10]), name='biases')
    tf.add_to_collection(tf.GraphKeys.VARIABLES, name)
    tf.add_to_collection(tf.GraphKeys.VARIABLES, Weights)
    tf.add_to_collection(tf.GraphKeys.VARIABLES, biases)
    try:
        saver = tf.train.Saver(tf.global_variables())  # 'Saver' misnomer! Better: Persister!
    except:
        pass
    print("load data")
    #print sess.run(name) 此时才有一个Tensor获取变量还要进行赋值
    saver.restore(sess, "./data/soft.ckpt")  # now OK

    #all_vars = tf.trainable_variables()
    #for v in all_vars:
    #    print v.name, v.eval(sess)

    #print sess.run(name)

    correct_prediction = tf.equal(tf.argmax(softmax_tensor, 1), tf.argmax(y_, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    print(accuracy.eval({x: mnist.test.images, y_: mnist.test.labels}))
