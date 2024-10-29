import numpy as np
from hillcipher import HillCipher, MatrixNotInvertible

inputs = [
    {   "plaintext": "ATTACKATDAWN",
        "key_matrix": np.array([[19, 8, 4], [3, 12, 7]]),
        "modulus": 26,
        "invertible": "The matrix is invertible.",
        "decrypt_key_error": "The determinant = 0."
    },
    {   "plaintext": "ATTACKATDAWN",
        "key_matrix": np.array([[7, 8], [11, 11]]),
        "modulus": 26,
        "invertible": "The matrix is invertible.",
        "decrypt_key_error": "The determinant = 0."
    },
    {   "plaintext": "ATTACKATDAWN",
        "key_matrix": np.array([[5, 15], [4, 12]]),
        "modulus": 26,
        "invertible": "The matrix is not invertible.",
        "decrypt_key_error": "The determinant = 0."
    }
]

for input_data in inputs:
    plaintext = input_data["plaintext"]
    key_matrix = input_data["key_matrix"]
    modulus = input_data["modulus"]
    hc = HillCipher(key_matrix, modulus)

    if key_matrix.shape[0] != key_matrix.shape[1]:
        print("The matrix is not square.")
        continue

    try:
        hc.invertible(key_matrix)
    except MatrixNotInvertible as e:
        print("The matrix is not invertible.")
    else:
        print(input_data["invertible"])

    plaintext_vectors = [hc.encode(plaintext[i:i+2]) for i in range(0, len(plaintext), 2)]
    print("Plaintext:", plaintext)
    print("Plaintext column vectors:", plaintext_vectors)

    ciphertext_vectors = [hc.encrypt(plaintext_vectors[i], key_matrix) for i in range(len(plaintext_vectors))]
    ciphertext = ''.join([hc.decode(ciphertext_vectors[i]).strip() for i in range(len(ciphertext_vectors))])
    print("Ciphertext:", ciphertext)
    print("Ciphertext column vectors:", ciphertext_vectors)

    try:
        hc.get_decryption_key(key_matrix)
    except MatrixNotInvertible as e:
        print(input_data["decrypt_key_error"])
    else:
        print("The matrix is invertible.")