def compresser_texte(texte):
    # Si le texte est vide, on retourne une chaîne vide
    if not texte:
        return ""

    resultat = ""
    compteur = 1

    # Parcours du texte à partir du deuxième caractère
    for i in range(1, len(texte)):
        if texte[i] == texte[i - 1]:
            compteur += 1
        else:
            # On ajoute la lettre suivie de son compteur
            resultat += texte[i - 1] + str(compteur)
            compteur = 1

    # Ajout du dernier caractère et de son compteur
    resultat += texte[-1] + str(compteur)

    return resultat


# Exemple d'utilisation
texte = "aaabbcccc"
print(compresser_texte(texte))
