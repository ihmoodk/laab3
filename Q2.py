user_values = []
for i in range(10):
    while True:
        try:
            value = float(input(f"Enter value {i + 1}: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    user_values.append(value)

largest_number = user_values[0]
for number in user_values:
    if number > largest_number:
        largest_number = number

print(f"The largest number in the list is: {largest_number}")
