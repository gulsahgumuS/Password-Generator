import random 
import string 

def get_user_input():
    lenght= input("Enter the desired password length:")
    while not lenght.isdigit() or int(lenght) <=0:
        print("Please enter a valid positive number.")
        lenght=("Enter the desired password lenght:")

    preferences={
        "uppercase":input("Include uppercase letters? (y/n): ").strip().lower()=='y',
        "lowercase": input("Include lowercase letters? (y/n): ").strip().lower()=='y',
        "numbers": input("Include numbers? (y/n): ").strip().lower()=='y',
        "symbols": input("Include symbols (y/n): ").strip().lower()=='y'
    }
    return int(lenght) ,preferences

def create_character_pool(preferences):
    char_pool=" "

    if preferences["uppercase"]:
        char_pool += string.ascii_uppercase
    if preferences["lowercase"]:
        char_pool += string.ascii_lowercase
    if preferences["numbers"]:
        char_pool += string.digits
    if preferences["symbols"]:
        char_pool += string.punctuation

    return char_pool

def generate_password(lenght,char_pool):
    return''.join(random.choice(char_pool) for _ in range(lenght))

def password_generator():
    print("Welcome to the Password Generator:)")

    lenght, preferences= get_user_input()
    char_pool=create_character_pool(preferences)
    
    if not char_pool:
        print("ERROR no character types selected. Please choose at least one.")
        return
    
    password=generate_password(lenght, char_pool)
    print(f"Your generator password is: {password}")

if __name__ == "__main__":
    password_generator()