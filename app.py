x = int(input("Enter a number: "))

# Iterate through the range from 1 to x
for i in range(1, x + 1):
    # Check if number is divisible by 3 and 5
    if i % 3 == 0 and i % 5 == 0:
        # Print the number
        print(i, "is divisible by 3 and 5")
    else:
        print(i, "is not divisible by 3 and 5")