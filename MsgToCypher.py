#!/usr/bin/env python3

"""
ChaCha20-Poly1305 script (Post-Quantum safe - symmetric)

* Generate key and nonce
* Encrypt
* Decrypt
"""

import secrets
import sys
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305


# Générer une clé ChaCha20-Poly1305 (256 bits)
def generer_cle():
    return ChaCha20Poly1305.generate_key()


# Générer un nonce (12 octets recommandés)
def generer_nonce():
    return secrets.token_bytes(12)


# Chiffrer une chaîne de caractères
def chiffre_message(cle, nonce, message):
    message = message.encode()
    chacha = ChaCha20Poly1305(cle)
    ct = chacha.encrypt(nonce, message, None)
    return ct


# Déchiffrer un message
def dechiffre_message(cle, nonce, ct):
    chacha = ChaCha20Poly1305(cle)
    message = chacha.decrypt(nonce, ct, None)
    return message.decode()


if __name__ == "__main__":

    if len(sys.argv) != 2 and len(sys.argv) != 5:
        print("Usage to encrypt with random key: <script> <msg>")
        print("Usage to encrypt: <script> enc <msg> <key_hex> <nonce_hex>")
        print("Usage to decrypt: <script> dec <cipher_hex> <key_hex> <nonce_hex>")
        print("\nExemple :")
        print("python ./MsgToCypher.py test")
        print("python ./MsgToCypher.py enc test "
              "9CEA372979FFDCBA028BD523A3F43A44B527DE31E2BBAE56F641D87D3F6C80BC "
              "A977EA111934D65E8A6B5AC3")
        print("python ./MsgToCypher.py dec "
              "EFAADCF7EA0A786EF7B4EF7504605970 "
              "9CEA372979FFDCBA028BD523A3F43A44B527DE31E2BBAE56F641D87D3F6C80BC "
              "A977EA111934D65E8A6B5AC3")
        sys.exit(0)

    # Chiffrement avec clé et nonce aléatoires
    if len(sys.argv) == 2:
        m = sys.argv[1]
        k = generer_cle()
        n = generer_nonce()
        c = chiffre_message(k, n, m)

        print("key:", k.hex().upper())
        print("nonce:", n.hex().upper())
        print("cipherText:", c.hex().upper())

    # Mode explicite enc / dec
    if len(sys.argv) == 5:
        if sys.argv[1] == 'enc':
            m = sys.argv[2]
            k = bytes.fromhex(sys.argv[3])
            n = bytes.fromhex(sys.argv[4])
            c = chiffre_message(k, n, m)

            print("key:", k.hex().upper())
            print("nonce:", n.hex().upper())
            print("cipherText:", c.hex().upper())

        if sys.argv[1] == 'dec':
            c = bytes.fromhex(sys.argv[2])
            k = bytes.fromhex(sys.argv[3])
            n = bytes.fromhex(sys.argv[4])
            m = dechiffre_message(k, n, c)

            print("message:", m)
