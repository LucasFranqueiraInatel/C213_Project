import numpy as np
from scipy.io import loadmat
import matplotlib.pyplot as plt

# Carregar o arquivo .mat
dados = loadmat('TransferFunction6.mat')

# Extraindo as variáveis e assegurando que são 1D
saida = dados.get('saida').flatten()
degrau = dados.get('degrau').flatten()
t = dados.get('t').flatten()

# Encontrar o índice do primeiro valor em saida que é >= 28,3% e 63,2% de saida[-1]
L_t1 = np.where(saida >= 0.283 * saida[-1])[0][0]
L_t2 = np.where(saida >= 0.632 * saida[-1])[0][0]

# Tempo correspondente a 28,3% e 63,2% de saida[-1]
t1 = t[L_t1]
t2 = t[L_t2]

# Imprimir o tempo encontrado
print("T1=",t1)
print("T2=",t2)

# Plotando os gráficos
plt.plot(t, saida, label='Saída')
plt.plot(t, degrau, label='Degrau de entrada')

# Marcar os pontos t1 e t2 no gráfico
plt.scatter([t1, t2], [saida[L_t1], saida[L_t2]], color='red')  # desenha os pontos em vermelho

# Anotação dos pontos
plt.annotate(f'T1 ({t1:.2f}s)', (t1, saida[L_t1]), textcoords="offset points", xytext=(-10,10), ha='center', fontsize=8, color='red')
plt.annotate(f'T2 ({t2:.2f}s)', (t2, saida[L_t2]), textcoords="offset points", xytext=(-10,10), ha='center', fontsize=8, color='red')

plt.xlabel('t[s]')
plt.ylabel('Amplitude')
plt.legend(loc='upper left')
plt.grid()
plt.show()
