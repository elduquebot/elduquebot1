import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Programa basico para simular la compra y venta de una sola accion basada en una
#estrategia de medias moviles

def sma(data, period):   #subfuncion para obtener el sma
    sma1=np.zeros(data.size+1-period)
    for step in range(
            len(sma1)):
        sma1[step]=np.mean(data[step:period+step])
    return sma1

arr_buy = []
arr_buy_x = []
arr_sell = []
arr_sell_x = []
datos = pd.read_csv("goog.csv")  # se lee el csv
datos = datos.iloc[::-1]  # aqui se giran las columnas para que esten en orden por fechas
cierre = np.array(datos["Adj Close"])
periodo = 50  # periodo del sma
sma = sma(datos["Adj Close"], periodo)  # calculo del sma
x = np.arange(0, len(datos["Adj Close"]))  # eje x para graficar
buy = 0  # bandera de compra
cash = 0  # dinero

for step in range(1,len(sma)):
    step2 = step + (len(cierre) - len(sma))
    if cierre[step2] > sma[step] and buy == 0 and cierre[step2 - 1] <= sma[step - 1]:
        arr_buy.append(cierre[step2])
        arr_buy_x.append(x[step2])
        buy = 1
        cash = cash - cierre[step2]

    elif cierre[step2] < sma[step] and buy == 1 and cierre[step2 - 1] >= sma[step - 1]:
        arr_sell.append(cierre[step2])
        arr_sell_x.append(x[step2])
        cash = cash + cierre[step2]
        buy = 0


if buy == 1: #venta final
    cash = cash + cierre[step2]




print "cash", cash
plt.plot(x, datos["Adj Close"], label="Adj Close")  # grafica  precio de cierre
plt.plot(x[periodo-1:], sma, label="Sma " + str(periodo))  # grafica sma
plt.scatter(arr_buy_x, arr_buy, color="y", s=40, label="Buy") #Puntos de compra
plt.scatter(arr_sell_x, arr_sell, color="r", s=40, label="Sell") # puntos de venta
plt.legend()
plt.grid(True)
plt.show()