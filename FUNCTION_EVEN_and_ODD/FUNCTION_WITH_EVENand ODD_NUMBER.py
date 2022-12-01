
def even(number):
    while y in number:
       # print(y)
        if y % 2 == 0:  
            print(f"your number {y} is EVEN") 
            break

def odd(number):
    while y in number:
        if y % 2 == 1:  
            print(f"your number {y} is ODD")      
            break 

x = range(1, 111)
y = int(input("Enter a integer here:\n"))
if y in x and y % 2 == 0:
    even(x)
elif y in x and y % 2 == 1:
    odd(x)
else:
    print("your choice is out of range")


