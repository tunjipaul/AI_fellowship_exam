Python Exam
Read the questions below carefully. Each question tests different aspects of your Python knowledge.
Writing full programs
Completing partially written code
Debugging incorrect code
You are required to write all your programs in a single file and name it "your_fullname_exam.py". Create a new repository named "AI-fellowship-exam" and push your codes there.
Onces you are done pushing, add your file to a zip folder and submit both the zip file and your github link on the exam platform.
Question 1
Write a Python program that works as a basic calculator with continuous use.

Instruction

The program should repeatedly allow the user to perform operations until they choose to exit.
Ask the user to enter two numbers.
Then ask them to choose an operation: addition, subtraction, multiplication, or division.
Use functions to define each operation.
Use try-except to handle invalid input and division by zero.
Use control flow (if-elif-else) to select the correct operation.
Use a while loop to keep running until the user chooses to exit.
Expected Output

Enter first number: 12
Enter second number: 4
Choose operation (+, -, *, /) or 'exit' to quit: /
Result: 3.0

Enter first number: 10
Enter second number: 0
Choose operation (+, -, *, /) or 'exit' to quit: /
Error: Cannot divide by zero

Enter first number: 5
Enter second number: 6
Choose operation (+, -, *, /) or 'exit' to quit: *
Result: 30

Choose operation (+, -, *, /) or 'exit' to quit: exit
Exiting calculator... Goodbye!
Question 2
Complete the missing parts of the program below so that it keeps asking the user for a number and tells whether it is even or odd.
Instruction

Use input, int conversion, if-else control flow, and print output.
Use a while loop that runs until the user types 'exit'.
while ____
    user_input = input("Enter a number (or type 'exit' to quit): ")
    if user_input == "exit"__
        print("Goodbye!")
        ______        # break out of loop
    
    num = __________(user_input)   # convert to integer
    
    if num % 2 == 0:
        print("The number is ______")
    ___
        print("The number is ______")

Expected Output

Enter a number (or type 'exit' to quit): 7
The number is odd
Enter a number (or type 'exit' to quit): 10
The number is even
Enter a number (or type 'exit' to quit): exit
Goodbye!
Question 3
The following code is supposed to ask for a user’s age repeatedly and say whether they are allowed to vote (18+).
It should also exit if the user types 'exit'. However, the code contains errors.
while True:
    age = input("Enter your age (or type exit to quit): ")
    if age == exit:
        print("Goodbye!")
        break
    
    try:
        if age >= 18:
            print("You can vote")
        else:
            print("You cannot vote")
    except:
        print("Invalid input")
Instruction

Identify and fix the errors.
Ensure the program uses try-except to catch invalid input.
Ensure it uses a while loop to keep asking until 'exit' is typed.
Expected Output

Enter your age (or type 'exit' to quit): 20
You can vote
Enter your age (or type 'exit' to quit): abc
Invalid input. Please enter a number.
Enter your age (or type 'exit' to quit): exit
Goodbye!