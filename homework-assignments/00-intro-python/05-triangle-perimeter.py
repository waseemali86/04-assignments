# Prompt the user to enter the lengths of each side of a triangle and then calculate and print the perimeter of the triangle 
# (the sum of all of the side lengths).


# ---SOLUTION---

# Prompt the user to enter the lengths of each side of a triangle
side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))


# and then calculate and print the perimeter of the triangle
perimeter = side1 + side2 + side3

print(f"The perimeter of the triangle is {perimeter}.")