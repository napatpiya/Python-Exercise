print("Please select convertor")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
x = int(input("\nSelect (1,2): "))

if x == 1:
    c = float(input("\nCelsius:"))
    fahrenheit = ((9 / 5) * c) + 32

    print("{0:.2f}".format(c) ,"Celsius is" , "{0:.2f}".format(fahrenheit), "Fahrenheit")
elif x == 2:
    f = float(input("\nFahrenheit:"))
    celsius = ((5 / 9) * f) - 32

    print("{0:.2f}".format(f) ,"Fahrenheit is" , "{0:.2f}".format(celsius), "Celsius")
else:
    print("Wrong Input!!")