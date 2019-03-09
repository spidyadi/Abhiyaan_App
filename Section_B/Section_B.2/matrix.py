import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

x = tf.placeholder("float",[None,None])
# dynamic matrix
r = tf.reverse(x,[-1])
# reverse matrix along y axis
w = tf.matrix_band_part(r, -1, 0)
# gets lower left matrix
z = tf.matrix_band_part(r, 0, -1)
# gets higher right matrix
a = tf.matrix_band_part(r, 0, 0)
# gets diagonal matrix
y = tf.transpose(tf.reverse(w,[-1])) + tf.reverse(z,[-1]) - tf.reverse(a,[-1])
# transpose lower right triangle
with tf.Session() as session:
	# input you nxn matrix here
	x_data = [[1, 2, 3], 
              [4, 5, 6],
              [7, 8, 9]]
	result = session.run(y, feed_dict = {x : x_data})
	print(result);
	session.close()