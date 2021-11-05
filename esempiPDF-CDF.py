# °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
# Laboratorio di Matematica e Fisica Applicata - laurea triennale di Meccatronica 
#
# Docente: Prof. Alessandro Gabrielli (alessandro.gabrielli@unibo.it)
# Tutor: Francesca Del Corso (francesca.delcorso@unibo.it)
#
# A.A. 2021/2022

# °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
# esempiPDF-CDF.py
#
# Esempi di utilizzo delle funzioni PDF (Probability Density Function), CDF (Cumulative Density Function) dalla libreria norm di scipy
#

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


def gauss(x, mu, sigma):	
    return (1/(np.sqrt(2*np.pi)*sigma))* np.exp(-np.power(x-mu,2)/(2*np.power(sigma,2)))


np.random.seed(123)                    # per generare sempre la stessa sequenza

mu = 0                                 # media
sigma = 1                              # standard deviation
s = np.random.normal(mu,sigma,1000) 
x = np.linspace(0,1000, 1000)

# Verifichiamo media e varianza:
a = abs(mu-np.mean(s))
print("Media: ",a)
b= abs(sigma-np.std(s))
print("Sigma: ",b)

# Istogramma del campione, insieme alla PDF 
nBins=100
xmin = mu - 5*sigma
xmax = mu + 5*sigma

x = np.linspace(xmin,xmax,nBins)
binwidth = (xmax-xmin)/float(nBins)

plt.hist(s, x, density=True, label="histogram")
gauss = 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (x - mu)**2 / (2 * sigma**2) )
plt.plot(x,gauss, color='r', linewidth=2, label="Gauss")
plt.xlabel( r"$x$" )
plt.legend()

plt.show()
plt.close()


# PDF , CDF, Prob usando scipy
pdf = norm.pdf(x, mu, sigma)
plt.grid()

plt.plot(x,pdf, '-', color='r', label= 'PDF')

cdf = norm.cdf(x, mu,sigma)
plt.plot(x,cdf, 'b+', label='CDF' )

print("Normal distribution:")
print("Media :", norm.mean(mu,sigma))
print("std:",norm.std(mu,sigma) )

plt.legend()

plt.show()
plt.close()