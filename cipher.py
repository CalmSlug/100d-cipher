# Importing art assets:
import cipher_art

# List of characters that will be encoded or decoded:
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Cipher function:
def caesar(action, plain_text, shift_amount):
    # Creating a variable to store modified text;
    # Checking each character in the initial text:
    shifted_text = ""
    for item in plain_text:

        # If checked character IS in the alphabet list:
        if item in alphabet:

            # Picking a character with a BIGGER index;
            # If shift is out of bounds, loop to the START of the list:
            if action == "encode":
                shifted_index = alphabet.index(item) + shift_amount
                if shifted_index > 25:
                    shifted_index = shifted_index - 26
            
            # Picking a character with a SMALLER index;
            # If shift is out of bounds, loop to the END of the list:
            elif action == "decode":
                shifted_index = alphabet.index(item) - shift_amount
                if shifted_index < 0:
                    shifted_index = 26 + shifted_index
            
            # Writing new character into the modified text variable:
            shifted_text += alphabet[shifted_index]
        
        # If checked character IS NOT in the alphabet list:
        else:
            # Writing checked character into the modified text variable:
            shifted_text += item
    
    # Printing out final result:
    print(f"The {action}d text is: {shifted_text}")

# User input function;
# Uses recursion to chain itself:
def main():
    # Getting user input:
    direction = input("Type ENCODE to encrypt, type DECODE to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # Checking if the shift variable is too big;
    # It has to be less than the alphabet variable:
    if shift > 26:
        shift = shift % 26

    # Performing requested task using the cipher function:
    caesar(direction, text, shift)

    # Checking if user wants to perform another operation:
    print()
    print("Type YES if you want to go again. Otherwise type NO.")
    again = input().lower()
    if again == "yes":
        main()
    else:
        print("Goodbye")

# Main logic:
# 1. Print intro art
# 2. Start user input function
print(cipher_art.logo)
main()
