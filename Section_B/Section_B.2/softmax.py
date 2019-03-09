import tensorflow as tf
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

def softmax(x):
  return tf.exp(x)/tf.reduce_sum(tf.exp(x), 1)
  # softmax of the each row of matrix

x = tf.placeholder("float",[None,None])
# dynamic matrix
y = softmax(x)
# softmax of each row of matrix x
with tf.Session() as session:
	# input you nxn matrix here
	x_data = [[1, 2, 3],
			  [4, 5, 6],
			  [7, 8, 9]]
	result = session.run(y, feed_dict = {x : x_data})
	print(result);
	session.close()