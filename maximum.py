def maximum(num1, num2):
    return num1 if num1 > num2 else num2

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

max_num = maximum(num1, num2)
print("Maximum of", num1, "and", num2, "is:", max_num)
