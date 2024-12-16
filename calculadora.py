# calculadora.py

def calculadora():
    print("Bem-vindo à calculadora!")
    print("Selecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    # Recebe a escolha do usuário
    escolha = input("Digite o número da operação desejada (1/2/3/4): ")

    # Valida a escolha
    if escolha not in ['1', '2', '3', '4']:
        print("Opção inválida! Tente novamente.")
        return

    # Recebe os números do usuário
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Por favor, insira números válidos.")
        return

    # Realiza a operação
    if escolha == '1':
        print(f"O resultado da adição é: {num1 + num2}")
    elif escolha == '2':
        print(f"O resultado da subtração é: {num1 - num2}")
    elif escolha == '3':
        print(f"O resultado da multiplicação é: {num1 * num2}")
    elif escolha == '4':
        if num2 == 0:
            print("Erro! Não é possível dividir por zero.")
        else:
            print(f"O resultado da divisão é: {num1 / num2}")

# Executa a função principal
if __name__ == "__main__":
    calculadora()
