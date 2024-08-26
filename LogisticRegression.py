import numpy as np

def sigmoid(x):
  return 1/(1+np.exp(-x))

class LogisticRegression():

  def __init__(self, lr=0.001, n_iters = 1000):
    self.lr = lr
    self.n_iters = n_iters
    self.weights = None
    self.bias = None

  # x1, x2 -> y
  # sigmoid(a * x1 + b * x2 + c) = y

  def fit(self, X, y):
    print(X.shape)
    n_samples, n_features = X.shape
    self.weights = np.zeros(n_features)
    self.bias = 0

    for _ in range(self.n_iters):
      linear_pred = np.dot(X, self.weights ) + self.bias
      predictions = sigmoid(linear_pred)

      dw = (1/n_samples) * np.dot(np.transpose(X), (predictions -y))
      db = (1/n_samples) * np.sum(predictions - y)
      self.weights = self.weights - self.lr*dw
      self.bias = self.bias - self.lr*db

  def predict(self, x):
    # print(self.weights)

    linear_pred = np.dot(x, self.weights ) + self.bias
    y_pred = sigmoid(linear_pred)

    class_pred = [0 if y<=0.5 else 1 for y in y_pred]
    return class_pred


def predict_Average(x, list_w, list_b):
    n_samples, n_features = x.shape
    sumW=np.zeros(n_features)
    count = 0
    for w in list_w:
      sumW = sumW+w
      count = count +1
    avgW = sumW/count
    print(avgW)

    count=0
    sumb = 0
    for b in list_b:
      sumb = sumb+b
      count = count +1
    avgb = sumb/count

    linear_pred = np.dot(x, avgW) + avgb

    y_pred = sigmoid(linear_pred)
    class_pred = [0 if y<=0.5 else 1 for y in y_pred]
    return class_pred

def accuracy(y_pred, y_test):
  return np.sum(y_pred == np.ravel(y_test) )/len(y_test)