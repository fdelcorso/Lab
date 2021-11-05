# °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
# Laboratorio di Matematica e Fisica Applicata - laurea triennale di Meccatronica 
#
# Docente: Prof. Alessandro Gabrielli (alessandro.gabrielli@unibo.it)
# Tutor: Francesca Del Corso (francesca.delcorso@unibo.it)
#
# A.A. 2021/2022

# °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°

# calcoloPigrecoMontecarlo.py
#
# Calcolo di π = 4*Ac/Aq utilizzando il metodo Monte Carlo. Semplificazione: il centro del cerchio ha coordinate (0,0) e raggio 1, x in [-1,1], y in [-1,1]
#  

import matplotlib.pyplot as plt
import numpy as np
import random            # https://docs.python.org/3/library/random.html

N = int(input("Inserisci il numero di punti per approssimare π: ")) 
puntiCerchio = 0

X_in = []               # (X,Y) sono le coppie di valori dentro il cerchio inscritto nel quadrato
Y_in = []
X_out =[]               # (X_out,Y_out) sono le coppie di valori fuori dal cerchio ma dentro il quadrato circoscritto
Y_out =[]
for i in range(N):
    x = random.uniform(-1.0,1.0)         
    y = random.uniform(-1.0,1.0)
    if (x**2+y**2 <= 1):
        X_in.append(x)
        Y_in.append(y)
        puntiCerchio += 1
    else:   
        X_out.append(x)
        Y_out.append(y)

pigreco = 4*puntiCerchio/N
print("Valore approssimato di pigreco per " + str(N) + " punti: " + str(pigreco) )

# precisione
pi = np.pi
err = pigreco/pi
prec = abs(1-err)*100
print(f'Precisione:  {prec:.2f} % ')

# Plot
plt.scatter(X_in, Y_in, color="green", marker   =".")
plt.scatter(X_out, Y_out, color="red", marker   =".")

x_coord = np.linspace(-1,1)         # default: 50 valori
y_coord = np.sqrt(1-(x_coord**2))
plt.plot(x_coord, y_coord, color= "k")
plt.plot(x_coord, -y_coord, color= "k")

plt.title("Calcolo π con metodo Monte Carlo \n")

plt.show()
plt.close()
