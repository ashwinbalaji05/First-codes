def fibonacci(n):
    return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)

n = int(input("Enter the value of n: "))
result = fibonacci(n)
print("The", n, "th Fibonacci number is:", result)

