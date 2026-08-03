import string


def analyze_password():
    password = input("Enter password: ")
    length = len(password)

    lower_count = 0
    upper_count = 0
    digits_count = 0
    symbols_count = 0

    lower_repeats = {}
    upper_repeats = {}
    digits_repeats = {}
    symbols_repeats = {}


    # Block for Lowercase repeats
    for char in password:
        if char in string.ascii_lowercase:
            lower_repeats[char] = lower_repeats.get(char, 0) + 1
    print("Lowercase repeats: ")
    found = False
    for char, count in lower_repeats.items():
        if count > 1:
            print(f"'{char}' repeats {count} times")
            found  = True
    if not found:
        print("No repeated lowercase letters.")

    # Block for Upppercase repeats
    for char in password:
        if char in string.ascii_uppercase:
            upper_repeats[char] = upper_repeats.get(char, 0) + 1
    print("Uppercase repeats: ")
    found = False
    for char, count in upper_repeats.items():
        if count > 1:
            print(f"'{char}' repeats {count} times")
            found = True
    if not found:
        print("No repeated uppercase letters.")

    # Block for Digits repeats
    for char in password:
        if char in string.digits:
            digits_repeats[char] = digits_repeats.get(char, 0) + 1
    print("Digits repeats: ")
    found = False
    for char, count in digits_repeats.items():
        if count > 1:
            print(f"'{char}' repeats {count} times")
            found = True
    if not found:
        print("No repeated Digits.")

    # Block for Symbols repeats
    for char in password:
        if char in string.punctuation:
            symbols_repeats[char] = symbols_repeats.get(char, 0) + 1
    print("Symbols repeats: ")
    found = False
    for char, count in  symbols_repeats.items():
        if count > 1:
            print(f"'{char}' repeats {count} times")
            found = True 
    if not found:
        print("No repeated symbols.")

    for char in password:
        if char in string.ascii_lowercase:
            lower_count += 1
        elif char in string.ascii_uppercase:
            upper_count += 1
        elif char in string.digits:
            digits_count += 1
        elif char in string.punctuation:
            symbols_count += 1


    print(f"Length: {length}")
    print(f"Lowercase: {lower_count}")
    print(f"Uppercase: {upper_count}")
    print(f"Digits: {digits_count}")
    print(f"Symbols {symbols_count}")

analyze_password()