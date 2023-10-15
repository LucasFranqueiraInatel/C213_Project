import numpy as np
import control as cnt
import matplotlib.pyplot as plt

k = 2.193
tau = 8.95
theta = 1.49

num = np. array ([k]) # Cria um array contendo um único elemento, 'k'
den = np. array ([tau , 1])# Cria um array contendo o valor de 'tau' e 1
H = cnt.tf(num , den)# Cria uma funcao de transferencia

# Montar o sistema usando expansão de Pade
n_pade = 20 # Define a ordem da aproximação de Pade.
( num_pade , den_pade ) = cnt.pade ( theta , n_pade ) # Gera polinômios para aproximação de Padé do atraso "theta".
H_pade = cnt.tf( num_pade , den_pade )# Cria uma função de transferência usando os polinômios obtidos.

Hs = cnt.series (H , H_pade)
Hmf = cnt.feedback(Hs, 1)
t = np.linspace (0 ,50, 300)

# Vamos multiplicar Hs e Hmf por 10, pq é o valor do degrau
(t , y ) = cnt.step_response ( 10*Hs, t )
plt.plot(t, y, label='Malha Aberta')

(t , y1 ) = cnt.step_response ( 10*Hmf, t)
plt.plot(t, y1, label='Malha Fechada')

plt.xlabel ( ' t [ s ] ')
plt.ylabel('Amplitude')
plt.legend(loc='lower right')

plt.title('Malha Aberta x Malha Fechada')
plt.grid ()
plt.show()

# Erro de estado estacionário para malha aberta e malha fechada
e_ss_open = 10 - y[-1]
e_ss_closed = 10 - y1[-1]

# Exibindo os erros de estado estacionário
print(f"Erro malha aberta: {e_ss_open:.2f}")
print(f"Erro malha fechada: {e_ss_closed:.2f}")
