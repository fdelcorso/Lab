import numpy as np

from matplotlib import pyplot as plt

def nuovaFunzione(x):
    y = 10*np.cos(x) - x
    return (y)

def main():

    y = np.linspace(-10, 10, 100) 
    ris = nuovaFunzione(y)

    # Plot della funzione
    plt.plot(y, ris, 'ro', width=0.095)
    plt.show()
    plt.close()
    #print(ris)

if (__name__ == "__main__"):
    main()

