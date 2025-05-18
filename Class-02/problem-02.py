# Issue Ref.: Issue Ref. https://github.com/sharminshanta/data-science/issues/11

'''
Pyramid diamond-style star pattern
Print the following pattern.
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
'''

rows = 5

# Top half with middle row
for i in range(1, rows + 1):
    print("* " * i)

# Bottom half under the middle row
for i in range(rows - 1, 0, -1):
    print("* " * i)
