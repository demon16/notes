
import tensorflow as tf

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

hw = tf.constant("hello world.")

# sess = tf.Session()

# print(sess.run(hw))

# sess.close()

a = tf.constant(2)
print(a)
b = tf.constant(3)
c = tf.multiply(a, b)
d = tf.add(c, 1)

with tf.Session() as sess:
    print(sess.run(d))