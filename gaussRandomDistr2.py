# °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
# Laboratorio di Matematica e Fisica Applicata - laurea triennale di Meccatronica 
#
# Docente: Prof. Alessandro Gabrielli (alessandro.gabrielli@unibo.it)
# Tutor: Francesca Del Corso (francesca.delcorso@unibo.it)
#
# A.A. 2021/2022

# °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°

# gaussRandomDistr2.py
#
# Il programma genera N numeri random da una distribuzione normale (gaussiana) con determinati mu e sigma e plotta l'istogramma delle frequenze e la PDF.


from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()  # creiamo Figure and Axes

mu = 0                    # mean
sigma = 1                 # std
nbins = 100 

# Inseriamo un numero N in input
N = int(input("Inserisci un numero: "))

# Generiamo N valori distribuiti come una gaussiana e inseriamoli in un array 'x'
x = np.random.normal(mu, sigma, N) 

# Plot istogramma
# density=True per avere valori tra 0 e 1
count, bins, columns = ax.hist(x, nbins, density=True)

y = norm.pdf(bins, mu, sigma)
ax.plot(bins, y, 'b--')

ax.set_xlabel('x')
ax.set_ylabel('Densità di probabilità')
ax.set_title('Istogramma di una Gaussiana con $\mu=0$, $\sigma=1$')
fig.tight_layout()      # ottimizza lo spazio fra i grafici
plt.show()

