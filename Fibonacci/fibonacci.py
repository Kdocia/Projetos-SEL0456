class Fibonacci:
    def __init__(self, n):
        self.n = n
        self.sequence = []

    def generate_sequence(self):
        a, b = 0, 1
        for _ in range(self.n):
            self.sequence.append(a)
            a, b = b, a + b

    def get_sequence(self):
        return self.sequence

    def display_sequence(self):
        print("Sequência de Fibonacci:")
        for number in self.sequence:
            print(number, end=" ")
        print()


# Crie uma instância da classe Fibonacci para gerar a sequência
n = int(input("Quantos números da sequência de Fibonacci você deseja gerar? "))
fib = Fibonacci(n)

# Gere a sequência de Fibonacci
fib.generate_sequence()

# Exiba a sequência gerada
fib.display_sequence()
