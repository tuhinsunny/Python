# Accept a list of numbers from the console
numstr = input("Enter a list of numbers separated by spaces: ")

# Split the input string into a list of values
numlist = numstr.split()

# Convert each value in the list to an integer
numlist = [int(num) for num in numlist]

# Initialize variables to store the maximum and minimum values
maxnum = numlist[0]
minnum = numlist[0]

# Iterate through the list
for num in numlist:
    if num > maxnum:
        maxnum = num
    if num < minnum:
        minnum = num

# Print the results
print("Maximum value:", maxnum)
print("Minimum value:", minnum)