import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Programa basico para calcular medias moviles y graficarlas

def sma(data, period):   #subfuncion para obtener el sma
    sma1=np.zeros(data.size+1-period)
    for step in range(
            len(sma1)):
        sma1[step]=np.mean(data[step:period+step])
    return sma1

datos = pd.read_csv("goog.csv")  # se lee el csv
datos = datos.iloc[::-1]  # aqui se giran las filas para que esten en orden por fechas
periodo = 100  # periodo del sma
sma = sma(datos["Adj Close"], periodo)  # calculo del sma
x = np.arange(0, len(datos["Adj Close"]))  # eje x para graficar

plt.plot(x, datos["Adj Close"], label="Adj Close")  # grafica  precio de cierre
plt.plot(x[periodo-1:], sma, label="Sma " + str(periodo))  # grafica sma
plt.legend()
plt.grid(True)
plt.show()
