while True:
    option = input("Enter add or subtract multiply divide quit :  ").lower()
    if option == 'quit':
        break
    elif option == 'add':
        number1 = float(input("Enter first number: "))
        number2 = float(input("Enter second number: "))
        print(number1 + number2)
    elif option == 'subtract':
        number1 = float(input("Enter first number: "))
        number2 = float(input("Enter second number: "))
        print(number1 - number2)
    elif option == 'multiply':
        number1 = float(input("Enter first number: "))
        number2 = float(input("Enter second number: "))
        print(number1 * number2)
    elif option == 'divide':
        number1 = float(input("Enter first number: "))
        number2 = float(input("Enter second number: "))
        print(number1 / number2)
print("EXIT")
