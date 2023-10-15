import numpy as np
import control as cnt
import matplotlib.pyplot as plt
from scipy.io import loadmat

# Importar os dados do arquivo .mat
mat = loadmat('TransferFunction10.mat')
degrau = mat.get('degrau')
saida = mat.get('saida')
t1 = mat.get('t')

# Parâmetros da função de transferência em primeira ordem
k = 2.193
tau = 8.95
theta = 1.49

# Construir a função de transferência
num = np.array([k])
den = np.array([tau, 1])
H = cnt.tf(num, den)

# Montar o sistema usando expansão de Pade
n_pade = 20
(num_pade, den_pade) = cnt.pade(theta, n_pade)
H_pade = cnt.tf(num_pade, den_pade)
Hs = cnt.series(H, H_pade)

# Simular a resposta da função de transferência estimada
time, y = cnt.step_response(10*Hs, T=t1)

# Plotar os gráficos
plt.figure(figsize=(10, 6))
plt.plot(time, y, label='Resposta estimada', linewidth=2)
plt.plot(time, saida, label='Resposta fornecida', linestyle='dashed', linewidth=2)
plt.plot(time, degrau, label='Entrada (degrau)', linestyle='dotted', linewidth=2)

# Adicionar legendas e título
plt.xlabel('Tempo [s]', fontsize=12)
plt.ylabel('Amplitude', fontsize=12)
plt.legend(loc='upper right', fontsize=10)
plt.title('Resposta da Função de Transferência Fornecida e Estimada', fontsize=14)

# Adicionar grade
plt.grid(True)

# Exibir o gráfico
plt.show()
