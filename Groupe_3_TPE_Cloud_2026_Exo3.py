# Cette fonction vérifie si une année est bissextile
# Une année est bissextile si :
# - elle est divisible par 4
# - sauf si elle est divisible par 100
# - sauf si elle est divisible par 400
def est_bissextile(annee):
    return (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0)


# Cette fonction vérifie si une date donnée est valide
# Elle reçoit : année, mois et jour
def date_valide(annee, mois, jour):

    # Dictionnaire contenant le nombre de jours pour chaque mois
    # Février dépend de l'année (bissextile ou non)
    jours_par_mois = {
        1: 31,                                  # Janvier
        2: 29 if est_bissextile(annee) else 28, # Février
        3: 31,                                  # Mars
        4: 30,                                  # Avril
        5: 31,                                  # Mai
        6: 30,                                  # Juin
        7: 31,                                  # Juillet
        8: 31,                                  # Août
        9: 30,                                  # Septembre
        10: 31,                                 # Octobre
        11: 30,                                 # Novembre
        12: 31                                  # Décembre
    }

    # Vérifie si le mois est compris entre 1 et 12
    if mois < 1 or mois > 12:
        return False

    # Vérifie si le jour est valide pour le mois donné
    if jour < 1 or jour > jours_par_mois[mois]:
        return False

    # Si toutes les vérifications sont correctes
    return True


# Cette fonction convertit une date du format AAAA-MM-JJ
# vers le format JJ/MM/AAAA après avoir vérifié sa validité
def convertir_date(date_str):
    try:
        # Séparation de la date en année, mois et jour
        annee, mois, jour = map(int, date_str.split("-"))
    except ValueError:
        # Si le format n'est pas respecté
        return "Format invalide. Utilisez AAAA-MM-JJ."

    # Vérifie si la date est valide
    if not date_valide(annee, mois, jour):
        return "Date invalide."

    # Conversion vers le format JJ/MM/AAAA
    return f"{jour:02d}/{mois:02d}/{annee}"


# Point d'entrée du programme
# Ce code s'exécute seulement si le fichier est lancé directement
if __name__ == "__main__":
    # Demande à l'utilisateur d'entrer une date
    date = input("Entrez une date (AAAA-MM-JJ) : ")

    # Affiche le résultat de la conversion
    print("Résultat :", convertir_date(date))
