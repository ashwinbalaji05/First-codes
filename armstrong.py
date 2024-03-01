def is_armstrong(num):
    return num == sum(int(digit) ** len(str(num)) for digit in str(num))

num = int(input("Enter a number: "))
print(num, "is an Armstrong number") if is_armstrong(num) else print(num, "is not an Armstrong number")
