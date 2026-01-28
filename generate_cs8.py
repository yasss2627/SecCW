from MsgToCypher import generer_cle, chiffre_message
from CWToCS8 import convert_to_CW, write_toCS8

# 1️⃣ Votre message
message = "Merci Mickael"

# 2️⃣ Générer une clé
cle = generer_cle()

# 3️⃣ Chiffrement OTP-SHA3
ct = chiffre_message(cle, message)

# 4️⃣ Transformer en hex pour Morse
texte_a_transmettre = ct.hex().upper()

# 5️⃣ Convertir en signal CW (AM ou FM)
signal_iq = convert_to_CW(texte_a_transmettre, modulation='AM')

# 6️⃣ Écrire le fichier CS8
write_toCS8(signal_iq, "output.cs8")

print("CS8 généré : output.cs8")
print("clé hex :", cle.hex().upper())
print("ciphertext hex :", ct.hex().upper())
