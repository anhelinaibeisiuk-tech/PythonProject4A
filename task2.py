def print_a_to_b(a, b):
    print(a, end=' ')
    if a < b:
        print_a_to_b(a + 1, b)
    elif a > b:
        print_a_to_b(a - 1, b)

# Зчитування двох чисел
a = int(input())
b = int(input())
print_a_to_b(a, b)