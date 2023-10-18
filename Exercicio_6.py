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
kp = kp - 2.0
ti = ti + 6.5
td = td - 0.15

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

# plt.plot(t, y, label='Cohen & Coon Ajustado')
# plt.xlabel('t [s]')
# plt.ylabel('Amplitude')
# plt.grid()
# plt.legend()
# plt.show()

# Cálculo dos Parâmetros do Controlador PID usando as fórmulas CHR 2
kp_chr = (0.95*tau)/(k*theta)
ti_chr = 1.357*tau
td_chr = 0.473*theta

kp_chr -= 0.75
ti_chr -= 3
td_chr -= 0.23

# Construção das Funções de Transferência para as partes P, I, e D usando CHR 2
numkp_chr = np.array([kp_chr])
denkp_chr = np.array([1])
numki_chr = np.array([kp_chr])
denki_chr = np.array([ti_chr, 0])
numkd_chr = np.array([kp_chr*td_chr, 0])
denkd_chr = np.array([1])
Hkp_chr = cnt.tf(numkp_chr, denkp_chr)
Hki_chr = cnt.tf(numki_chr, denki_chr)
Hkd_chr = cnt.tf(numkd_chr, denkd_chr)

# Combinação das partes P, I, e D para formar o Controlador PID completo (CHR 2)
Hctrl1_chr = cnt.parallel(Hkp_chr, Hki_chr)
Hctrl_chr = cnt.parallel(Hctrl1_chr, Hkd_chr)

# Série da Planta com o Controlador PID (CHR 2)
Hdel_chr = cnt.series(Hs, Hctrl_chr)

# Construção do Sistema de Controle em Malha Fechada (CHR 2)
Hcl_chr = cnt.feedback(Hdel_chr, 1)

# Geração e Plotagem das Respostas ao Degrau dos Sistemas
t = np.linspace(0, 30, 100)
(t, y) = cnt.step_response(10*Hcl, t)
(t_chr, y_chr) = cnt.step_response(10*Hcl_chr, t)

plt.plot(t, y, label='Cohen & Coon Ajustado')
plt.plot(t_chr, y_chr, linestyle='dashed', label='CHR 2 Ajustado')
plt.xlabel('t [s]')
plt.ylabel('Amplitude')
plt.title('Comparação: Cohen & Coon vs CHR 2')
plt.grid()
plt.legend()
plt.show()