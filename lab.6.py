def encode(original_password): # this is my first edit
    result = ""
    for numbers in original_password:
        new_numbers = str((int(numbers) + 3) % 10 )
        result += new_numbers
    return result

def decode(password):
    pass

def menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

def main():
    test = True
    while test:
        menu()
        user_input = int(input("Please enter an option: "))
        if user_input == 1:
            original_password = input("Please enter your password to encode: ")
            original_password = encode(original_password)
            print("Your password has been encoded and stored! ")
        elif user_input == 2:
            pass
        else:
            test = False

if __name__ == '__main__':
    main()