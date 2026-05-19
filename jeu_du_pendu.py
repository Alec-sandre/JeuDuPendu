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

    mot_selectionne = random.choice(mots_pendu_liste)

    return mot_selectionne

def jeu_pendu(mot_a_deviner) : # Fonction qui effectue le jeu à partir d'un mot en entrée
    print(mot_a_deviner)
    print("Mot à deviner : ")
    avancement_mots = "_" * len(mot_a_deviner)
    affichage = avancement_mots
    print(avancement_mots)
    lettre_trouvee = []
    mot_trouve = False # Condition boucle while
    nbre_de_vie = 6
    lettres_essayees = [] # Pour éviter de répéter la même lettre

    while not mot_trouve and nbre_de_vie > 0: # Il faut avoir des vies et que le mot ne soit pas trouvé
        print("La lettre à essayer doit être en minuscule et sans accent")
        lettre_entree = input("Entrez une lettre : ")
        if lettre_entree not in lettres_essayees : # Evite répétition
            lettres_essayees.append(lettre_entree)
            if lettre_entree in mot_a_deviner :
                lettre_trouvee.append(lettre_entree)
                affichage = ""
                for lettre in mot_a_deviner :
                    if lettre in lettres_essayees :
                        affichage += lettre
                    else :
                        affichage += "_"
                print(affichage)
            else :
                nbre_de_vie -= 1
                print(f"La lettre {lettre_entree} est incorrecte. Nombre de vie restante {nbre_de_vie}.")
        else :
            print("Lettre déjà essayée. Renseignez-en une nouvelle.")
            print(affichage)

    # Affichage condition de sortie
    if(nbre_de_vie == 0) :
        print("Vous avez perdu.")
    else :
        print(f"Vous avez gagné ! Le mot était : {mot_a_deviner}.")


jeu_pendu(selection_mots())
