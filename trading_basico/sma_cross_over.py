import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Programa basico para simular la compra y venta de una sola accion basada en una
#estrategia basada en cruce de medias moviles

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
periodo_fast = 20  # periodo del sma rapido
periodo_slow = 50  # periodo del sma lento
sma_fast = sma(datos["Adj Close"], periodo_fast)  # calculo del sma rapido
sma_slow = sma(datos["Adj Close"], periodo_slow)  # calculo del sma rapido
x = np.arange(0, len(datos["Adj Close"]))  # eje x para graficar
buy = 0  # bandera de compra
cash = 0  # dinero

for step in range(1, len(sma_slow)):
    step2 = step + (len(sma_fast) - len(sma_slow))
    step_cierre = step + (len(cierre) - len(sma_slow))
    if sma_fast[step2] > sma_slow[step] and buy == 0 and sma_fast[step2 - 1] <= sma_slow[step - 1]:
        arr_buy.append(cierre[step_cierre])
        arr_buy_x.append(x[step_cierre])
        buy = 1
        cash = cash - cierre[step_cierre]

    elif sma_fast[step2] < sma_slow[step] and buy == 1 and sma_fast[step2 - 1] >= sma_slow[step - 1]:
        arr_sell.append(cierre[step_cierre])
        arr_sell_x.append(x[step_cierre])
        cash = cash + cierre[step_cierre]
        buy = 0


if buy == 1: #venta final
    cash = cash + cierre[step_cierre]


print "cash", cash
plt.plot(x, datos["Adj Close"], label="Adj Close")  # grafica  precio de cierre
plt.plot(x[periodo_fast-1:], sma_fast, label="Sma " + str(periodo_fast))  # grafica sma rapido
plt.plot(x[periodo_slow-1:], sma_slow, label="Sma " + str(periodo_slow))  # grafica sma rapido
plt.scatter(arr_buy_x, arr_buy, color="y", s=40, label="Buy") #Puntos de compra
plt.scatter(arr_sell_x, arr_sell, color="r", s=40, label="Sell") # puntos de venta
plt.legend()
plt.grid(True)
plt.show()