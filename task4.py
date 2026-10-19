def sum_digits(n):
    if n < 10:
        return n
    return (n % 10) + sum_digits(n // 10)

# Зчитування та виклик
n = int(input())
print(sum_digits(n))