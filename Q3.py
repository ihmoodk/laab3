def celsius_to_fahrenheit(celsius):
    return (9/5) * celsius + 32

while True:
    try:
        celsius_temperature = float(input("Enter Celsius temperature: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

fahrenheit_temperature = celsius_to_fahrenheit(celsius_temperature)

print(f"{celsius_temperature} degrees Celsius is equivalent to {fahrenheit_temperature:.2f} degrees Fahrenheit.")
