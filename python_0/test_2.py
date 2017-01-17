import tensorflow as tf
state = tf.Variable(0,name= "tengxing")

one = tf.constant(1)
new_value = tf.add(state,one)
update = tf.assign(state,new_value)

# all variables  
init = tf.initialize_all_variables()

# session 
with tf.Session() as sess:
# all variables init
	sess.run(init)
	for step in range(3):
		sess.run(update)
		print (state)	
		print( sess.run(state))
print(state.name)
