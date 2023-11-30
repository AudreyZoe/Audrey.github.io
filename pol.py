# Fonction de création de la grille de Polybe
def creer_grille_polybe():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    grille = {}
    for i in range(5):
        for j in range(5):
            if len(alphabet) > 0:
                grille[alphabet[0]] = (i + 1, j + 1)
                alphabet = alphabet[1:]
            else:
                grille[str(i) + str(j)] = (i + 1, j + 1)
    return grille

# Fonction de chiffrement avec Polybe


def chiffrement_polybe(message):
    grille = creer_grille_polybe()
    # Convertit en majuscules et remplace J par I
    message = message.upper().replace("J", "I")
    message_chiffre = ""
    for lettre in message:
        if lettre.isalpha() or lettre.isdigit():
            if lettre == "J":
                lettre = "I"
            if lettre != " ":
                message_chiffre += str(grille[lettre][0]) + \
                    str(grille[lettre][1]) + " "
        else:
            message_chiffre += lettre
    return message_chiffre.strip()


# Fonction de déchiffrement avec Polybe
def dechiffrement_polybe(message_chiffre):
    grille = creer_grille_polybe()
    message_dechiffre = ""
    coordonnees = message_chiffre.split()
    for coord in coordonnees:
        ligne = int(coord[0])
        colonne = int(coord[1])
        for lettre, c in grille.items():
            if c == (ligne, colonne):
                if lettre == 'I' or lettre == 'J':
                    # Assurer la cohérence avec le remplacement de I par J et vice versa
                    if 'I' in grille and 'J' in grille:
                        if grille['I'] == (ligne, colonne):
                            message_dechiffre += 'I'
                        elif grille['J'] == (ligne, colonne):
                            message_dechiffre += 'J'
                    else:
                        message_dechiffre += lettre
                else:
                    message_dechiffre += lettre
    return message_dechiffre


# Demander à l'utilisateur d'entrer le message à chiffrer
message_original = input("Entrez le message à chiffrer : ")

message_chiffre = chiffrement_polybe(message_original)
message_dechiffre = dechiffrement_polybe(message_chiffre)

print("Message original :", message_original)
print("Message chiffré :", message_chiffre)
print("Message déchiffré :", message_dechiffre)
