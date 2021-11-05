# °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
# Laboratorio di Matematica e Fisica Applicata - laurea triennale di Meccatronica 
#
# Docente: Prof. Alessandro Gabrielli (alessandro.gabrielli@unibo.it)
# Tutor: Francesca Del Corso (francesca.delcorso@unibo.it)
#
# A.A. 2021/2022

# °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
# testmatplotlib.py
#
# Esempio di distribuzione binomiale random. 
# https://numpy.org/doc/stable/reference/random/generated/numpy.random.binomial.html

import numpy as np
from matplotlib import pyplot as plt


x = np.random.binomial(n=10, p=0.5, size=100 )  # n= numero di prove, p=probabilita'ad ogni prova size=numero di volte che ripeto
y = np.random.binomial(n=10, p=0.5, size=x.size)
data = np.column_stack((x, y))

# Plot
fig, (ax1, ax2)  = plt.subplots(nrows=1, ncols=2, figsize=(8, 4))     # larghezza: 8 pollici, altezza: 4 pollici

ax1.scatter(x, y, marker='o', c='r', edgecolor='b')
ax1.set_title('Scatter plot')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_xlim(0)

ax2.hist(data, bins=np.arange(data.min(), data.max()), label=('x', 'y'))
ax2.legend(loc='upper left')
ax2.set_title('Frequencies of $x$ and $y$')
ax2.yaxis.tick_right()
plt.tight_layout()                  # ottimizza lo spazio fra i grafici
plt.show()
plt.close()


