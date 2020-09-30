print("Simple Calculator")
print("1.Add")
print("2.Substract")
print("3.Multiply")
print("4.Divide")
print("5.Square")
print("6.Power")
print("7.Square Root")
print("8.Quit")
while True:
    option = input("Enter add or subtract multiply divide quit :  ")
    if option == 8:
        break
    elif option == 1:
        number1 = float(input("Enter first number: "))
        number2 = float(input("Enter second number: "))
        print(number1 + number2)
    elif option == 2:
        number1 = float(input("Enter first number: "))
        number2 = float(input("Enter second number: "))
        print(number1 - number2)
    elif option == 3:
        number1 = float(input("Enter first number: "))
        number2 = float(input("Enter second number: "))
        print(number1 * number2)
    elif option == 4:
        number1 = float(input("Enter first number: "))
        number2 = float(input("Enter second number: "))
        print(number1 / number2)
    elif option == 5:
        number1 = float(input("Enter a number: "))
        print(number1**2)
    elif option == 6:
        number1 = float(input("Enter the number to find its value: "))
        number2 = float(input("Enter a value of power: "))
        print(number1 ** number2)
    elif option == 7:
        number1 = float(input("Enter a number: "))
        print(number1 ** 0.5)
    else : 
        print("Invalid Input")
print("EXIT")