def compound_interest(principal, rate, time, n):
    return principal * ((1 + rate / (n * 100)) ** (n * time))

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the interest rate (in percentage): "))
time = float(input("Enter the time period (in years): "))
n = int(input("Enter the number of times interest is compounded per time period: "))

interest = compound_interest(principal, rate, time, n)
print("Compound Interest:", interest)

