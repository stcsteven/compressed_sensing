# Suppplementary library
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy.optimize as spopt
import scipy.fftpack as spfft
import scipy.ndimage as spimg
import cvxpy as cvx

from helper.framework import *
from helper.statistics import *

number_of_elements = 100
noise_mean = 3
noise_sd = 0.1

# Generate signal
def generate_signal():    
    t = np.linspace(0, 1/256, number_of_elements)
    clean_signal = np.sin(1394 * np.pi * t)
    noise = np.random.normal(noise_mean, noise_sd, number_of_elements)
    signal = clean_signal + noise
    snr = calculate_snr(signal, 0, ddof=0)
    figure_description = "SNR: " + str(snr)
    figure_subtitle = "Noise Mean: "+ str(noise_mean) + "\nNoise SD: "+ str(noise_sd)
    
    visualize(plt, figure_title=figure_description, figure_size = (14,5), figure_subtitle=figure_subtitle)
    plt.figure(1)
    plt.plot(t,signal)
    plt.show()
    
# Main Function
def main():
    generate_signal()
    
if __name__ == "__main__":
    main()
