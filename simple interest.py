def simple_interest(p,r,t):
    return (p*r*t)/100
p=float(input("enter the principle amount:"))
r=float(input("enter the rate of interest(in percentage):"))
t=float(input("enter the time(in years):"))
interest=simple_interest(p,r,t)
print("Simple interest:",interest)