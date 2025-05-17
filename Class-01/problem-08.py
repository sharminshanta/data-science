# Issue Ref. https://github.com/sharminshanta/data-science/issues/8
# Q8:- Given 2 fractions, find the sum of those 2 fractions. Take the
# numerator and denominator values of the fractions from the user.

'''
How the Euclidean Algorithm Works to find GCD(Greatest Common Divisor):
Steps:
Given two numbers a and b, where a > b.
Divide a by b, and get the remainder r.
Replace a with b and b with r.
Repeat until r becomes 0.
The last non-zero remainder is the GCD.
'''

# Find Greatest Common Divisor
def findGCD(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

# Find Lest Common Multiplier
def findLCM(a, b):
    product = a * b
    LCM = product / findGCD(a, b)

    return LCM

# Addition of Fraction
def addFraction(n1, d1, n2, d2):
    LCM = findLCM(d1, d2)
    # print(LCM)
    # exit()
    result = ((LCM / d1) * n1) + ((LCM / d2) * n2)
    result = result / LCM

    return result


# numerator1 = int(input("Enter first numerator: "))
# denominator1 = int(input("Enter first denominator: "))
# numerator2 = int(input("Enter second numerator: "))
# denominator2 = int(input("Enter second denominator: "))
# result = addFraction(numerator1, denominator1, numerator2, denominator2)
# print(float("{:.3f}".format(result)))

try:
    print("Enter the first fraction:")
    numerator1 = int(input("Enter first numerator: "))
    denominator1 = int(input("Enter first denominator: "))

    print("Enter the second fraction:")
    numerator2 = int(input("Enter second numerator: "))
    denominator2 = int(input("Enter second denominator: "))

    if denominator1 == 0 or denominator2 == 0:
        print("Denominator cannot be zero.")
    else:
        result = addFraction(numerator1, denominator1, numerator2, denominator2)
        print(f"The sum of the fractions is: {float("{:.3f}".format(result))}")
except ValueError:
    print("Invalid input! Please enter integers only.")