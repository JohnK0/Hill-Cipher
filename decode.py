"""
decode.py
Description: decrypts a ciphertext
"""
import numpy as n
import conversions as conv

# uses the Extended Euclidean Algorithm
def find_mult_inv(det, modulus):
    p0, p1 = 0, 1
    quotient = []
    remainder = 0
    # the Euclidean algorithm to only gather the quotients
    while remainder != 1:
        quotient.append(int(modulus/det))
        remainder = int(modulus%det)
        det, modulus = remainder, det
    # compute the multiplicative inverse of the determinant
    for i in range(len(quotient)):
        p0, p1 = p1, int(n.remainder(p0 - p1*quotient[i], 26))
    #return the multiplicative inverse of the determinant
    return p1

# returns the multiplicative inverse of the determinant
def find_mult_inv_of_det(keymatrix):
    #find the determinant of the keymatrix
    det = round(n.remainder(n.linalg.det(keymatrix), 26))
    #return the multiplicative inverse of the determinant
    return find_mult_inv(det, 26)

# computes the adjacent keymatrix
def find_adj_matrix(keymatrix):
    keymatrix[0][0], keymatrix[1][1] = keymatrix[1][1], keymatrix[0][0]
    keymatrix[0,1], keymatrix[1,0] = -keymatrix[0,1], -keymatrix[1,0]
    # return the adjacent keymatrix
    return keymatrix

# computes the inverse keymatrix
def find_inv_keymatrix(keymatrix):
    # the keymatrix's determinant and adjacent matrix
    det, adj_keymatrix = find_mult_inv_of_det(keymatrix), find_adj_matrix(keymatrix)
    # returns the inverse keymatrix
    return n.remainder(det*adj_keymatrix, 26)

# decrypts a ciphertext through a keyword
def decode_(keyword, ciphertext):
    keymatrix = conv.keyword_to_keymatrix(keyword, 2)
    inv_keymatrix = find_inv_keymatrix(keymatrix)
    ciphermatrix = conv.text_to_matrix(ciphertext, 2)
    return(conv.matrix_to_text(inv_keymatrix, ciphermatrix))

def main():
    keyword = input("What is the key? ")
    ciphertext = input("What do you want to decode? ")
    # Encoded text of below is "jajamyeung"
    # ciphertext = 'lvlvqggejb'
    print("The decrypted text: ",decode_(keyword, ciphertext))

if __name__ == "__main__":
    main()
