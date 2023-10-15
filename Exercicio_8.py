def pid_calculator(theta, T, K, setpoint):
    # Cálculos dos parâmetros PID
    kp_chr = 0.95 * T / (K * theta)
    ti_chr = 1.357 * T
    td_chr = 0.473 * theta

    kp = ((1 / K) * (T / theta)) * ((4 / 3) + ((1 / 4) * (theta / T)))
    ti = theta * ((32 + (6 * (theta / T))) / (13 + (8 * (theta / T))))
    td = theta * (4 / (11 + 2 * (theta / T)))

    print(f"\nResultados dos cálculos PID:")
    print(f"{'Método':<25} {'Kp/Kc':<15} {'Ki/Ti':<15} {'Kd/Td':<15}")
    print(f"{'-' * 60}")
    print(f"{'PID do CHR':<25} {kp_chr:<15.5f} {ti_chr:<15.5f} {td_chr:<15.5f}")
    print(f"{'PID do Cohen-Coon':<25} {kp:<15.5f} {ti:<15.5f} {td:<15.5f}")


def main():
    print("Calculadora PID")

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
