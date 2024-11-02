def right_angled_triangle(height):
    for place in range(height):
        formula = place + 1
        for star in range(formula):
            print("*", end="")
        print()

def square_with_hollow_center(height):
    for place in range(1,height + 1):
        if place == 1 or place == height:
            for star in range(height):
                print("*", end="")
        else:
            for star in range(1, height + 1):
                if star == 1 or star == height:
                    print("*", end="")
                else:
                    print(" ", end="")
        print()

def square_with_hollow_diamond(height):
    middle = height // 2
    #top part
    for row in range(middle + 1):
        for col in range(height):
            if col == middle - row or col == middle + row:
                print("*", end="")
            else:
                print(" ", end="")
        print()
    #lower part
    for row in range(middle - 1, -1, -1):
        for col in range(height):
            if col == middle - row or col == middle + row:
                print("*", end="")
            else:
                print(" ", end="")
        print()

def diamond(height):
    for i in range(1, height + 1):
        i = i - (height // 2 + 1)
        if i < 0:
            i = -i
        print(" " * i + "*" * (height - i * 2) + " " * i)

def left_angled_triangle(height):
    for places in range(height):
        space = places
        places = height - places
        if places < 0:
            places = -places
        print("*" * places + " " * space)

def pyramid(height):
    for row in range(height):
        spaces = height - row - 1
        stars = 2 * row + 1
        print(" " * spaces + "*" * stars + " " * spaces)

def right_angled_triangle_with_numbers(height):
    for place in range(height):
        formula = place + 1
        for number in range(1, formula + 1):
            print(number, end="")
        print()

def inverted_pyramid(height):
    for row in range(height, 0, -1):
        spaces = height - row + 1
        stars = 2 * row - 1
        print(" " * spaces + "*" * stars + " " * spaces)

def star_dash_square(height):
    for row in range(1,height + 1):
        if row % 2 == 0:
            for i in range(1, height + 1):
                if i % 2 == 0:
                    print("*", end="")
                else:
                    print("_", end="")
        else:
            for j in range(1, height + 1):
                if j % 2 == 0:
                    print("_", end="")
                else:
                    print("*", end="")
        print()

print("Choose a pattern to print:")
print("1. Right-angled Triangle")
print("2. Square with Hollow Center")
print("3. Diamond with a hole in the middle")
print("4. Diamond")
print("5. Left-angled Triangle")
print("6. Pyramid")
print("7. Right-angled Triangle with Numbers")
print("8. Inverted Pyramid")
print("9. Alternating Star-Dash Square")

choice = input("Enter the number of your choice (1-9): ")

if choice == "1":
    print("You have chosen: Right-angled Triangle!")
    height = int(input("Please select the height of your triangle: "))
    right_angled_triangle(height)

elif choice == "2":
    print("You have chosen: Square with Hollow Center!")
    height = int(input("Please select the height of your square: "))
    square_with_hollow_center(height)

elif choice == "3":
    print("You have chosen: Diamond with a hole in the middle!")
    height = int(input("Please select the height of your hollow diamond (must be odd): "))
    while height % 2 == 0:
        print("Please enter an odd number.")
        height = int(input("Please select the height of your hollow diamond (must be odd): "))
    square_with_hollow_diamond(height)

elif choice == "4":
    print("You have chosen: Diamond!")
    height = int(input("Please select the height of your diamond (must be odd): "))
    while height % 2 == 0:
        print("Please enter an odd number.")
        height = int(input("Please select the height of your diamond (must be odd): "))
    diamond(height)

elif choice == "5":
    print("You have chosen: Left-angled Triangle!")
    height = int(input("Please select the height of your triangle: "))
    left_angled_triangle(height)

elif choice == "6":
    print("You have chosen: Pyramid!")
    height = int(input("Please select the height of your pyramid (must be odd): "))
    while height % 2 == 0:
        print("Please enter an odd number.")
        height = int(input("Please select the height of your pyramid (must be odd): "))
    pyramid(height)

elif choice == "7":
    print("You have chosen: Right-angled Triangle with Numbers!")
    height = int(input("Please select the height of your triangle: "))
    right_angled_triangle_with_numbers(height)

elif choice == "8":
    print("You have chosen: Inverted Pyramid!")
    height = int(input("Please select the height of your inverted pyramid (must be odd): "))
    while height % 2 == 0:
        print("Please enter an odd number.")
        height = int(input("Please select the height of your inverted pyramid (must be odd): "))
    inverted_pyramid(height)

elif choice == "9":
    print("You have chosen: Alternating Star-Dash Square!")
    height = int(input("Please select the height of your star-dash square: "))
    star_dash_square(height)

else:
    print("Invalid choice. Please enter a number between 1 and 9.")



