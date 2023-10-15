import numpy as np
from scipy.io import loadmat
import matplotlib.pyplot as plt

#Carregar o arquivo .mat
dados = loadmat('TransferFunction10.mat')

#Extraindo as variáveis e assegurando que são 1D
saida = dados.get('saida')
degrau = dados.get('degrau')
tempo = dados.get('t')


#Plotando os gráficos
plt.plot(tempo.T, saida, label='Saída')
plt.plot(tempo.T, degrau, label='Degrau de entrada')

#Legendas do Grafico
plt.xlabel('t[s]')
plt.ylabel('Amplitude')
plt.legend(loc='upper left')
plt.grid()
plt.show()


#Exercicio 2

#Conseguindo o maior e menor valor valor de saida
max_sinal = max(saida)
min_sinal = min(saida)
delta_sinal = max_sinal - min_sinal
degrau = degrau[1]

#Determinando t1 e t2
y_t1 = max_sinal * 0.283
y_t2 = max_sinal * 0.632

t1 = 4.48
t2 = 10.45
print(f'Y(t1) =  {y_t1[0]:.2f}   t1 = {t1}')
print(f'Y(t2) =  {y_t2[0]:.2f}  t2 = {t2}')

k = delta_sinal/degrau
tau = 1.5 * (t2 - t1)
theta = t2 - tau
print(f"K: {k[0]:.2f}")
print(f"τ: {tau:.2f}")
print(f"θ: {theta:.2f}")
