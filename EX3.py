def print_diamond(n):
    if n % 2 == 0:
        return "Please provide an odd integer."
    for i in range(n // 2 + 1):
        print(" " * (n // 2 - i) + "*" * (2 * i + 1))
    for i in range(n // 2 - 1, -1, -1):
        print(" " * (n // 2 - i) + "*" * (2 * i + 1))
print_diamond(5)