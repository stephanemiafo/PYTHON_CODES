
# READING STUDENT'S GRADE
history = float(input("enter your history grade here: "))
socio = float(input("enter your socio grade here: "))
psycho = float(input("enter your psycho grade here: "))
esl = float(input("enter your esl grade here: "))
engl = float(input("enter your engl grade here: "))

# CALCULATION THE AVERAGE GRADE
avg = (history + socio + psycho + esl + engl) / 5

if avg >= 90:                                                       # COMPARING THE AVERAGE TO THE STANDART
    print(f"{avg:.2f}, the student's final grade is A")             # DISPLAYING THE RESULT FOR "A" STUDENTS AT 2 DECIMAL PLACE
elif avg >= 80 and avg < 90:                                        # COMPARING THE AVERAGE TO THE STANDART
    print(f"{avg:.2f}, the student's final grade is B")             # DISPLAYING THE RESULT FOR "B" STUDENTS AT 2 DECIMAL PLACE
elif avg >= 70 and avg < 80:                                        # COMPARING THE AVERAGE TO THE STANDART
    print(f"{avg:.2f}, the student's final grade is C")             # DISPLAYING THE RESULT FOR "C" STUDENTS AT 2 DECIMAL PLACE
elif avg >= 60 and avg < 70:                                        # COMPARING THE AVERAGE TO THE STANDART
    print(f"{avg:.2f}, the student's final grade is D")             # DISPLAYING THE RESULT FOR "D" STUDENTS AT 2 DECIMAL PLACE
else: 
    print("Failed")                                                 # DISPLAYED THIS RESULT IF STUDENT'S FINAL GRADE DOES NOT MEET ANY OF THE ABOVE STANDART
