def addition():
    option = input("Addition: press 1 to continue, 0 to exit")

    while option != "1" and option != "0" :
        option = input("Choose a valid option: 1 to continue, 0 to exit")

    while option == "1" :
        try :
            input_number = float(input("Enter the number you would like to add to"))
            result = input_number

            input_number = float(input("Enter the number you would like to add"))
            result += input_number

            print(f"result = {result}")
        except ValueError as e :
            print(f"error {e}")
            result = None

        option = input("Press 1 to continue, press any other key to quit")

def subtraction():

    option = input("Subtraction: press 1 to continue, 0 to exit")

    while option != "1" and option != "0":
        option = input("Choose a valid option: 1 to continue, 0 to exit")

    while option == "1":
        try:
            input_number = float(input("Enter the number you would like to subtract from"))
            result = input_number

            input_number = float(input("Enter the number you would like to subtract"))
            result -= input_number

            print(f"result = {result}")
        except ValueError as e:
            print(f"error {e}")
            result = None

        option = input("Press 1 to continue, press any other key to quit")

def division():

    option = input("Division: press 1 to continue, 0 to exit")

    while option != "1" and option != "0" :
        option = input("Choose a valid option: 1 to continue, 0 to exit")

    while option == "1" :
        try :
            input_number = float(input("Enter the number you would like to divide"))
            result = input_number

            input_number = float(input("Enter the number you would like to divide by"))
            result = result / input_number

            print(f"result = {result}")
        except ValueError as e :
            print(f"error {e}")

        option = input("Press 1 to continue, press any other key to quit")

def multiplication():

    option = input("Multiplication: press 1 to continue, 0 to exit")

    while option != "1" and option != "0" :
        option = input("Choose a valid option: 1 to continue, 0 to exit")

    while option == "1" :
        try :
            input_number = float(input("Enter the number you would like to multiply"))
            result = input_number
            
            input_number = float(input("Enter the number you would like to multiply by"))
            result = result * input_number

            print(f"result = {result}")
        except ValueError as e :
            print(f"error {e}")
            result = None

        option = input("Press 1 to continue, press any other key to quit")

def main():
    while True:
        operation = input("""Choose an option: 
        1. Addition 
        2. Subtraction
        3. Multiplication
        4. Division
        5. Exit
                            """)

        if operation == "1":
            addition()

        elif operation == "2":
            subtraction()

        elif operation == "3":
            multiplication()

        elif operation == "4":
            division()

        elif operation == "5":
            break

        else:
            print("You have chosen an invalid option, please try again")

if __name__ == '__main__': main()
