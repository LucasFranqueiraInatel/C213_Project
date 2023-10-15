import numpy as np
from scipy.io import loadmat
import matplotlib.pyplot as plt

# Carregar o arquivo .mat
dados = loadmat('TransferFunction6.mat')

# Extraindo as variáveis
saida = dados.get('saida')
degrau = dados.get('degrau')
t = dados.get('t')

graf1 = plt.plot(t.T,saida, label='Saída')
graf1 = plt.plot(t.T,degrau, label='Degrau de entrada')

plt.xlabel('t[s]')
plt.ylabel('Amplitude')
plt.legend(loc='upper left')

plt.grid()
plt.show()


# L = np.where(saida > 0.283*saida[-1])[0][0]
# T = np.where(saida > 0.632*saida[-1])[0][0] - L


# k = saida[-1]/degrau[-1]  # Ganho estático
# tau = T  # Constante de tempo
# theta = L  # Atraso de tempo
#
# print(f"k = {k}, τ = {tau}, Ɵ = {theta}")