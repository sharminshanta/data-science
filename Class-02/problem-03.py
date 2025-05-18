# Issue Ref.: Issue Ref. https://github.com/sharminshanta/data-science/issues/12

'''
Write a program to pring the following pattern.
    *
  * * *
* * * * *
'''

rows = 3

for i in range(1, rows + 1):
    # Print spaces
    print("  " * (rows - i), end="")  # Two spaces per level

    # Print stars
    print("* " * (2 * i - 1))