# °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
# Laboratorio di Matematica e Fisica Applicata - laurea triennale di Meccatronica 
#
# Docente: Prof. Alessandro Gabrielli (alessandro.gabrielli@unibo.it)
# Tutor: Francesca Del Corso (francesca.delcorso@unibo.it)
#
# A.A. 2021/2022

# °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°

# uniformRandomDistribution.py
#
# Il programma genera Ngen numeri random con distribuzione uniforme in un determinato intervallo.
#

import numpy as np
from matplotlib import pyplot as plt

# Impostiamo il generatore di numeri pseudocasuali di numpy per ottenere sempre la stessa sequenza (per replicare la randomizzazione)
np.random.seed(123)   
                      
Ngen = int(input("Indica quanti numeri random si vogliono generare: "))
print(type(Ngen))

# Generiamo Ngen valori secondo una distribuzione uniforme e li salviamo in un numpy.ndarray
uniforme = np.random.uniform(0.,1.,Ngen) 

bins = np.linspace(0,1,11)                    # array di valori spaziati uniformemente su uno specifico intervallo

plt.hist(uniforme, bins, width=0.095, alpha=0.7, color='green')  
plt.title("Istogramma distribuzione random uniforme \n")
plt.xlabel("Intervallo")                              # label asse x
plt.ylabel('Numero valori')                              # label asse y

plt.show()
plt.close()




