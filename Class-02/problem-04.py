# Issue Ref.: Issue Ref. https://github.com/sharminshanta/data-science/issues/13
'''
Problem 1 - Print the following pattern. Write a program to use for loop to print the following reverse number pattern.
1
2 1
3 2 1
4 3 2 1
5 4 3 2 1
'''

for i in range(1, 6):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()