import tensorflow as tf

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


const1 = tf.constant([[2, 2]])
const2 = tf.constant([[4], [4]])

# 矩阵乘法运算matrix mul tf.add()
multiple = tf.matmul(const1, const2)
print(multiple)

sess = tf.Session()

result = sess.run(multiple)

print(result)

if const1.graph is tf.get_default_graph():
    print("const1所在的图(Graph)是当前上下文默认的图")

sess.close()

with tf.Session() as sess:
    result2 = sess.run(multiple)
    print("Multiple的结果是 %s " % result2)