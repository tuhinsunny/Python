#Write a program to get a string from a given string where all occurrences
# of the last character have been changed to ‘*’, except the last character.
str = input("Enter a string: ")
last_char = str[-1]
str = str[:-1].replace(last_char,'*')+last_char
print(str)