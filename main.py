import numpy as np
from scipy.io import loadmat
import matplotlib.pyplot as plt

# Carregar o arquivo .mat
dados = loadmat('TransferFunction6.mat')

# Extraindo as variáveis e assegurando que são 1D
saida = dados.get('saida').flatten()
degrau = dados.get('degrau').flatten()
tempo = dados.get('t').flatten()

# Encontrar o índice do primeiro valor em saida que é >= 28,3% e 63,2% de saida[-1]
L_t1 = np.where(saida >= 0.283 * saida[-1])[0][0]
L_t2 = np.where(saida >= 0.632 * saida[-1])[0][0]

# Tempo correspondente a 28,3% e 63,2% de saida[-1]
t1 = tempo[L_t1]
t2 = tempo[L_t2]

# Imprimir o tempo encontrado
print(f"delta = {saida[-1]:.2f}")
print("T1 = ",t1)
print("T2 = ",t2)
t = 1.5*(t2-t1)
print(f"t = {t}")
o = t2-t
print(f"Ø = {o}")
k = saida[-1]/degrau[-1]
print(f"k = {k}")
print(degrau[-1])

# Plotando os gráficos
plt.plot(tempo, saida, label='Saída')
plt.plot(tempo, degrau, label='Degrau de entrada')

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
