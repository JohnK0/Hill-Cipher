"""
encode.py
Description: encrypts a plaintext
"""

import numpy as n
import conversions as conv

def encode_(keyword, plaintext):
    # conversion from plaintext to plainmatrix
    plainmatrix = conv.text_to_matrix(plaintext, 2)
    # conversion from keyword to keymatrix
    keymatrix = conv.keyword_to_keymatrix(keyword, 2)
    # print("plainmatrix:\n", plainmatrix, "\nKeymatrix:\n", keymatrix)
    ciphertext = conv.matrix_to_text(keymatrix, plainmatrix)
    # print(ciphertext)
    return ciphertext

def main():
    # user input for plaintext
    plaintext = input("What do you want to encode? ")
    keyword = input("What is the key? ")
    # basic keyword below
    # keyword = 'hill'
    #encrypt plaintext
    print("The encrypted text: ", encode_('hill', plaintext))

if __name__ == "__main__":
    main()
