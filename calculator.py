
while True:
    option = input("Enter add or subtract multiply divide percentage quit :  ")
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
    elif option == 'percentage':
        number = float(input("Enter first number: "))
        totalnumber = float(input("Enter total number: "))
        p= ((number/100)*totalnumber)
        print("The percentage is= ",p,"%")
    else : 
        print("Invalid Input")
print("EXIT")
