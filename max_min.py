#  GATHERING USER INPUTS
a = float(input("enter a value for 'a' here: "))
b = float(input("enter a value for 'b' here: "))
c = float(input("enter a value for 'c' here: "))
d = float(input("enter a value for 'd' here: "))
# LIST OF INPUTS 
# in_gle = []  # THIS IS THE CASE OF AN EMPTY LIST
in_gle = [a, b, c, d]    
if len(in_gle) == 0:                                  # 1ST CONDITION  
    print("None")                                     # DISPLAY THE RESULT IF THE 1ST CONDITION IS TRUE  
elif len(in_gle) != 0 and a == b == c == d == 0:      # 2ND CONDITION                                                                           
    print(f"{0}\t{0}")                                # DISPLAY THE RESULT IF THE 2ND CONDITION IS TRUE
else:
    print(f"{max(in_gle)}\t{min(in_gle)}")            # DISPLAY ANY OTHER RESULT



    


