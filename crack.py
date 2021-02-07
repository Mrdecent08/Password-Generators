import random
def onlysmall():
    characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']
    len = int(input("Enter length of password: "))
    j=pow(26,len)
    password =""
    for i in range(j):
        password =""
        for i in range(len):
            password = password+random.choice(characters)
        print("Your password is ", end='')
        print("\033[96m {}\033[00m" .format(password))

def onlycapital():
    characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    len = int(input("Enter length of password: "))
    j=pow(26,len)
    password =""
    for i in range(j):
        password =""
        for i in range(len):
            password = password+random.choice(characters)
        print("Your password is ", end='')
        print("\033[96m {}\033[00m" .format(password)) 

def alphabets():
    characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y','z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    len = int(input("Enter length of password: "))
    j=pow(52,len)
    password =""
    for i in range(j):
        password =""
        for i in range(len):
            password = password+random.choice(characters)
        print("Your password is ", end='')
        print("\033[96m {}\033[00m" .format(password))

def includedigits():
    characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y','z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    len = int(input("Enter length of password: "))
    j=pow(62,len)
    password =""
    for i in range(j):
        password =""
        for i in range(len):
            password = password+random.choice(characters)
        print("Your password is ", end='')
        print("\033[96m {}\033[00m" .format(password))
def includespecial():
    characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y','z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>','*', '(', ')']
    len = int(input("Enter length of password: "))
    j=pow(77,len)
    password =""
    for i in range(j):
        password =""
        for i in range(len):
            password = password+random.choice(characters)
        print("Your password is ", end='')
        print("\033[96m {}\033[00m" .format(password))
if __name__ == "__main__":
    print(" To generate a passwords with only small letters press 1 \n To generate a passwords with only capital letters press 2 \n To generate a passwords including digits press 3 \n To generate a passwords including special character press 4 \n To generate passwords with only alphabets press 5 \n")
    choice = int(input("Enter the choice "))
    if choice==1:
        onlysmall()
    if choice==2: 
            onlycapital() 
    if choice==3: 
            includedigits() 
    if choice==4: 
            includespecial()
    if choice==5: 
            alphabets() 
    