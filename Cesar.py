print("CHIFFREMENT DE CESAR")
print("Ce programme permet de chiffrer et de déchiffrer des messages.")

# Demande à l'utilisateur d'entrer le texte à chiffrer
message_a_coder = input("Rentrez votre texte à chiffer :")

# Demande à l'utilisateur d'entrer la clé
while True:
    try:
        clef = int(input("Rentrez votre clé :"))
        break
    except ValueError:
        print("Veuillez entrer un nombre entier valide pour la clé.")

# Chiffrement
message_chiffré = [(ord(i)+clef) for i in message_a_coder]
message_chiffré_final = "".join([chr(i) for i in message_chiffré])
print("Message chiffré : ", message_chiffré_final)

# Demande à l'utilisateur d'entrer le texte à déchiffrer
message_a_coder = input("Rentrez votre texte à déchiffrer :")

# Déchiffrement
message_déchiffré = [(ord(i)-clef) for i in message_chiffré_final]
message_déchiffré_final = "".join([chr(i) for i in message_déchiffré])
print("Message déchiffré : ", message_déchiffré_final)
