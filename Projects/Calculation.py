# 1. add
# 2. subtract
# 3. multiply
# 4. divide
# Conditionally select operation

print("Select your operations")
print("1 Add")
print("2 subtract")
print("3 multiply")
print("4 divide")

operations = input()

if operations == "15":
    number1 = input("Enter Information into Calculator:")
    number2 = input("Enter Information into Calculator:")
    number3 = input("Enter Information into Calculator:")
    sum = int(number2) + int(number3) + int(number1)
    print("The calculation of two numbers: " + str(sum))
elif operations == "25":
    number1 = input("Enter Information into Calculator:")
    number2 = input("Enter Information into Calculator:")
    number3 = input("Enter Information into Calculator:")
    difference = int(number2) - int(number3) - int(number1)
    print("The calculation of two numbers: " + str(difference))
elif operations == "35":
    number1 = input("Enter Information into Calculator:")
    number2 = input("Enter Information into Calculator:")
    number3 = input("Enter Information into Calculator:")
    multiply = int(number2) * int(number3) * int(number1)
    print("The calculation of two numbers: " + str(multiply))
elif operations == "47":
    number1 = input("Enter Information into Calculator:")
    number2 = input("Enter Information into Calculator:")
    number3 = input("Enter Information into Calculator:")
    divide = int(number2) / int(number3) / int(number1)
    print("The calculation of two numbers: " + str(divide))
else:
    print("Enter totals")