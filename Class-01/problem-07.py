# Issue Ref. https://github.com/sharminshanta/data-science/issues/7
# Q7:- Given the first 2 terms of an Arithmetic Series. Find the value of Nth term
# of the series. Assume all inputs are provided by the user.

'''
Formula: an = a1 + (n - 1) * d
a1 is the first term,
a2 is the second term,
d = a2 - a1 is the common difference,
n is the term position,
'''

def findNthTermOfArithmeticSeries(first_term, second_term, n):
    difference = second_term - first_term
    nth_term_value = first_term + (n - 1) * difference
    return nth_term_value

try:
    first_term_value = int(input("Enter the first_term integer: "))
    second_term_value = int(input("Enter the second_term integer: "))
    nth_term = int(input("Enter the nth term value to find it: "))

    if nth_term > 0:
        result = findNthTermOfArithmeticSeries(first_term_value, second_term_value, nth_term)
        print(f"The value of {nth_term}th term is {result}")
    else:
        print("Please, enter the nth term value greater than 0.")
except ValueError:
    print("Please, enter the valid integer.")