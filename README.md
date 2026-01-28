# SecCW – Chiffrement et transmission Morse (CS8)

## Objectif
Fork du projet **SecCW** avec modification de l’algorithme de chiffrement afin de :
- Réduire la taille des messages transmis en Morse
- Remplacer AES-CBC par un chiffrement moderne plus adapté au flux
- Générer et transmettre des fichiers **CS8** exploitables en SDR

---

## Modifications apportées

### 1 MsgToCypher.py
- Suppression de **AES-CBC + PKCS7**
- Remplacement par **ChaCha20‑Poly1305**
- Suppression du padding (chiffrement par flux)
- Remplacement de l’IV par un **nonce (96 bits)**
- Authentification intégrée (confidentialité + intégrité)
- Message chiffré plus court et mieux adapté à la transmission Morse


Fonctions modifiées :
- `chiffre_message(cle, nonce, message)`
- `dechiffre_message(cle, nonce, ct)`
Voir le code directement et comparer les modifications avec l'original.

---

### 2 CWToCS8.py
- Aucune modification de l’algorithme Morse
- Utilisation directe du message chiffré en entrée
- Vérification du bon fonctionnement par génération et lecture SDR
Voir le code directement et comparer les modifications avec l'original.
---

### 3 generate_cs8.py
- Génération d’un fichier **.cs8** dans le dossier d’exécution

## Génération d’un fichier CS8
```bash
python generate_cs8.py "<message_chiffré>" output.cs8 AM
```

Le fichier output.cs8 est créé dans le répertoire python.

Test matériel (HackRF)

Test réalisé avec un HackRF One en clonant le projet suivant :
https://github.com/fl1ckje/HackRF-tools

Commande utilisée pour jouer le signal CS8 :

.\hackrf_transfer.exe -s 8000000 -x 47 -g 60 -l 40 -a 1 -f 26975000 -b 1750000 -t "C:\Users\yyabo\Desktop\PC\cours\4 ESGI\python\output.cs8"


Le signal Morse chiffré est correctement transmis lors du test effectué avec Michaël.