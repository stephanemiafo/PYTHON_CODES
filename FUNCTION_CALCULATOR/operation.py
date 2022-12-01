
def add(addition):
    if user_operation == addition:
        print(x + y)

def sub(substraction):
    if user_operation == substraction:
        print(x - y)

def multi(multiplication):
    if user_operation == multiplication:
        print(x * y)

def div(division):
    if user_operation == division:
        print(x / y)

x = 5
y = 9
user_operation = input("Please enter you operation of choice here:\n")

# ASSUMING THAT THESE ARE THE ONLY OPERATIONS THAT THE USER CAN PERFORM
operations = ["addition", "substraction", "multiplication", "division"]
if user_operation == operations[0]:
    add(operations[0])
elif user_operation == operations[1]:
    sub(operations[1])
elif user_operation == operations[2]:
    multi(operations[2])
else:
    div(operations[3])

 



