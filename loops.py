# Program to find the sum of all numbers stored in a list

# List of numbers
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]
words = ["lavish", "jain"]
# variable to store the sum
total = 0

for i in range(len(words)):
    print("The word is", words[i])

# iterate over the list
for val in numbers:
    total += val
    if total == 14:
        print("the number is {0}".format(total))

# Output: The sum is 48
print("The sum is", total)