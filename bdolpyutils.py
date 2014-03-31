import cPickle
import numpy as np
import sys

def progBar(t, N, length=20, barChar='=', headChar='>'):
  sys.stdout.write('\r')
  formatStr = '[%-'+str(length)+'s] %d%% (%d/%d)'
  sys.stdout.write(formatStr %
      (barChar*int(float(t)/float(N)*length)+headChar, 
        np.ceil(float(t)/float(N)*100), t, N))
  sys.stdout.flush()

def loadMNIST(path, digits=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], asBitVector=False,
    asInt=False):
  print "Loading MNIST data for digits "+str(digits)+"... ",
  sys.stdout.flush()
  
  train, valid, test = cPickle.load(open(path, "rb"))

  X_train = train[0]
  Y_train = train[1]
  X_valid = valid[0]
  Y_valid = valid[1]
  X_test  = test[0]
  Y_test  = test[1]

  # Eliminate unused digits
  for d in range(0, 10):
    if d not in digits:
      X_train = np.delete(X_train, np.where(Y_train==d)[0], 0)
      Y_train = np.delete(Y_train, np.where(Y_train==d)[0], 0)
      X_valid = np.delete(X_valid, np.where(Y_valid==d)[0], 0)
      Y_valid = np.delete(Y_valid, np.where(Y_valid==d)[0], 0)
      X_test = np.delete(X_test, np.where(Y_test==d)[0], 0)
      Y_test = np.delete(Y_test, np.where(Y_test==d)[0], 0)

  # Transform labels to bit vectors for use in multilayer perceptrons
  if asBitVector:
    Y_tr = np.zeros((Y_train.shape[0], len(digits)))
    Y_va = np.zeros((Y_valid.shape[0], len(digits)))
    Y_te = np.zeros((Y_test.shape[0], len(digits)))

    for i in range(0, len(digits)):
      Y_tr[np.where(Y_train==digits[i]), i] = 1
      Y_va[np.where(Y_valid==digits[i]), i] = 1
      Y_te[np.where(Y_test==digits[i]), i] = 1

  else:
    Y_tr = Y_train
    Y_va = Y_valid
    Y_te = Y_test

  if asInt:
    X_train = (255.0*X_train).astype(int)
    X_valid = (255.0*X_valid).astype(int)
    X_test = (255.0*X_test).astype(int)

  print "Done!"
  return X_train, Y_tr, X_valid, Y_va, X_test, Y_te
