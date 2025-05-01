import random,string,pyperclip

print("--- Random Password Generator ---")

length = int(input("Enter the length of password: "))
level = input("Choose difficulty level (weak / medium / strong): ").lower()

def generate_password(length, level):
    levels = {
        'weak': string.ascii_letters,
        'medium': string.ascii_letters + string.digits,
        'strong': string.ascii_letters + string.digits + string.punctuation
    }

    min_length = {
        'weak':3,
        'medium': 6, 
        'strong': 8}

    if level not in levels:
        return "Error: Select a valid level (weak / medium / strong)."
    
    if level in min_length and length < min_length[level]:
        return f"Error: {level} password must be at least {min_length[level]} characters long."

    return ''.join(random.choice(levels[level]) for _ in range(length))

password=generate_password(length, level)
print("Generated password:", password )

if not password.startswith("Error"):
    pyperclip.copy(password)
    print("----password copied to clipboard----")
