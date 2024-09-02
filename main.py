def is_fibonacci(n):
    # Função para verificar se um número é um número de Fibonacci
    def is_perfect_square(x):
        s = int(x**0.5)
        return s*s == x

    # Um número é um número de Fibonacci se e somente se um (5*n^2 + 4) ou (5*n^2 - 4) é um quadrado perfeito
    return is_perfect_square(5*n*n + 4) or is_perfect_square(5*n*n - 4)

def main():
    try:
        num = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))
        if num < 0:
            print("Por favor, insira um número não negativo.")
            return

        if is_fibonacci(num):
            print(f"O número {num} pertence à sequência de Fibonacci.")
        else:
            print(f"O número {num} não pertence à sequência de Fibonacci.")
    except ValueError:
        print("Entrada inválida! Por favor, insira um número inteiro.")

if __name__ == "__main__":
    main()
