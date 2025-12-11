def c_to_f(c):
    return (c * 9/5) + 32

def f_to_c(f):
    return (f - 32) * 5/9

def c_to_k(c):
    return c + 273.15

def k_to_c(k):
    return k - 273.15

def f_to_k(f):
    return c_to_k(f_to_c(f))

def k_to_f(k):
    return c_to_f(k_to_c(k))


while True:
    print("\n---- Temperature Converter ----")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    print("7. Exit")

    choice = int(input("Enter your choice (1-7): "))

    if choice == 7:
        print("Exiting Temperature Converter…")
        break

    temp = float(input("Enter temperature value: "))

    if choice == 1:
        print("Result:", c_to_f(temp), "°F")
    elif choice == 2:
        print("Result:", f_to_c(temp), "°C")
    elif choice == 3:
        print("Result:", c_to_k(temp), "K")
    elif choice == 4:
        print("Result:", k_to_c(temp), "°C")
    elif choice == 5:
        print("Result:", f_to_k(temp), "K")
    elif choice == 6:
        print("Result:", k_to_f(temp), "°F")
    else:
        print("Invalid choice!")
