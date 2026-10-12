import random

x1 = 0
y1 = 0
x2 = 4
y2 = 4

print(f"Point 1: ({x1}, {y1})")
print(f"Point 2: ({x2}, {y2})")
print(f"Area of rectangle: {abs(x2 - x1) * abs(y2 - y1)}")
print("What is your possition? (x)")
input_position_x = input().strip().split(',')
print("What is your possition? (y)")
input_position_y = input().strip().split(',')
try:
    x, y = int(input_position_x[0]), int(input_position_y[0])
    if x1 <= x <= x2 and y1 <= y <= y2:
        print("You are inside the rectangle.")
        if x == x1 and y == y1:
            print("You are on the bottom left corner of the rectangle.")
        elif x == x2 and y == y1:
            print("You are on the bottom right corner of the rectangle.")
        elif x == x1 and y == y2:
            print("You are on the top left corner of the rectangle.")
        elif x == x2 and y == y2:
            print("You are on the top right corner of the rectangle.")
        elif  x == x1 and y >= y1 and y<= y2:
            print("You are on the left edge of the rectangle.")
        elif x == x2 and y1 <= y <= y2:
            print("You are on the right edge of the rectangle.")
        elif y == y1 and x1 <= x <= x2:
            print("You are on the bottom edge of the rectangle.")
        elif y == y2 and x1 <= x <= x2:
            print("You are on the top edge of the rectangle.")
    else:
        print("You are outside the rectangle.")
except (ValueError, IndexError):
    print("Invalid input. Please enter two integers separated by a comma.")