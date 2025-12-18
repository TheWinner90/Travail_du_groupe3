# Cette fonction vérifie si une chaîne est un palindrome
def est_palindrome(s):
    return s == s[::-1]


# Cette fonction compte le nombre total de sous-chaînes palindromiques
def compter_sous_chaines_palindromiques(chaine):

    n = len(chaine)      # Longueur de la chaîne
    compteur = 0         # Compteur de palindromes

    # Parcours de toutes les sous-chaînes possibles
    for i in range(n):
        for j in range(i + 1, n + 1):

            # Extraction de la sous-chaîne
            sous_chaine = chaine[i:j]

            # Vérification du palindrome
            if est_palindrome(sous_chaine):
                compteur += 1

    return compteur


# Point d'entrée du programme
if __name__ == "__main__":

    # Demande à l'utilisateur d'entrer une chaîne
    texte = input("Entrez une chaîne de caractères : ")

    # Calcul du nombre de sous-chaînes palindromiques
    resultat = compter_sous_chaines_palindromiques(texte)

    # Affichage du résultat
    print("Nombre total de sous-chaînes palindromiques :", resultat)
