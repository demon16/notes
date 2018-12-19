
# 机器学习

  - 收集数据
  - 准备数据(抽取特征)
  - 选择/建立模型
  - 训练模型
  - 测试模型
  - 调节参数

## 基于深度神经网络的学习研究称之为深度学习
只有一个两个隐藏层的简单神经网络, 不把他称为深度神经网络, 大于两个隐藏层的神经网络我们称之为深度神经网络.

## tensorflow基础结构
  - 数据模型 Tensor(张量)
  - 计算模型 Graph(图)
  - 运行模型 Session(会话)

## 几种tensor
  - Constant 值不能改变的一种Tensor
  - Variable
  - Placeholder
  - SparseTensor

```python
# tf.constant
tf.constant(
    value,
    dtype=None,
    shape=None,
    name='Const',
    verify_shape=False
)

# tf.Variable
__init__(
    initial_value=None,
    trainable=True,
    collections=None,
    validate_shape=True,
    caching_device=None,
    name=None,
    variable_def=None,
    dtype=None,
    expected_shape=None,
    import_scope=None,
    constraint=None
)

# tf.placeholder
tf.placeholder(
    dtype,
    shape=None,
    name=None
)

# tf.SparseTensor
SparseTensor(indices=[[0, 0], [1, 2]], values=[1, 2], dense_shape=[3, 4])
# output
[[1, 0, 0, 0]
 [0, 0, 2, 0]
 [0, 0, 0, 0]]

sess = tf.Session()
sess.run(xxx)
run(
    fetches,
    feed_dict=None,
    options=None,
    run_metadata=None
)
```

## 用tensorflow保存图的信息到日志中
```python
tf.summary.FileWriter("log_path", sess.graph)
```

## 矢量运算
```python
primes = tf.constant([2, 3, 5, 7, 11, 13], dtype=tf.int32)
# add
one = tf.constant(1, dtype=tf.int32)
just_beyond_primes = tf.add(primes, one)

# muliply1
two = tf.constant(2, dtype=tf.int32)
primes_doubled = primes * two

# multipyl2
tf.multiply(primes, primes)

# pow
tf.pow(primes, 2)

# substract
tf.substract(primes, one)

# Reshape two tensors in order to muliply them
a = tf.constant([5, 3, 2, 7, 1, 4])
b = tf.constant([4, 6, 3])
reshaped_a = tf.reshape(a, [2, 3])
reshaped_b = tf.reshape(b, [3, 1])
tf.matmul(a, b)
```

# 变量赋值
```python
v = tf.contrib.eager.Variable([3])

v = tf.contrib.eager.Variable([3])

# Create a vector variable of shape [1, 4], with random initial values,
# sampled from a normal distribution with mean 1 and standard deviation 0.35.
w = tf.contrib.eager.Variable(tf.random_normal([1, 4], mean=1.0, stddev=0.35))

# 向变量赋新值时, 其形状必须和之前的形状一致.
tf.assign(v, [7])
v.assign([5])
```

# concat
```python
die1 = tf.contrib.eager.Variable(
    tf.random_uniform([10, 1], minval=1, maxval=7, dtype=tf.int32))
die2 = tf.contrib.eager.Variable(
    tf.random_uniform([10, 1], minval=1, maxval=7, dtype=tf.int32))
dice_sum = tf.add(die1, die2)
resulting_matrix = tf.concat(values=[die1, die2, dice_sum], axis=1)
```