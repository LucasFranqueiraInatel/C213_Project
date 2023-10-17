import numpy as np
import control as cnt
import matplotlib.pyplot as plt
from scipy.io import loadmat

# Importar os dados do arquivo .mat
mat = loadmat('TransferFunction10.mat')
degrau = mat.get('degrau')
saida = mat.get('saida')
t1 = mat.get('t')

# Parâmetros da função de transferência encontrados
k = 2.193
tau = 8.95
theta = 1.49

num = np.array([k]) # Cria um array contendo um único elemento, 'k'
den = np.array([tau, 1]) # Cria um array contendo o valor de 'tau' e 1
H = cnt.tf(num, den) # Cria uma funcao de transferencia


# Montar o sistema usando expansão de Pade
n_pade = 20 # Define a ordem da aproximação de Padé.
(num_pade, den_pade) = cnt.pade(theta, n_pade) # Gera polinômios para aproximação de Padé do atraso "theta".
H_pade = cnt.tf(num_pade, den_pade) # Cria uma função de transferência usando os polinômios obtidos.
Hs = cnt.series(H, H_pade) # Concatena em série as funções de transferência H e H_pade.


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

# Calcular a diferença entre a resposta estimada e a resposta fornecida em cada ponto do tempo
diff = y - saida.flatten()
# Encontrar o valor máximo absoluto dessa diferença
max_diff = np.max(np.abs(diff))
print("A maior diferença entre as respostas é:", max_diff)
