# Lista para representar o estado das cadeiras (1 = disponível, 0 = ocupada)
cadeiras = [1 for _ in range(10)]
# Lista para contar quantas vezes uma cadeira foi reservada
contadores = [0 for _ in range(10)]

def mostrar_reservas():
    """Exibe a situação atual das cadeiras no cinema."""
    for i in range(10):
        if cadeiras[i] == 0:
            print(f"[B{i+1:02d}]", end="")
        else:
            print("[--]", end="")
    print("\n" + "-" * 50)

def fazer_reserva():
    """Executa o processo de reserva de assento."""
    while True:
        mostrar_reservas()
        assento = input("Reservar a cadeira (ex: B1 a B10): ").strip().upper()

        # Verifica se o formato está correto e dentro do intervalo
        if assento.startswith("B") and assento[1:].isdigit():
            num = int(assento[1:])
            if 1 <= num <= 10:
                idx = num - 1
                contadores[idx] += 1
                if cadeiras[idx] == 0:
                    print("ERRO: Lugar Ocupado!")
                    contadores[idx] = 1  # mantém contador apenas como histórico
                else:
                    cadeiras[idx] = 0
                break
        print("ERRO: Digite um valor correto (B1 a B10).")

def menu():
    """Menu principal do sistema."""
    while True:
        print("\n=== Menu de Reservas ===")
        print("1. Fazer reservas")
        print("2. Ver reservas")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            while True:
                fazer_reserva()
                continuar = input("Deseja reservar outro banco? (S/N): ").strip().upper()
                if continuar not in ("S", "N"):
                    while continuar not in ("S", "N"):
                        continuar = input("ERRO: Digite um valor correto (S/N): ").strip().upper()
                if continuar == "N":
                    break
        elif opcao == "2":
            mostrar_reservas()
        elif opcao == "3":
            print("Saindo do sistema. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executa o menu principal
menu()
