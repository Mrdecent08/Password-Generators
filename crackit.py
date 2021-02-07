import random
import numpy as np

name = list(input("Enter the name: "))
dateofbirth = list(input("Enter date of birth: "))
phonenumber = list(input("Enter Phone number: "))
petname = list(input("Enter the PetName: "))
characters= list(name+dateofbirth+phonenumber+petname)
total = len(characters)
len = int(input("Enter length of password: "))
j=pow(total,len)
password =""
for i in range(j):
    password =""
    for i in range(len):
        password = password+random.choice(characters)
        print("Your password is ", end='')
        print("\033[96m {}\033[00m" .format(password))
print("Your passwords are generated.")