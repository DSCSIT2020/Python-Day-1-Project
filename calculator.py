
while True:
    print("\nChoose Operation:\n[1] Add\n[2] Subtract\n[3] Multiply\n[4] Divide\n[5] Exponent\n[6] Average\n[q] Quit")
    option = input(">>>")
    if option == 'q':
        print("Thanks for using me...")
        break
    elif option == '1':
        number1 = float(input("Enter first number: "))
        number2 = float(input("Enter second number: "))
        print(number1 + number2)
    elif option == '2':
        number1 = float(input("Enter first number: "))
        number2 = float(input("Enter second number: "))
        print(number1 - number2)
    elif option == '3':
        number1 = float(input("Enter first number: "))
        number2 = float(input("Enter second number: "))
        print(number1 * number2)
    elif option == '4':
        number1 = float(input("Enter first number: "))
        number2 = float(input("Enter second number: "))
        print(number1 / number2)
    elif option == '5':
        number1 = float(input("Enter a number: "))
        number2 = float(input("Enter the power: "))
        print(number1 ** number2)
    elif option == '6':
        number1 = float(input("Enter first number: "))
        number2 = float(input("Enter second number: "))
        print((number1+number2)/2)
    else : 
        print("Invalid Input")
print("EXIT")