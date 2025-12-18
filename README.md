# Travail_du_groupe3
TPE du cours en cloud computing

## Exercice3. Convertisseur de Date

### Problème posé
Il s'agit ici de convertir une date du format **AAAA-MM-JJ** vers **JJ/MM/AAAA** tout en s’assurant que la date saisie est valide.

### Approche de résolution
- La date saisie est d’abord découpée en année, mois et jour.
- Une fonction vérifie si l’année est bissextile afin de gérer correctement le mois de février.
- Le nombre de jours autorisés pour chaque mois est contrôlé.
- Si la date est valide, elle est reformattée vers **JJ/MM/AAAA**.
- Sinon, un message d’erreur est affiché.

### Exemple
Entrée :2024-02-29
Sortie :
29/02/2024


---

## Exercice5. Fonction de Compression de Texte

### Problème posé
La fonction permet de compresser une chaîne de caractères en remplaçant les lettres répétées consécutivement par un compteur.

### Approche de résolution
- Le texte est parcouru caractère par caractère.
- Un compteur est utilisé pour compter les répétitions consécutives d’un même caractère.
- À chaque changement de caractère, la lettre suivie de son compteur est ajoutée au résultat.
- Cette méthode permet de réduire la taille de la chaîne lorsque des répétitions existent.

### Exemple
Entrée :
aaabbccccddff
Sortie:
a3b2c4d2f2




## Exercice19. Détection de Sous-chaînes Palindromiques

### Problème posé
La fonction permet de déterminer le nombre total de sous-chaînes palindromiques présentes dans une chaîne de caractères.

### Approche de résolution
- Toutes les sous-chaînes possibles sont générées à partir de la chaîne saisie.
- Chaque sous-chaîne est comparée à son inverse afin de vérifier si elle est palindromique.
- Un compteur permet de compter le nombre total de sous-chaînes répondant à cette condition.
- Le programme prend la chaîne directement en entrée utilisateur.
- Et affiche le nombre total de sous-chaînes palindromique.

### Exemple
Entrée :abba
Sortie: 6



## Objectif des projets réalisés
Ces projets permettent nous ont permis de :
- pratiquer la manipulation des chaînes de caractères
- comprendre la validation de données
- développer une logique algorithmique claire
- écrire du code structuré et compréhensible



## Exécution
Chaque programme peut être exécuté individuellement avec la commande :
```bash
Groupe_3_TPE_CLoud_2026_Exo3.py
Groupe_3_TPE_CLoud_2026_exo5.py
Groupe_3_TPE_CLoud_2026_exo19.py



MEMBRES DU GROUPE3
GUEBERGUE Donald (23A202FS)          :fonction compression de texte et chef du projet
ISSA Mahamat adam (23A158FS)         :fonction convertisseur de date et membre 
BRAHIM Hissein kitti(23B134FS)       :fonction convertisseur de date et membre 
MOBEL Parfait (23A467FS)             :fonction compression de texte et chef du projet
DJEGOLNOUDJI Elysée (23B363FS)       :fonction detecttion de palindrome dans des sous-chaines 
GUIDEGUE Elysée (22B725FS)           :fonction detecttion de palindrome dans des sous-chaines 
ISSA Mahamat moukour (22A662FS)      :fonction compression de texte et chef du projet
