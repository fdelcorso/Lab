# °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
# Laboratorio di Matematica e Fisica Applicata - laurea triennale di Meccatronica 
#
# Docente: Prof. Alessandro Gabrielli (alessandro.gabrielli@unibo.it)
# Tutor: Francesca Del Corso (francesca.delcorso@unibo.it)
#
# A.A. 2021/2022

# °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°

# gaussRandomDistribution.py
#
# Il programma genera Ngen numeri random da una distribuzione normale (gaussiana) con determinati mu e sigma.

import numpy as np
from matplotlib import pyplot as plt

mu, sigma = 0, 1
nbins = 30

# Inserimento di un numero di valori che si vuol generare in maniera random distribuiti come una gaussiana
N = int(input("Inserisci un numero: "))

np.random.seed(0)
s = np.random.normal(mu, sigma, N)

# Plot
# density=true normalizza i valori dell'istogramma dividendo il numero di elementi in ogni bin per il numero totale di elementi
# per poter comparare l'hist con la funzione di probabilità associata
count, bins, columns = plt.hist(s, nbins, density=True,  width=0.2)   
  
gauss = 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu)**2 / (2 * sigma**2) )
plt.plot(bins, gauss, 'r-', linewidth=2) 

plt.show()
plt.close()

