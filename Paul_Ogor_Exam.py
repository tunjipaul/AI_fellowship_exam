#question 1.

def add_task(a,b):
    return a + b

def subtract_task(a,b):
    return a - b

def multiply_task(a, b):
    return a * b

def divide(a,b):
    denominator_error(b)
    return a/b


def denominator_error(b):
    if b <= 0:
        raise ZeroDivisionError
    


    




while True:
    
    
    try:
        print("Choose Operation; (+, -, *, /) or type Exit to quit: ")
        num_1 = float(input("Enter first number: "))
        num_2 = float(input("Enter Second Number: "))
    
        choice = input("Select an operation; (+, -, *, /) or type Exit to quit: ").strip().lower()
    
        if choice == "+":
            print(f"The sum of {num_1} + {num_2} = {add_task(num_1, num_2)} ")
        elif choice == "-":
            print(f"The subtraction of {num_1} - {num_2} = {subtract_task(num_1, num_2)} ")
        elif choice == "*":
            print(f"The multiplication of {num_1} * {num_2} = {multiply_task(num_1, num_2)} ")
        elif choice == "/":
            print(f"The division of {num_1} / {num_2} = {divide(num_1, num_2)} ")
        elif choice == "exit":
            print(f"Exiting Calculator... Goodbye!")
            break
        else:
            print("You have entered the wrong value. Try again! ")
    except Exception as d:
        raise("You have entered the wrong value. Try again!")
    except Exception as e:
        print("error:", e)
    

#question 2
while True:
    user_input = input("Enter a number (or type 'exit' to quit): ")
    if user_input == "exit":
        print("Goodbye!")
        break       # break out of loop
    
    num = int(user_input)   # convert to integer
    
    if num % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")

#question 3.
while True:
    age = float(input("Enter your age (or type exit to quit): "))
    try:
     if age >= 18:
        print("You can vote")
     elif age == "exit":
        print("Goodbye!")
        break
     else:
            print("You cannot vote")
    
    except:
     print("Invalid input")
     