# fuction in python

# def my_function():
#     print("Salam o alikum chahat fateh all the way from london")
# # my_function()   function calling...

# def display_name(name):
#     print(f"How are you samad {name}")

# display_name("Abdus samad")
# display_name("Kamran Khan")

# lambda funciton 
# my_lamdafunciton = lambda number1, number2: number1 + number2
# print(my_lamdafunciton(12,8))

# Without Lambda function Example
# def addition(firstNumber):
#     def actual_Addition(secondNumber):
#         print("Old Way")
#         return firstNumber + secondNumber
#     return actual_Addition
# result = addition(10)
# finalResult = result(40)
# print(finalResult)

# Same example with lamda function
def addition(firstNumber):
    return lambda secondNumber: firstNumber + secondNumber
result = addition(10)
finalResult = result(80)
print(finalResult)