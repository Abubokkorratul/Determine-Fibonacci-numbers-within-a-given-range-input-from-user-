low = int(input("Enter the lower bound of the range: "))
high = int(input("Enter the upper bound of the range: "))
a, b = 0, 1
print("Fibonacci numbers in the range:")
while a <= high:
    if a >= low:
        print(a, end=" ")
    a, b = b, a + b
