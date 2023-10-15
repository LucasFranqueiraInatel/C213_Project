import numpy as np
import control as cnt
import matplotlib.pyplot as plt

# Parâmetros da Função de Transferência da Planta
k = 2.193       # Ganho
tau = 8.95      # Constante de tempo
theta = 1.49    # Atraso de tempo

# Cálculo dos Parâmetros do Controlador PID usando as fórmulas de Cohen-Coon
kp = (1/k)*(tau/theta)*((4/3) + (1/4)*(theta/tau))
ti = theta*((32+6*(theta/tau))/(13+8*(theta/tau)))
td = theta*((4)/(11+2*(theta/tau)))

#ajustes finos
kp = kp - 2.77
ti = ti + 6.57
td = td + 0.174

# Definição da Função de Transferência da Planta
num = np.array([k])
den = np.array([tau, 1])
H = cnt.tf(num, den)

# Aplicação da Aproximação de Pade para lidar com o atraso de tempo
n_pade = 20
(num_pade, den_pade) = cnt.pade(theta, n_pade)
H_pade = cnt.tf(num_pade, den_pade)
Hs = cnt.series(H, H_pade)

# Construção das Funções de Transferência para as partes P, I, e D do Controlador PID
numkp = np.array([kp])
denkp = np.array([1])
numki = np.array([kp])
denki = np.array([ti, 0])
numkd = np.array([kp*td, 0])
denkd = np.array([1])
Hkp = cnt.tf(numkp, denkp)
Hki = cnt.tf(numki, denki)
Hkd = cnt.tf(numkd, denkd)

# Combinação das partes P, I, e D para formar o Controlador PID completo
Hctrl1 = cnt.parallel(Hkp, Hki)
Hctrl = cnt.parallel(Hctrl1, Hkd)

# Série da Planta com o Controlador PID
Hdel = cnt.series(Hs, Hctrl)

# Construção do Sistema de Controle em Malha Fechada
Hcl = cnt.feedback(Hdel, 1)


# Geração e Plotagem das Respostas ao Degrau dos Sistemas
t = np.linspace(0, 30, 100)
(t, y) = cnt.step_response(10*Hcl, t)

plt.plot(t, y, label='Cohen & Coon')
plt.xlabel('t [s]')
plt.ylabel('Amplitude')
plt.grid()
plt.legend()
plt.show()