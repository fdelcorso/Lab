# °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
# Laboratorio di Matematica e Fisica Applicata - laurea triennale di Meccatronica 
#
# Docente: Prof. Alessandro Gabrielli (alessandro.gabrielli@unibo.it)
# Tutor: Francesca Del Corso (francesca.delcorso@unibo.it)
#
# A.A. 2021/2022

# °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°

# randomRandint.py
#
# ESEMPIO di generazione numeri interi random e di utilizzo subplots in matplotlib
#

import numpy as np
from matplotlib import pyplot as plt

#x = np.arange(0, 11, 1.)
x = np.random.randint(low=1, high=11, size=50)
print(x)
print(type(x))
y = 2*x + 10

# Plot
fig = plt.figure(figsize=(10,2))    
ax = fig.add_subplot(111)     
# 111 = prima cifra indica numero di righe, seconda cifra il numero di colonne, 
# terza cifra la cella corrispondente nella griglia generata con le prime due cifre 
ax.plot(x, y, 'mo')
ax.set_title('Performance attesa Esame Lab Fisica e Matematica applicata', fontdict={'size':12,'weight':'bold'})
ax.set_xlabel('Esercizi svolti', fontsize=10, size=10)
ax.set_ylabel('Votazione esame', fontsize=10)
plt.tight_layout()                  # ottimizza lo spazio fra i grafici
plt.show()
plt.close()