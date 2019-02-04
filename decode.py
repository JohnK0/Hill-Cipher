import numpy as n
import conversions as conv

#uses the Extended Euclidean Algorithm
def find_mult_inv(dev, modulus):
    p0, p1 = 0, 1
    quotient = []
    remainder = 0
    while remainder != 1:
        quotient.append(int(modulus/dev))
        remainder = int(modulus%dev)
        dev, modulus = remainder, dev
    
    for i in range(len(quotient)):
        p0, p1 = p1, int(n.remainder(p0 - p1*quotient[i], 26))

    return p1

def find_mult_inv_of_det(keymatrix):
    det = round(n.remainder(n.linalg.det(keymatrix), 26))
    return find_mult_inv(det, 26)


def find_adj_matrix(keymatrix):
    keymatrix[0][0], keymatrix[1][1] = keymatrix[1][1], keymatrix[0][0]
    keymatrix[0,1], keymatrix[1,0] = -keymatrix[0,1], -keymatrix[1,0]
    return keymatrix

def find_inv_keymatrix(keymatrix):
    det, adj_keymatrix = find_mult_inv_of_det(keymatrix), find_adj_matrix(keymatrix)
    return n.remainder(det*adj_keymatrix, 26)


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
    print("Decoded text: ",decode_(keyword, ciphertext))

if __name__ == "__main__":
    main()
