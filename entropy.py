import math
import string


def password_alphabet(password):
    alphabet = 0
    
    if any(char.isdigit() for char in password):
        alphabet += 10
    if any(not char.isalnum() for char in password):
        alphabet += 32
    if any(char.islower() for char in password):
        alphabet += 26
    if any(char.isupper() for char in password):
        alphabet += 26

    return alphabet

    
def password_entropy(password):
    alphabet = password_alphabet(password)
    length = len(password)

    if alphabet == 0:
        return 0 

    entropy = length * math.log2(alphabet)
    return entropy

def password_strength(entropy):
    if entropy < 40:
        return "Weak"
    elif entropy < 60:
        return "Medium"
    elif entropy < 80:
        return "Strong"
    else:
        return "Very Strong"


password = input("Enter password: ")

length = len(password)
alphabet = password_alphabet(password)
entropy = password_entropy(password)
strength = password_strength(entropy)

print("Length of password: ", length)
print(f"Alphabet: {alphabet}")
print(f"Entropy: {entropy:.2f} bits")
print(f"Strength: {strength}")