# Issue Ref. https://github.com/sharminshanta/data-science/issues/4
# Q4: Write a program to find the simple interest when the value of principle,rate
# of interest and time period is provided by the user.

capital = float(input("Enter the value of capital: "))
interest = float(input("Enter the rate of interest (%): "))
time = int(input("Enter the duration in years: "))

# We know that, the simple interest is (Capital * Interest * Time) /  100
simple_interest = (capital * interest * time) / 100
print(simple_interest)
