from calculator_art import logo
# in the following lines of codes, I have defined functions to carry out the four basic operations - you can define more functions to cover more advanced arithmetic operations
def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}
# this function is for the recursion of the program to be able to start a new calculation
def calculator():
  print(logo)

  num1 = float(input("What's the first number?: "))
  # this for loop simply prints out all the symbols for the user to choose from
  for symbol in operations:
    print(symbol)
  should_continue = True
  # This while loop is for reducing repetition in case the user wants to continue with calculation
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    # An if statement to check whether the user wants to continue calculaiton or start a new one
    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
      num1 = answer
    else:
      should_continue = False
      # for the clear function to work properly, you should imoprt the right package based on your IDE
      clear()
      calculator()

calculator()
