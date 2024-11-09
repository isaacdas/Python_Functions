#####################################  Calculator app

#addition function
def addition(number1,number2):
    return number1 + number2

#subtraction function 
def subtraction(number1,number2):
    return number1 - number2

#multiplication function
def multiplication(number1,number2):
    return number1 * number2


#division function
def division(number1,number2):
    return number1 / number2 if number2 else print("You tried dividing by zero, ending code.", ZeroDivisionError)




#loop for input
while True:
    #user input
    operation_input = input('''\nWhich operation would you like to perform?
a) Addition
b) Subtraction
c) Multiplication
d) Division                   
Enter your choice (Enter [q] to quit):  ''')
    
        #quit statement
    if operation_input.lower() == 'q':
        print("\nThank you for using my program, goodbye.\n")
        break

        #option a
    elif operation_input.lower() == 'a':
        while True: #user input catch
            try:
                #try first number input
                number_input1 = input("\nEnter the first number you would like to use: ")
                #secure int or float 
                if number_input1 == int or float:
                    number_input1 = float(number_input1)
                        #try second number if first number input successful
                    try: 
                        number_input2 = input(f"Enter the second number.\n{number_input1} plus ")
                        #secure second number int or float
                        if number_input2 == int or float:
                            number_input2 = float(number_input2)
                            #calls the addition function
                            number_addition = addition(number_input1, number_input2)
                            print(f"\nAnswer: {number_addition}")
                            break #breaks the loop

                        else:
                            raise ValueError #raises second number value error
                        
                    except ValueError:
                        print("\n\nPlease enter a valid number.")
                    #end second number constraints
                else:
                    raise ValueError #raises a value error if str or bool

            except ValueError:
                print("\n\nPlease enter a valid number.")

                
                
    #option b
    elif operation_input.lower() == 'b':
        while True: #user input catch
            try:
                #try first number input
                number_input1 = input("\nEnter the first number you would like to use: ")
                #secure int or float 
                if number_input1 == int or float:
                    number_input1 = float(number_input1)
                        #try second number if first number input successful
                    try: 
                        number_input2 = input(f"Enter the second number.\n{number_input1} minus ")
                        #secure second number int or float
                        if number_input2 == int or float:
                            number_input2 = float(number_input2)
                            #calls the subtraction function
                            number_subtraction = subtraction(number_input1, number_input2)
                            print(f"\nAnswer: {number_subtraction}")
                            break #breaks the loop

                        else:
                            raise ValueError #raises second number value error
                        
                    except ValueError:
                        print("\n\nPlease enter a valid number.")
                    #end second number constraints
                else:
                    raise ValueError #raises a value error if str or bool

            except ValueError:
                print("\n\nPlease enter a valid number.")



    #option c
    elif operation_input.lower() == 'c':
        while True: #user input catch
            try:
                #try first number input
                number_input1 = input("\nEnter the first number you would like to use: ")
                #secure int or float 
                if number_input1 == int or float:
                    number_input1 = float(number_input1)
                        #try second number if first number input successful
                    try: 
                        number_input2 = input(f"Enter the second number.\n{number_input1} times ")
                        #secure second number int or float
                        if number_input2 == int or float:
                            number_input2 = float(number_input2)

                            #calls the multiplication function
                            number_multiplication = multiplication(number_input1, number_input2)
                            print(f"\nAnswer: {number_multiplication}")
                            break #breaks the loop
                        else:
                            raise ValueError #raises second number value error
                        
                    except ValueError:
                        print("\n\nPlease enter a valid number.")
                    #end second number constraints
                else:
                    raise ValueError #raises a value error if str or bool

            except ValueError:
                print("\n\nPlease enter a valid number.")
    
    #option d
    elif operation_input.lower() == 'd':
        while True: #user input catch
            try:
                #try first number input
                number_input1 = input("\nEnter the first number you would like to use: ")
                #secure int or float 
                if number_input1 == int or float:
                    number_input1 = float(number_input1)
                        #try second number if first number input successful
                    try: 
                        number_input2 = input(f"Enter the second number.\n{number_input1} divided by ")
                            #secure number float
                        if number_input2 == int or float:
                            number_input2 = float(number_input2)
                            
                            #calls the division function
                            number_division = division(number_input1, number_input2)
                            print(f"\nAnswer: {number_division}")
                            break #breaks the loop

                        else:
                            raise ValueError #raises second number value error
                        
                    except ValueError:
                        print("\n\nPlease enter a valid number.")
                    #end second number constraints
                else:
                    raise ValueError #raises a value error if str or bool

            except ValueError:
                print("\n\nPlease enter a valid number.")
    else:
        print("\nPlease make a valid selection (a, b, c or d) before continuing.")
    

