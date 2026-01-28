#!/usr/bin/env python3
"""
MsgToCypher.py - Post-quantum minimal ciphertext (OTP-like SHA-3)

* Generate key/seed
* Encrypt via XOR stream
* Decrypt
"""

import sys
import secrets
import hashlib

# Générer une clé/seed pour le flux pseudo-aléatoire
def generer_cle(taille=32):
    return secrets.token_bytes(taille)

# Générer un flux pseudo-aléatoire à partir de la clé/seed
def flux_pseudo_aleatoire(cle, taille_message):
    # On utilise SHA3-256 en mode counter
    counter = 0
    flux = b""
    while len(flux) < taille_message:
        h = hashlib.sha3_256(cle + counter.to_bytes(4, 'big')).digest()
        flux += h
        counter += 1
    return flux[:taille_message]

# Chiffrer un message
def chiffre_message(cle, message):
    message_bytes = message.encode()
    flux = flux_pseudo_aleatoire(cle, len(message_bytes))
    ct = bytes([b ^ f for b, f in zip(message_bytes, flux)])
    return ct

# Déchiffrer un message
def dechiffre_message(cle, ct):
    flux = flux_pseudo_aleatoire(cle, len(ct))
    message_bytes = bytes([b ^ f for b, f in zip(ct, flux)])
    return message_bytes.decode()

if __name__ == "__main__":

    if len(sys.argv) != 2 and len(sys.argv) != 3 and len(sys.argv) != 4:
        print("Usage encrypt random key: <script> <msg>")
        print("Usage encrypt with key: <script> enc <msg> <key_hex>")
        print("Usage decrypt: <script> dec <cipher_hex> <key_hex>")
        sys.exit(0)

    # Chiffrement avec clé aléatoire
    if len(sys.argv) == 2:
        msg = sys.argv[1]
        cle = generer_cle()
        ct = chiffre_message(cle, msg)
        print("key:", cle.hex().upper())
        print("cipherText:", ct.hex().upper())

    # Mode explicite enc / dec
    if len(sys.argv) == 4:
        if sys.argv[1] == 'enc':
            msg = sys.argv[2]
            cle = bytes.fromhex(sys.argv[3])
            ct = chiffre_message(cle, msg)
            print("key:", cle.hex().upper())
            print("cipherText:", ct.hex().upper())

        if sys.argv[1] == 'dec':
            ct = bytes.fromhex(sys.argv[2])
            cle = bytes.fromhex(sys.argv[3])
            msg = dechiffre_message(cle, ct)
            print("message:", msg)
