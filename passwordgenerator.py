import random
import string
def generate_password(length, use_letters, use_numbers, use_symbols):
    
    char_pool = ""
    if use_letters:
        char_pool += string.ascii_letters 
    if use_numbers:
        char_pool += string.digits  
    if use_symbols:
        char_pool += string.punctuation 
    if not char_pool:
        print("You must select at least one character type!")
        return None
   
    password = ''.join(random.choice(char_pool) for _ in range(length))
    return password

def main():
    
    length = int(input("Enter the desired password length: "))

    use_letters = input("Include letters? (yes/no): ").lower() == "yes"
    use_numbers = input("Include numbers? (yes/no): ").lower() == "yes"
    use_symbols = input("Include symbols? (yes/no): ").lower() == "yes"

    password = generate_password(length, use_letters, use_numbers, use_symbols)
    if password:
        print(f"\nGenerated Password: {password}")

if __name__ == "__main__":
    main()