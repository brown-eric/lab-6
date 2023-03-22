# Eric Brown's Code
def encode(password):

    encode_dict = {"0": "3", "1": "4", "2": "5", "3": "6", "4": "7",
                   "5": "8", "6": "9", "7": "0", "8": "1", "9": "2"}

    encoded_password = ""

    for character in password:
        encoded_password += encode_dict[character]

    return encoded_password


def menu():
    print("Menu\n"
          "-------------\n"
          "1. Encode\n"
          "2. Decode\n"
          "3. Quit\n\n")


def main_loop():
    while True:
        menu()
        choice = int(input("Please enter an option: "))
        if choice == 1:
            password = str(input("Please enter your password to encode: "))
            encoded_password = encode(password)
            print("Your password has been encoded and stored!\n")
        elif choice == 2:
            print(f"The encoded password is {encoded_password}, and the original password is {password}.\n")
        elif choice == 3:
            break


if __name__ == '__main__':
    main_loop()
