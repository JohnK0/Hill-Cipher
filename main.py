"""
main.py
Description: program to encrypt a text (plaintext) into an encrypted text (ciphertext) and decrypt the ciphertext back into plaintext
Assumption:
 - the key matrix will be 2x2
"""
import encode as e
import decode as d

def main():
    # user input for plaintext
    plaintext = input("Enter a text you want to encode: ")
    keyword = input("Enter a key: ")
    # encrypt plaintext
    ciphertext = e.encode_(keyword, plaintext)
    print("Ciphertext for \"", plaintext,"\" is \"", ciphertext,"\"")
    response = input("Do you want to decode the ciphertext (y/n)? ")
    if response == "y":
        # decrypt ciphertext
        decodedtext = d.decode_(keyword, ciphertext)
        print("Decoded text: ", decodedtext)
if __name__ == "__main__":
    main()
