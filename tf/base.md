**经验风险最小化** 检查多个样本并尝试找出可最大限度地减少损失的模型

**损失** 对糟糕预测的惩罚.是一个数值, 表示对于单个样本而言模型预测的准确程度

**平方损失**  L2损失
```
  = the square of the difference between the label and the prediction
  = (observation - prediction(x))2
  = (y - y')2
```

**均方误差(MSE)** 每个样本的平均平方损失. 虽然`MSE`常用于机器学习, 但它既不是唯一实用的损失函数，也不是适用于所有情形的最佳损失函数

![flow](.resource/flow.png)

**收敛** 不断迭代, 直到总体损失不再变化或至少变化极其缓慢为止. 这时候, 我们可以说该模型已经收敛

**梯度下降法**
  - 梯度下降法的第一个阶段是为 `w1`选择一个其实值(起点).
  - 然后, 梯度下降法算法会计算损失曲线在起点处的梯度. 简而言之, **梯度**是偏导数的矢量; 它可以让你了解哪个方向距离目标"更近"或"更远".

**学习速率/步长** 梯度下降法算法乘以一个称为学习效率(步长)的表量, 以确定下一个点的位置. 如果梯度大小为2.5, 学习效率为0.01, 则梯度下降法算法会选择距离前一个点0.025的位置作为下一个点.

**超参数** 编程人员在机器学习算法中用于调整的"旋钮", 大多数机器学习编程人员会花费相当多的时间来调整学习速率. 如果选择的学习速率过小, 就会花费太长的学习时间. 相反, 如果指定的学习速率过大, 下一个点将永远在U形曲线的底部随意弹跳.

**批量** 用于在单次迭代中计算梯度的样本总数

**随机梯度下降法(SGD)** 每次迭代只使用一个小样本(批量大小为1). 如果进行足够的迭代, `SGD`也可以发挥作用, 但过程会非常杂乱.

**小批量随机梯度下降法(小批量SGD)** 介于全批量迭代与SGD之间的折衷方案. 小批量通常包含10-1000个随机选择的样本. 小批量SGD可以减少SGD中的杂乱样本数量, 但仍然比全批量更高效.
