import numpy as np
import control as cnt
import matplotlib.pyplot as plt

def pid_calculator(theta, T, K, setpoint):
    # Cálculos dos parâmetros PID pelo método de CHR
    kp_chr = 0.95 * T / (K * theta)
    ti_chr = 1.357 * T
    td_chr = 0.473 * theta

    # Cálculos dos parâmetros PID pelo método de Cohen-Coon
    kp = ((1 / K) * (T / theta)) * ((4 / 3) + ((1 / 4) * (theta / T)))
    ti = theta * ((32 + (6 * (theta / T))) / (13 + (8 * (theta / T))))
    td = theta * (4 / (11 + 2 * (theta / T)))

    # Construindo as Funções de Transferência e a resposta ao degrau

    # Planta
    num = np.array([K])
    den = np.array([T, 1])
    H = cnt.tf(num, den)

    # Aproximação de Pade para lidar com o atraso de tempo
    n_pade = 20
    (num_pade, den_pade) = cnt.pade(theta, n_pade)
    H_pade = cnt.tf(num_pade, den_pade)
    Hs = cnt.series(H, H_pade)

    # Controlador Cohen-Coon
    Hkp = cnt.tf([kp], [1])
    Hki = cnt.tf([kp], [ti, 0])
    Hkd = cnt.tf([kp*td, 0], [1])
    Hctrl1 = cnt.parallel(Hkp, Hki)
    Hctrl = cnt.parallel(Hctrl1, Hkd)
    Hdel = cnt.series(Hs, Hctrl)
    Hcl = cnt.feedback(Hdel, 1)

    # Controlador CHR
    Hkp_chr = cnt.tf([kp_chr], [1])
    Hki_chr = cnt.tf([kp_chr], [ti_chr, 0])
    Hkd_chr = cnt.tf([kp_chr*td_chr, 0], [1])
    Hctrl1_chr = cnt.parallel(Hkp_chr, Hki_chr)
    Hctrl_chr = cnt.parallel(Hctrl1_chr, Hkd_chr)
    Hdel_chr = cnt.series(Hs, Hctrl_chr)
    Hcl_chr = cnt.feedback(Hdel_chr, 1)

    # Plotagem das Respostas ao Degrau dos Sistemas
    t = np.linspace(0, 30, 100)
    (t, y) = cnt.step_response(10*Hcl, t)
    (t_chr, y_chr) = cnt.step_response(10*Hcl_chr, t)

    plt.plot(t, y, label='Cohen & Coon')
    plt.plot(t_chr, y_chr, linestyle='dashed', label='CHR 2')
    plt.xlabel('t [s]')
    plt.ylabel('Amplitude')
    plt.title('Comparação: Cohen & Coon vs CHR 2')
    plt.grid()
    plt.legend()
    plt.show()

def main():
    print("Calculadora PID e Comparação de Respostas")

    try:
        theta = float(input("Digite o valor de Theta (θ): "))
        T = float(input("Digite o valor de T: "))
        K = float(input("Digite o valor de K: "))
        setpoint = float(input("Digite o valor do Setpoint: "))

        pid_calculator(theta, T, K, setpoint)

    except ValueError:
        print("\nPor favor, insira um número válido.")

if __name__ == "__main__":
    main()
