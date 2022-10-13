# This program would print a triangle star pyramid
n = int(input("Height: "))

# This variable would print spaces before the stars of the pyramid in each row.
k = n - 1
for i in range(n):
    # This loop makes rows
    
    for j in range(0, k):
        # This loop prints spaces before the stars
        print(end=" ")
    
    # Decreasing the space variable for the next row.
    k = k - 1

    for j in range(i + 1):
        # This loop prints the stars. To make a pyramid shape, we have to print a space after the star in each row.
        print("*", end=" ")
    
    # Printing a new line character to make a new row.
    print("\r")