def menu():
        
        a = float(input("Choose first number: "))
        b = float(input("Choose second number: "))

        print("""
Choose an operation:
1. Addition
2. Subtraction
3. Multiplication
4. Exponentiation
5. Division
6. Division with remainder
""")

        

        op = int(input("Choose operation number: "))
        return a, b, op

def calculate():
        a, b, op = menu()

        if op == 1:
                print("Sum: {} + {} = {}".format(a,b,a+b))
        elif op == 2:
                print("Difference: {} - {} = {}".format(a,b,a-b))
        elif op == 3:
                print("Product: {} * {} = {}".format(a,b,a*b))
        elif op == 4:
                print("Power: {}^{} = {}".format(a,b,a**b))
        elif op == 5:
                try:
                        print("Quotient: {} / {} = {}".format(a,b,a/b))
                except:
                        print("It is impossible to divide by 0!")
        elif op == 6:
                try:
                        print("Quotient: {} / {} = {} Remainder: {}".format(a,b,a//b,a%b))
                except:
                        print("It is impossible to divide by 0!")
        else:
                print("invalid input")
        again()

def again():
                choice = int(input("""
Would you like to make another calculation?
1: Yes
2: No
"""))
                if choice == 1:
                        calculate()
                elif choice == 2: 
                        print("See you next time!")
                else:
                        print("Invalid input")
calculate()
