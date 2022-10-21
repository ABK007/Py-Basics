#Code for calculator
from logo import logo

#Add
def add(n1, n2):
    return n1 + n2

#Subtract
def subtract(n1, n2):
    return n1 - n2

#Multiply
def multiply(n1, n2):
    return n1 * n2

#Divde
def divide(n1, n2):
    return n1 / n2

def calculator (): #Defined the calculator function
    
    print(logo) #prints calculator logo

    # Created dictionary to with keys as operation symbols and functions as values
    operations = { "+": add,
                  "-":subtract,
                  "*":multiply,
                  "/": divide }

    # Asking for first number
    num1 = float(input("What's the first number?: "))


    for symbol in operations:
        print(symbol)



    while True: # Created while loop to continuously execute the following code
        operation_symbol = input("Pick an operation : ")
        num2 = float(input("What's the next number?: "))

        Calculation_function = operations[operation_symbol]
        answer = Calculation_function(num1, num2) # passing value to the function depending on the operation selected

        print(f"{num1} {operation_symbol} {num2} = {answer}")


        resume =  input(f"Type 'y' to continue calculating with {answer} or type 'n' to start new calculation: ").lower()

        if resume == "y":
            num1 = answer

        elif resume == "n":
            calculator() #Added calculator function for recursion


calculator()