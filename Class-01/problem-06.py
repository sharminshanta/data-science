# Issue Ref.: https://github.com/sharminshanta/data-science/issues/6
#Q6: Write a program to find the sum of squares of first n natural numbers where n will be provided by the user.

def findSumofSquare(number):
    sum = 0
    for i in range(1, number + 1):
        sum += i * i

    return sum

try:
    number = int(input("Enter the number: "))

    if number > 0:
        result = findSumofSquare(number)
        print(f"The sum of squares of first {number} natural number is: {result}")
    else:
        print("Please, enter the number greater than than 0")
except ValueError:
    print("Please, enter the valid integer.")
