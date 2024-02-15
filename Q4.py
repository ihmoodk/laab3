while True:
    try:
        number = int(input("Enter a number: "))
        break
    except ValueError:
        print("Invalid input. Please enter an integer.")

print(f"\nMultiplication table for {number}:\n")

for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")
