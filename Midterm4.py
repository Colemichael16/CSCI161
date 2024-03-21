#Cole McLean CSCI 161 Midterm 4 MWF Class
times = 5
names = []
for i in range(5):
    usr = input("Please type a name ");
    names.append(usr)
    print("You added", usr, "to the list.")

names.sort()
print("Organized names are ", names)
