>>> while True:
	print("Options: ")
	print("Enter 'add' to add two numbers")
	print("Enter 'subtract' to subtract two numbers")
	print("Enter 'multiply' to mulitply two numbers")
	print("Enter 'divide' to divide two numbers")
	print("Enter 'quit' to end the program")
	userInput = input(": ")
	if userInput == "quit":
		break
	elif userInput == "add":
		num1 = float(input("Enter a number: "))
		num2 = float(input("Enter a second number: "))
		result = str(num1 + num2)
		print("The answer is " + result)
	elif userInput == "subtract":
		num1 = float(input("Enter a number: "))
		num2 = float(input("Enter a second number: "))
		result = str(num1 - num2)
		print("The answer is " + result)
	elif userInput == "multiply":
		num1 = float(input("Enter a number: "))
		num2 = float(input("Enter a second number: "))
		result = str(num1 * num2)
		print("The answer is " + result)
	elif userInput == "divide":
		num1 = float(input("Enter a number: "))
		num2 = float(input("Enter a second number: "))
		result = str(num1 / num2)
		print("The answer is " + result)
	else:
		print("Unkown input")
