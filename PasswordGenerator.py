import secrets
import string

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
    use_uppercase = yes_no_check("Use Uppercase? (Yes/No): ")
    use_digits = yes_no_check("Use Digits? (Yes/No): ")
    use_symbols = yes_no_check("Use Symbols? (Yes/No): ")
    use_lowercase = yes_no_check("Use Lowercase? (Yes/No): ")

    while True:
        characters = " "
        if use_lowercase:
            characters += string.ascii_lowercase
        if use_uppercase:
            characters += string.ascii_uppercase
        if use_digits: 
            characters += string.digits
        if use_symbols:
            characters += string.punctuation
        if characters == " ":
            print("You must select at least one chracter type.")

            return characters
        

def generate_password(length, characters): 

    password = " "

    for _ in range(length):
        password += secrets.choice(characters)

    return password


def main():
    length = password_length()
    options = password_options()
    password = generate_password(length, options)

    print('Your password:', password)

main()
#length = password_length()
#password = generate_password(length)
#print(password)

