
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