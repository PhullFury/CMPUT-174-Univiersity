import time

age = int(input("Enter the legal driving age: "))

time.sleep(.5)

if (age == 16):
    print("Correct, the legal driving age is", age)
else:
    print("No, the legal driving age is 16")