import numpy as n
import immutable_data as id

def matrix_to_text(keymatrix, matrix):
    text = ""
    # multiply plainmatrix by keymatrix modulo 26
    matrix = n.remainder(n.matmul(keymatrix, matrix), 26)
    (i, j) = n.shape(matrix)
    # create the ciphertext from the ciphermatrix
    for j0 in range(j):
        for i0 in range(i):
            text = text+(id.num_to_alph[matrix[i0][j0]])
    return text

def keyword_to_keymatrix(keyword, dimension):
    keynum = []
    # disparity: to verify whether the length of the keyword is less than the length of the dimension squared
    disparity = dimension*dimension-len(keyword)
    if disparity > 0:
        # add elements to list so length of the keyword is the same length as the length of the dimension squared
        for i in disparity:
            keyword.append(id.alphabet[i])
    # convert from letters to numbers
    for i in range(dimension*dimension):
        keynum.append(id.alph_to_num[keyword[i]])
    # the keymatrix
    keymatrix = n.asarray(keynum).reshape(dimension, dimension)
    return keymatrix

def text_to_matrix(text, dimension):
    num = []
    # convert from letters to numbers
    for i in text:
        num.append(id.alph_to_num[i])
    # plainmatrix's values
    if len(text)%dimension != 0:
        for i in range(len(text)%dimension):
            num.append(25)
    # the plainmatrix
    matrix = n.transpose(n.asarray(num).reshape(int(len(text)/2+len(text)%2),2))
    return matrix
