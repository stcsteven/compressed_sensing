# Suppplementary library
import os
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy.optimize as spopt
import scipy.fftpack as spfft
import scipy.ndimage as spimg
import cvxpy as cvx

from helper.framework import *
from helper.statistics import *

number_of_elements = 1000
sample = int(number_of_elements * 0.3)
noise_mean = 0.
noise_sd = 0.

# Generate signal
def generate_signal_and_sample():    
    t = np.linspace(0, 1/256, number_of_elements)
    clean_signal = np.sin(1394 * np.pi * t)
    noise = np.random.normal(noise_mean, noise_sd, number_of_elements)
    signal = clean_signal + noise
    return t, signal

# Sampling the Signal
def sampling(t, signal):
    idx_sample = np.random.choice(number_of_elements, sample, replace=False)
    idx_sample.sort()
    x_sample = t[idx_sample]
    y_sample = signal[idx_sample]
    return idx_sample, x_sample, y_sample

# Reconstruction
def calculate(idxs, y_sample):
    A = spfft.idct(np.identity(number_of_elements), norm='ortho', axis=0)
    A = A[idxs]
    
    vx = cvx.Variable(number_of_elements)
    objective = cvx.Minimize(cvx.norm(vx, 1))
    constraints = [A*vx == y_sample]
    prob = cvx.Problem(objective, constraints)
    result = prob.solve(verbose=True)

    x = np.array(vx.value)
    x = np.squeeze(x)
    signal = spfft.idct(x, norm='ortho', axis=0)
    return signal

# Evaluation
def evaluation(t, signal, reconstructed_signal, idx_sample, y_sample):
    snr = calculate_snr(signal, 0, ddof=sample-1)
    figure_description = "Number of Elements: " + str(number_of_elements) +" // Samples: "+ str(sample) +"\nNoise Mean: "+ str(noise_mean) + " // Noise Standard Deviation: "+ str(noise_sd) +"\nSNR: " + str(snr)
    fig, axs = plt.subplots(3)
    fig.suptitle(figure_description)
    fig.tight_layout(pad=1.25)
    axs[0].set_title('original')
    axs[0].plot(t, signal)
    axs[1].set_title('sample')
    axs[1].plot(idx_sample, y_sample, 'rx')
    axs[2].set_title('reconstructed')
    axs[2].plot(t, reconstructed_signal)

    plt.show()

# Main Function
def main():
    t, signal = generate_signal_and_sample()
    idxs, x_sample, y_sample = sampling(t, signal)
    result = calculate(idxs, y_sample)
    evaluation(t, signal, result, idxs, y_sample)


if __name__ == "__main__":
    main()
