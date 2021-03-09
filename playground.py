import numpy as np
import scipy.fftpack as spfft

# Main Function
def main():
    print(np.identity(3))
    print(spfft.idct(np.identity(3), norm='ortho', axis=0))
if __name__ == "__main__":
  main()