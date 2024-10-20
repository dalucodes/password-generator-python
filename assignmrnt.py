 import random
import string

def passwordGenerator(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""
    length=8
    for i in range(length):
        password +=random.choice(characters)
    return(password)
    
length = int(input("how long do you want your password to be"))

print(passwordGenerator(length))
