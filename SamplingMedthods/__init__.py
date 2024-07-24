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


#same size no repeats --> size of the sample, data frame, x - column header, y row header, number samples
# return an array of the samples
#same size yes repeats

# different size (random) --> number of samples, range of size, data frame,  x - column header, y row header
# different size (random) with repeats
# return an array of the samples
# stratfied - how we will approach
