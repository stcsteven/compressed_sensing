from .framework import class_name
import numpy as np

# Signal to Noise Ratio (SNR)
# 
# array -> dataset array
# ddof -> degree of freedom 
# axis <= array_dimension - 1
# 
# 
def calculate_snr(array, axis, ddof=0):
    if class_name(array) == 'list':
      array = np.asanyarray(array) 
    mean = array.mean(axis)
    standard_deviation = array.std(axis = axis, ddof = ddof)
    return np.where(standard_deviation == 0, 0 , mean/standard_deviation) 