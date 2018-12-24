# from __future__ import print_function

# import math

# from IPython import display
# from matplotlib import cm
# from matplotlib import gridspec
# from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
pd.set_option('display.max_columns', None)
# from sklearn import metrics
import tensorflow as tf
# from tensorflow.python.data import Dataset

# tf.logging.set_verbosity(tf.logging.ERROR)
# pd.options.display.max_rows = 10
# pd.options.display.float_format = '{:.1f}'.format

california_housing_dataframe = pd.read_csv("https://download.mlcc.google.cn/mledu-datasets/california_housing_train.csv", sep=",")
california_housing_dataframe = california_housing_dataframe.reindex(
    np.random.permutation(california_housing_dataframe.index))
california_housing_dataframe["median_house_value"] /= 1000.0
california_housing_dataframe
print(california_housing_dataframe)
print(california_housing_dataframe.describe())
print(california_housing_dataframe.head())

# Define the input feature: total_rooms.
my_feature = california_housing_dataframe[["total_rooms"]]

# Configure a numeric feature column for total_rooms.
feature_columns = [tf.feature_column.numeric_column("total_rooms")]
print(feature_columns)

# Define the label.
targets = california_housing_dataframe['median_house_value']

