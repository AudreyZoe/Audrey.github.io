def chiffrement_affine(phrase, a, b):
    resultat = ""         
    for caractere in phrase:
        if caractere.isalpha():
            if caractere.islower():
                resultat += chr((a * (ord(caractere) - ord('a')) + b) % 26 + ord('a'))
            else:
                resultat += chr((a * (ord(caractere) - ord('A')) + b) % 26 + ord('A'))
        else:
            resultat += caractere
    return resultat

# Exemple d'utilisation
phrase_a_chiffrer = input('Entrez la phrase à chiffer : ')
a = 5
b = int(input('Entrez le décalage : '))
phrase_chiffree = chiffrement_affine(phrase_a_chiffrer, a, b)
print("Phrase chiffrée:", phrase_chiffree)