def print_digits_reverse(n):
    print(n % 10, end=' ')
    if n >= 10:
        print_digits_reverse(n // 10)

# Зчитування та виклик
n = int(input())
print_digits_reverse(n)