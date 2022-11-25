

# CODE TO EXECUTE A COUNTDOWN in a While-Loop
count = 11                                                       # Initializing the count
while count <= 11 and count >= 0:                                # Delimiting the interval where the loop will happen
    count -= 1                                                   # Decrement (direction in which the loop will occur)
    if count <= 10 and count == 10:                              # Isolating the case of 10 when the loop is decreasing
        print("starting the countdown from 10 - 0")              # Warning message to the user 
        print(count)                                             # print the actual count
    elif count < 10 and count >= 0:                              # Rest of the loop decreasing
        print(count) 
    else:
        print("Countdown is over")                               # Message at the end of the loop