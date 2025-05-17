# Issue Ref.: https://github.com/sharminshanta/data-science/issues/9

'''
Problem: Given the height, width and breadth of a milk tank, you have to
find out how many glasses of milk can be obtained? Assume all the
inputs are provided by the user.
Input: Dimensions of the milk tank H = 20cm, L = 20cm, B = 20cm Dimensions of the glass h = 3cm, r = 1cm

Solution:
We know that,
Area is 2D capacity: Length * Width
Volume is 3D Capacity: height * width * breadth
Volume of milk tank = height * width * breadth
Volume of mil glass = height * length * breadth
Then, volume of milk tank / volume of milk glass = number of Glass
'''
def findNumberOfGlass():
    try:
        # Input tank dimensions (in cm)
        print("Enter the milk tank dimensions:")
        tank_h = int(input("Enter the height of milk tank: "))
        tank_w = int(input("Enter the width of milk tank: "))
        tank_b = int(input("Enter the breadth of milk tank: "))

        # Input glass dimensions (in cm)
        print("Enter the glass dimensions:")
        glass_h = int(input("Enter the height of milk glass: "))
        glass_w = int(input("Enter the width of milk glass: "))
        glass_b = int(input("Enter the breadth of milk glass: "))

        volume_of_tank = tank_h * tank_w * tank_b
        volume_of_glass = glass_h * glass_w * glass_b

        number_of_glass = volume_of_tank // volume_of_glass
        print(f"The required number of glass is {number_of_glass}.")
    except ValueError:
        print("Please, enter the valid integer.")

print(findNumberOfGlass())