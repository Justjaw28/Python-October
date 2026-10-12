import random

x1 = random.randint(0, 1)
y1 = random.randint(0, 1)
x2 = random.randint(2, 4)
y2 = random.randint(2, 4)

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
    else:
        print("You are outside the rectangle.")
except (ValueError, IndexError):
    print("Invalid input. Please enter two integers separated by a comma.")