import numpy as np

class MatrixNotInvertible(Exception):
    pass

class HillCipher:
    def __init__(self, key_matrix, modulus):
        self.key_matrix = key_matrix
        self.modulus = modulus

    def determinant(self, key_matrix):
        return int(round(np.linalg.det(key_matrix))) % self.modulus

    def invertible(self, key_matrix):
        if key_matrix.shape[0] != key_matrix.shape[1]:
            raise MatrixNotInvertible("The matrix is not square.")
        determinant = self.determinant(key_matrix)
        if determinant == 0:
            raise MatrixNotInvertible("The determinant = 0.")
        return True
    
    def mod_inverse(self, determinant, modulus):
        for i in range(1, modulus):
            if (determinant * i) % modulus == 1:
                return i
        return None
            
    def encode(self, str_):
        encoding_dict = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7,
                         'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15,
                         'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24,
                         'Z': 25}
        encoded = []
        for char in str_:
            encoded.append(encoding_dict[char])
        return np.array(encoded).reshape(-1, 1)

    def decode(self, str_):
        decoding_dict = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H',
                         8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P',
                         16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y',
                         25: 'Z'}
        decoded = []
        for num in str_:
            decoded.append(decoding_dict[num])
        return ''.join(decoded)

    def encrypt(self, plaintext, key):
        ciphertext = np.dot(key, plaintext) % self.modulus
        return ciphertext

    def get_decryption_key(self, key):
        determinant = self.determinant(key)
        mod_inverse = self.mod_inverse(determinant, self.modulus)
        key_inv = np.linalg.inv(key)
        decryption_key = (determinant * mod_inverse * key_inv) % self.modulus
        return decryption_key

    def decrypt(self, ciphertext, decryption_key):
        plaintext = np.dot(decryption_key, ciphertext) % self.modulus
        return plaintext