# Suppplementary library
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy.optimize as spopt
import scipy.fftpack as spfft
import scipy.ndimage as spimg
import cvxpy as cvx

from helper.framework import class_name, visualize

# Main Function
def main():
    n = 5000
    t = np.linspace(0, 1/8, n)
    y = np.sin(1394 * np.pi * t) + np.sin(3266 * np.pi * t)
    yt = spfft.dct(y, norm='ortho')

    m = 500 # 10% sample
    ri = np.random.choice(n, m, replace=False) # random sample of indices
    ri.sort() # sorting not strictly necessary, but convenient for plotting
    t2 = t[ri]
    y2 = y[ri]
    
    visualize(plt, figure_title='sinusoidal wave', figure_size = (14,5))
    plot1=plt.figure(1)
    plt.plot(t,y)
    plt.plot(t2, y2, 'ro')
    plot2=plt.figure(2)
    plt.plot(t,yt)
    plt.show()
    

if __name__ == "__main__":
    main()
