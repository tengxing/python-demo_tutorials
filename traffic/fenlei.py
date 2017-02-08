
#python ~/workspace/python/tensorflow/tensorflow/examples/image_retraining/retrain.py –bottleneck_dir=tf_files/bottlenecks –model_dir=tf_files/inception –output_graph=tf_files/retrained_graph.pb –output_labels=tf_files/retrained_labels.txt –image_dir=tf_files/bird_photos
http://www.tuicool.com/articles/ieQZVfa

import tensorflow as tf
import sys

# 命令行参数，传入要判断的图片路径
image_file = sys.argv[1]
# print(image_file)

# 读取图像
image = tf.gfile.FastGFile(image_file, 'rb').read()

# 加载图像分类标签
labels = []
for label in tf.gfile.GFile("output_labels.txt"):
    labels.append(label.rstrip())

# 加载Graph
with tf.gfile.FastGFile("output_graph.pb", 'rb') as f:
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(f.read())
    tf.import_graph_def(graph_def, name='')

with tf.Session() as sess:
    softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
    predict = sess.run(softmax_tensor, {'DecodeJpeg/contents:0': image})

# 根据分类概率进行排序
top = predict[0].argsort()[-len(predict[0]):][::-1]
for index in top:
    human_string = labels[index]
score = predict[0][index]
print(human_string, score)