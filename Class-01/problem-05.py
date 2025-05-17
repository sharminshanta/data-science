# # Issue Ref.: https://github.com/sharminshanta/data-science/issues/5
'''
Q5: Write a program that will tell the number of dogs and chicken are
there when the user will provide the value of total heads and legs.

Solution:
Let dogs = x, chickens = y
so, dogs + chickens = x + y = 4(user input)
x = 4 - y(heads - chickens) // dogs' value
then, 2x + 4y = 12 // total legs count. Since we know that chicken has 2 and dog has 4 legs
= 2(4 - y) + 4y = 12
= 8 - 2y + 4y = 12
= 8 + 2y = 12
= 2y = 12 - 4
= 2y = 8
= y = 8/4 = 2
so, chicken = 2
so, dog = 4 - 2 = 2
'''

def findAnimal(heads, legs):
    for chicken in range(0, heads):
        dog = heads - chicken
        total_legs = (4 * dog) + (2 * chicken)

        if (total_legs == legs):
            return chicken, dog

    return None, None  # No solution


# Get input from the user
try:
    heads = int(input("Enter the total number of heads: "))
    legs = int(input("Enter the total number of legs: "))

    chickens, dogs = findAnimal(heads, legs)

    if chickens is not None:
        print(f"There are {chickens} chickens and {dogs} dogs.")
    else:
        print("No valid solution exists with the given number of heads and legs.")
except ValueError:
    print("Please enter valid integer numbers.")