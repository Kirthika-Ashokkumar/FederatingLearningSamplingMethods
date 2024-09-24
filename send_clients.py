import numpy as np
import pandas as pd 
from sklearn.linear_model import LogisticRegression
import SamplingMedthods 
from client import client 


file_name = input("Enter your file name: ")
df = pd.read_csv(file_name)
df = df.replace("Yes", 1)
df = df.replace("No", 0)
df = df.replace("Male", 1)
df = df.replace("Female", 0)
df = df.replace("Positive", 1)
df = df.replace("Negative", 0)

sample_type = int(input("Types of samples:\n\ncluster_sampling(1)\ncluster_sampling_w_repeats(2)\ndifferent_random_samples(3)\ndifferent_random_samples_w_repeats(4)\nsplit_by_variable(5)\nEnter number correspodning to sampling method: "))
samplesX = []
samplesY = []

df_train = df.sample(frac = 0.8)
df_test = df.drop(df_train.index)

if(sample_type == 1):
    X_header = ['Age', 'Gender', 'Polyuria', 'Polydipsia', 'sudden weight loss', 'weakness', 'Polyphagia', 'Genital thrush', 'visual blurring', 'Itching', 'Irritability', 'delayed healing', 'partial paresis', 'muscle stiffness', 'Alopecia', 'Obesity']
    y_header = ['class']
    num_samples = input("How many samples: ")
    size = input("Size of sample: ")
    SamplingMedthods.cluster_sampling(df_train, int(size), int(num_samples), samplesX, samplesY, X_header, y_header)
    print(samplesX)
    print(samplesY)
elif(sample_type == 2):
    X_header = ['Age', 'Gender', 'Polyuria', 'Polydipsia', 'sudden weight loss', 'weakness', 'Polyphagia', 'Genital thrush', 'visual blurring', 'Itching', 'Irritability', 'delayed healing', 'partial paresis', 'muscle stiffness', 'Alopecia', 'Obesity']
    y_header = ['class']
    num_samples = input("How many samples: ")
    size = input("Size of sample: ")
    SamplingMedthods.cluster_sampling_w_repeats(df_train, size, num_samples, samplesX, samplesY, X_header, y_header)
elif(sample_type == 3):
    pass
elif(sample_type == 4):
    pass
elif(sample_type == 5):
    pass

def send_weights():
    LogReg = LogisticRegression()
    count = 0
    first = True
    for x in samplesX:
        cl = client()
        print(samplesY[count])
        LogReg.fit( x.astype(float), np.ravel((samplesY[count]).astype(float) ))
        print(LogReg.coef_, LogReg.intercept_)
        msg = format_weights_biases(first, LogReg.coef_, LogReg.intercept_)
        print("hi")
        cl.send(msg)
        print("hi")
        if(count == len(samplesX) - 1):
            cl.send("end")
        cl.discconnect()
        count = count+ 1
        first = False

    
def format_weights_biases(first, weights, bias):
    msg = ""
    if(first):
        msg +="start"
    msg += "W"
    for w in weights:
        msg += str(w)
    msg = "B" + str(bias)
    return msg

send_weights()
samplesX.clear
samplesY.clear













