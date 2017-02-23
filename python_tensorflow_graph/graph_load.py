import tensorflow as tf
from tensorflow.python.platform import gfile

with tf.Session() as persisted_sess:
  print("load graph")
  with gfile.FastGFile("graph/test.pb",'rb') as f:
    #create the default graph
    graph_def = tf.GraphDef()
    #parse the string from the f
    graph_def.ParseFromString(f.read())
    #import the persisted_sess from the graph_def
    persisted_sess.graph.as_default()
    tf.import_graph_def(graph_def, name='')
  print("map variables")
  persisted_result = persisted_sess.graph.get_tensor_by_name("saved_result:0")
  tf.add_to_collection(tf.GraphKeys.VARIABLES,persisted_result)
  try:
    saver = tf.train.Saver(tf.global_variables()) # 'Saver' misnomer! Better: Persister!
  except:pass
  print("load data")
  saver.restore(persisted_sess, "./data/checkpoint.ckpt")  # now OK
  print(persisted_result.eval())
  print("DONE")