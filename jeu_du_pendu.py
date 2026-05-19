'''
Permet de jouer au jeu du pendu.
Un seul import est requis pour faire fonctionner ce code : import random
Deux choix seront possibles. Utiliser une liste de mots incluse ou la fournir.
Pour simplifier la résolution, les majuscules/minuscules et accents sont assimilés à la même lettre.
6 chances sont disponibles.
Vous pouvez jouer et relancer, c'est parti !
'''

import random # permet d'utiliser la fonction random pour choisir un mot aléatoire

''' Cette fonction à pour but de ressortir la liste de mots extraite du fichier texte demandé. Il faut que le document
renseigné soit dans le répertoire de travail.
'''
def selection_mots():
    print("Le document à utiliser doit être de type .txt et il faut ajouter l'extension lorsque le nom est donné.")
    print("Il y a un mot par ligne dans le document à utiliser.")
    emplacement_mots = input("Renseignez le nom du document à utiliser : ")
    if isinstance(emplacement_mots, str) : # Confirme qu'une chaîne de caractère permette de remonter au fichier

        try: # On essaie d'ouvrir le fichier
            with open(emplacement_mots, 'r', encoding='utf-8') as mots_pendu_source:
                mots_pendu_liste = mots_pendu_source.readlines() # On organise le document en forme de liste

        except FileNotFoundError: # Le fichier ne marche pas / aucun fichier n'a été renseigné
            print("Le document n'est pas dans ce répertoire. Choix de la liste par défaut")
            with open('mots_pendu.txt', 'r', encoding='utf-8') as mots_pendu_source:
                mots_pendu_liste = mots_pendu_source.readlines()

    else :
        with open('mots_pendu.txt', 'r', encoding='utf-8') as mots_pendu_source:
            mots_pendu_liste = mots_pendu_source.readlines()

    mots_selectionne = random.choice(mots_pendu_liste)

    return mots_selectionne