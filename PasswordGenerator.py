import secrets
import string
import random

max_length = 16
min_length = 4
 




def password_length():
    while True:
        password_length = int(input(f"Enter length ({min_length}-{max_length}): "))

        print(password_length)
        if min_length <= password_length and password_length <= max_length:
            print("Length Accepted")
            return password_length
        else:
            print("incorrect length")

def yes_no_check(question):
     while True:
         answer = input(question).lower()

         if answer == "yes":
            return True
         elif answer == "no":         
            return False
         print("Please enter Yes or No.")


def password_options():
    while True:
        use_uppercase = yes_no_check("Use Uppercase? (Yes/No): ")
        use_digits = yes_no_check("Use Digits? (Yes/No): ")
        use_symbols = yes_no_check("Use Symbols? (Yes/No): ")
        use_lowercase = yes_no_check("Use Lowercase? (Yes/No): ")

        characters = ""

        if use_lowercase:
            characters += string.ascii_lowercase
        if use_uppercase:
            characters += string.ascii_uppercase
        if use_digits: 
            characters += string.digits
        if use_symbols:
            characters += string.punctuation

        if characters:
            return (characters, use_symbols, use_digits, use_uppercase, use_lowercase)
        
        print("Choose at least one option.")

        

def generate_password(
        length,
        characters,
        use_symbols,
        use_digits,
        use_uppercase,
        use_lowercase
    ): 

    required = 0

    #password = "" 
    password = []

    if use_uppercase:
        password.append(secrets.choice(string.ascii_uppercase))
    if use_lowercase:
        password.append(secrets.choice(string.ascii_lowercase))
    if use_digits:
        password.append(secrets.choice(string.digits))
    if use_symbols:
        password.append(secrets.choice(string.punctuation))

    if use_symbols:
        required += 1
    if use_digits:
        required += 1
    if use_uppercase:
        required += 1
    if use_lowercase:
        required += 1

    remaining = length - required

    for _ in range(remaining):
        password.append(secrets.choice(characters))

    random.shuffle(password)

    password = "".join(password)

    return password


def main():
    length = password_length()
    characters, use_symbols, use_digits, use_uppercase, use_lowercase = password_options()
    password = generate_password(
        length, 
        characters,
        use_symbols,
        use_digits,
        use_uppercase,
        use_lowercase,
        )

    print('Your password:', password)

main()
#length = password_length()
#password = generate_password(length)
#print(password)

