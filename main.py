import encode as e
import decode as d

def main():
    # user input for plaintext
    plaintext = input("Enter a text you want to encode: ")
    keyword = input("Enter a key: ")
    (keymatrix, ciphertext) = e.encode_(keyword, plaintext)
    print("Ciphertext for \"", plaintext,"\" is \"", ciphertext,"\"")
    response = input("Do you want to decode the ciphertext (y/n)? ")
    if response == "y":
        decodedtext = d.decode_(keyword, ciphertext)
        print("Decoded text: ", decodedtext)
if __name__ == "__main__":
    main()
