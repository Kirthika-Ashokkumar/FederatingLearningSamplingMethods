import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def cluster_sampling(size, df_train, num_samples, samplesX, samplesy, X_header, y_header):
    shuffle = df_train.sample(frac = 1)

    if size > df_train.size/num_samples:
        raise Exception("For the given size the number of samples needed can not be made out of the data frame ")
    
    samps = np.array_split(shuffle, size)

    for i in range(num_samples):
        samplesX.append(np.array(samps[i][X_header]))
        samplesy.append(np.array(samps[i][y_header]))

    return samps[0:num_samples]

def cluster_sampling_w_rpeats(df_train, num_samples, fraction, samplesX, samplesy, X_header, y_header):
    shuffle = df_train.sample(frac = 1)

    if fraction > 1:
        raise Exception("The given percent is not possible")
    
    samps = []
    for i in range(num_samples):
        samps.append(df_train.sample(frac=fraction, replace=False))
        samplesX.append(np.array(samps[i][X_header]))
        samplesy.append(np.array(samps[i][y_header]))
    
    return samps[0:num_samples]
    




#same size no repeats --> size of the sample, data frame, x - column header, y row header, number samples
# return an array of the samples
#same size yes repeats

# different size (random) --> number of samples, range of size, data frame,  x - column header, y row header
# different size (random) with repeats
# return an array of the samples
# stratfied - how we will approach
