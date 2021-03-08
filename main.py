# Suppplementary library
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy.optimize as spopt
import scipy.fftpack as spfft
import scipy.ndimage as spimg
import cvxpy as cvx

# sound i/o library
import librosa
import librosa.display

# Main Function
def main():
    audio_data = 'dataset/0dB.wav'
    print(os.path.exists(audio_data))
    x, sr = librosa.load(audio_data)
    print(x, class_name(x))
    print(sr)

if __name__ == "__main__":
    main()
