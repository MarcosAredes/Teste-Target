# sequência de Fibonacci
def is_fibonacci(num):
    a, b = 0, 1
    while b < num:
        a, b = b, a + b
    return b == num or a == num


num = int(input("Informe um número: "))

if is_fibonacci(num):
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} NÃO pertence à sequência de Fibonacci.")
