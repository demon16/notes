import tensorflow as tf

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


w = tf.Variable(2.0, dtype=tf.float32, name="Weight") # 权重
b = tf.Variable(1.0, dtype=tf.float32, name="Bias") # 偏差
x = tf.placeholder(dtype=tf.float32, name="Input") # 输入

with tf.name_scope("Output"): # 输出的命名空间
    y = w * x + b # 输出

path = './log'

# 创建用于初始化的所有变量(Variable)的操作
init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    writer = tf.summary.FileWriter(path, sess.graph)
    # 因为x是一个placeholder, 需要进行值的填充
    result = sess.run(y, {x: 3.0})
    print("y = %s " % result)
