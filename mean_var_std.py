import numpy as np

def calculate(list):

  len_list = len(list)

  if len_list != 9:
    raise ValueError("List must contain nine numbers.")

  methods = [np.mean, np.var, np.std, np.max, np.min, np.sum]
  names = ["mean", "variance", "standard deviation", "max", "min", "sum"]

  fnc = lambda arr, axis, f : f(arr, axis)

  np_list = np.array(list).reshape(3,3)

  calculations = {}

  for met, nam in zip(methods, names):
    calculations[nam] = [
      fnc(np_list, 0, met).tolist(), 
      fnc(np_list, 1, met).tolist(), 
      fnc(np_list, None, met), 
    ]


  return calculations