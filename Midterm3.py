#Cole McLean CSCI 161 MWF Midterm 3
def clamp(Number):

    if Number < 0:
        Number = 0
        return Number
    elif Number > 255:
        Number = 255
        return Number
    else:
        return Number


usr = input("Enter a number: ")
Answer = clamp(int(usr))
print(Answer)
