import random
def weakpassword():
    characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y','z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    len = 5
    password =""
    
    for i in range(len):
        password = password+random.choice(characters)
    print("Your password is ", end='')
    print("\033[96m {}\033[00m" .format(password))

def mediumpassword():
    characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y','z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>','*', '(', ')']
    len = 5
    password =""
        
    for i in range(len):
        password = password+random.choice(characters)
    print("Your password is ", end='')
    print("\033[96m {}\033[00m" .format(password)) 

def strongpassword():
    characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y','z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>','*', '(', ')']
    len = 8
    password =""
    for i in range(len):
        password = password+random.choice(characters)
    print("Your password is ", end='')
    print("\033[96m {}\033[00m" .format(password))
if __name__ == "__main__":
    print(" To generate a weak password press 1 \n To generate a weak password press 2 \n To generate a weak password press 3")
    choice = int(input("Enter the choice "))
    if choice==1:
        weakpassword()
    if choice==2: 
            mediumpassword() 
    if choice==3: 
            strongpassword() 