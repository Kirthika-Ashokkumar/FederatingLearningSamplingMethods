import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def cluster_sampling(size, df, x, y, num_samples):
    df_train = df.sample(frac = 0.8)
    df_test = df.drop(df_train.index)
    X_test = np.array(df_test[x])
    y_test = np.array(df_test[y])
    shuffle = df_train.sample(frac = 1);
    samplesX = []
    samplesy = []
    count = 0

    if size > df.size/num_samples:
        raise Exception("For the given size the number of samples needed can not be made out of the data frame ") 

