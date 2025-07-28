def km_to_miles(km):
    return km * 0.621371

def miles_to_km(miles):
    return miles / 0.621371

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

# Example usage:
print("Unit Converter")
print("1. Km to Miles")
print("2. Miles to Km")
print("3. Celsius to Fahrenheit")
print("4. Fahrenheit to Celsius")

choice = input("Enter your choice (1-4): ")

if choice == "1":
    km = float(input("Enter kilometers: "))
    print(f"{km} km = {km_to_miles(km):.2f} miles")
elif choice == "2":
    miles = float(input("Enter miles: "))
    print(f"{miles} miles = {miles_to_km(miles):.2f} km")
elif choice == "3":
    c = float(input("Enter Celsius: "))
    print(f"{c}°C = {celsius_to_fahrenheit(c):.2f}°F")
elif choice == "4":
    f = float(input("Enter Fahrenheit: "))
    print(f"{f}°F = {fahrenheit_to_celsius(f):.2f}°C")
else:
    print("Invalid choice.")
