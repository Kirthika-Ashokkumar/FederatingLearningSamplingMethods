import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

def cluster_sampling(size, df_train, num_samples, samplesX, samplesy, X_header, y_header):
    shuffle = df_train.sample(frac = 1)

    if size > len(df_train)/num_samples:
        raise Exception("For the given size the number of samples needed can not be made out of the data frame ")
    
    incr = size
    beginIdx = 0
    nextIdx = beginIdx + incr

    X = np.array(shuffle[X_header])
    y = np.array(shuffle[y_header])

    for i in range(num_samples):
        samplesX.append(X[beginIdx:nextIdx])
        samplesy.append(y[beginIdx:nextIdx])
        beginIdx = nextIdx
        nextIdx = beginIdx + incr

    return len(samplesX)


def cluster_sampling_w_repeats(df_train, num_samples, fraction, samplesX, samplesy, X_header, y_header):
    shuffle = df_train.sample(frac = 1)

    if fraction > 1:
        raise Exception("The given percent is not possible")
    
    samps = []
    for i in range(num_samples):
        samps.append(df_train.sample(frac=fraction, replace=False))
        samplesX.append(np.array(samps[i][X_header]))
        samplesy.append(np.array(samps[i][y_header]))
    
    return samps[0:num_samples]


def different_random_samples(df_train, min_size, max_size, samplesX, samplesy, X_header, y_header):
    
    if (min_size < 0 or max_size > len(df_train)):
        raise Exception("Min size cannot be negative and max size cannot be bigger than df")
    
    shuffle = df_train.sample(frac = 1)

    beginIdx = 0
    nextIdx = beginIdx + random.randint(min_size, max_size)
    count = 0
    
    X = np.array(shuffle[X_header])
    y = np.array(shuffle[y_header])

    while (nextIdx < len(df_train)):
        samplesX.append(X[beginIdx:nextIdx])
        samplesy.append(y[beginIdx:nextIdx])
        count = count+1
        beginIdx = nextIdx
        nextIdx = beginIdx + random.randint(min_size, max_size)

    if (len(df_train) - nextIdx > 10):
        samplesX.append(X[nextIdx:len(df_train)])
        samplesy.append(y[nextIdx:len(df_train)])
  

    return len(samplesy)

    
def different_random_samples_w_repeats(df_train, min_size, max_size, num_samples, samplesX, samplesy, X_header, y_header):
    
    if (min_size < 0 or max_size > len(df_train)):
        raise Exception("Min size cannot be negative and max size cannot be bigger than df")
    
    # shuffle = df_train.sample(frac = 1)
    # samps = []
    count = 0
    num_rows = len(df_train) #added

    X = np.array(df_train[X_header])
    y = np.array(df_train[y_header])
    
    while (count < num_samples):
        beginIdx = random.randint(0, num_rows)
        sample_size = random.randint(min_size, max_size) #added
        endIdx = min(beginIdx + sample_size, num_rows)
        while( endIdx - beginIdx <  min_size):
           beginIdx = random.randint(0, num_rows)
           sample_size = random.randint(min_size, max_size) #added
           endIdx = min(beginIdx + sample_size, num_rows)
        samplesX.append(X[beginIdx:endIdx])
        samplesy.append(y[beginIdx:endIdx])
        count = count+1

    return len(samplesy)

def split_by_variable(df_train, column, variables, samplesX, samplesy, X_header, y_header):
  
    for i in range(len(variables)):
        filt = (df_train[column] == variables[i])
        df_filt = df_train[filt]
        shuffle = df_filt.sample(frac = 1)
        samplesX.append( np.array(shuffle[X_header]))
        samplesy.append( np.array(shuffle[y_header]))

