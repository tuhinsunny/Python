tup = ()
n = int(input("Enter the number of elements to insert: "))
print("Enter the elements :")
for i in range(n):
    ele=int(input())
    tup += (ele,)
# Create an empty dictionary to store element frequencies
frequency = {}
for i in tup:
    # Update the frequency of the element in the dictionary
    frequency[i] = frequency.get(i, 0) + 1

# Display the element frequencies
for element, frequency in frequency.items():
    print(f"Element: {element}, Frequency: {frequency}")