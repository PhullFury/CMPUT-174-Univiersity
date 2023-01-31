Catch = 0
Release = 0
Number_Trout = 0
while Catch < 7:
    Fish = input("Have you caught a Fish? Y/N: ")
    if (Fish == "Y"):
        Catch += 1
        Trout = input("Was it a Trout? Y/N: ")
        if (Trout == "Y"):
            Number_Trout += 1
        elif (Trout == "N"):
            Would_Release = input("Would you like to release? Y/N: ")
            if (Would_Release == "Y" and Release <= 3):
                Release += 1
                print("Fish released")
            else:
                print("Release limit reahced")

print("Catch limit released")

if(Number_Trout >= 5):
    print("Trout Cakes")
else:
    print("Seafood Medley")
