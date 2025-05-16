# Issue Ref.: https://github.com/sharminshanta/data-science/issues/1
# Q1 :- Print the given strings as per stated format.
'''
Given strings:
"Machine" "Learning" "With Python and R" "Program" "By" "Datasolution360"
Output:
Machine-Learning-With Python and R-Program-Conducted-By-Datasolution360
'''


str1 = "Machine"
str2 = "Learning"
str3 = "With Python and R"
str4 = "Program"
str5 = "By"
str6 = "Datasolution360"

str7 = (f"{str1}-{str2}-{str3}-{str4}-Conducted-{str5}-{str6}")
print(str7)