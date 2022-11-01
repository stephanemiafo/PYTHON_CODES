# INSTRUCTION FOR THE USER
print("Please enter a number between 1-100")
# READING USER INPUT
num = int(input("enter an integer: "))
# PERFORMING THE ANALYSIS BY USING MODULO
if num % 2 == 0: 
    print(f"your number {num} is EVEN")   # DISPLAYING THE RESULT FOR EVEN NUMBERS 
else:
    print(f"your number {num} is ODD")    # DISPLAYING THE RESULT FOR ODD NUMBERS  


     # METHOD 2
# READING USER INPUT
# num = int(input("enter a number: "))
# if num > 1 and num < 100:  # REQUIRING THE NUMBER TO BE IN THIS RANGE
#     if num % 2 == 0:    # PERFORMING THE ANALYSIS
#         print(f"your number {num} is EVEN")     # DISPLAYING THE RESULT FOR EVEN NUMBERS 
#     else:
#         print(f"your number {num} is ODD")      # DISPLAYING THE RESULT FOR ODD NUMBERS  
#     print("Good to pay attention")   # DISPLAY THE RESULT FOR PICKING A NUMBER IN THE GIVEN RANGE
# else:
#     print("number out of range")    # DISPLAY THE RESULT FOR PICKING A NUMBER OUT OF RANGE
#     print("please pay attention to instructions")  # REINSTRUCTION MESSAGE