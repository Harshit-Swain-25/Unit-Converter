def c_to_f(c):
    return (c * 9/5) + 32

def f_to_c(f):
    return (f - 32) * 5/9

def km_to_miles(km):
    return km * 0.621371

def miles_to_km(mi):
    return mi / 0.621371

def kg_to_lbs(kg):
    return kg * 2.2046226218

def lbs_to_kg(lbs):
    return lbs / 2.2046226218

def m_to_feet(m):
    return m * 3.28084

def feet_to_m(m):
    return m / 3.28084

def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def main():
    menu = """
Unit Converter
1) Celsius -> Fahrenheit
2) Fahrenheit -> Celsius
3) Kilometers -> Miles
4) Miles -> Kilometers
5) Kilograms -> Pounds
6) Pounds -> Kilograms
7) Meters -> Feet
8) Feet -> Meters
9) Exit
"""
    while True:
        print(menu)
        choice = input("Choose (1-9): ").strip()
        if choice == '9':
            print("Goodbye!")
            break

        if choice == '1':
            v = get_float("Celsius: ")
            print(f"{v} °C = {c_to_f(v):.2f} °F\n")
        elif choice == '2':
            v = get_float("Fahrenheit: ")
            print(f"{v} °F = {f_to_c(v):.2f} °C\n")
        elif choice == '3':
            v = get_float("Kilometers: ")
            print(f"{v} km = {km_to_miles(v):.4f} miles\n")
        elif choice == '4':
            v = get_float("Miles: ")
            print(f"{v} miles = {miles_to_km(v):.4f} km\n")
        elif choice == '5':
            v = get_float("Kilograms: ")
            print(f"{v} kg = {kg_to_lbs(v):.4f} lbs\n")
        elif choice == '6':
            v = get_float("Pounds: ")
            print(f"{v} lbs = {lbs_to_kg(v):.4f} kg\n")
        elif choice == '7':
            v = get_float("Meters: ")
            print(f"{v} m = {m_to_feet(v):.4f} feet\n")
        elif choice == '8':
            v = get_float("Feet: ")
            print(f"{v} feet = {feet_to_m(v):.4f} m\n")
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
