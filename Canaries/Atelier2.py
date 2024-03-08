# -*- coding: utf-8 -*- ## Pour s’assurer de la compatiblite entre correcteurs

#### REPRESENTATION DES DONNEES
###initialisation des grilles et autres variables de jeu
grille_debut = [["○"]*4,["○"]*4,["●"]*4,["●"]*4]
grille_millieu = [['○', None, '○', '○'], ['○', None, None, '○'], ['●', '○', None, None], [None, None, '●', '●']]

ordonnees = {"A":0,"B":1,"C":2,"D":3,"a":0,"b":1,"c":2,"d":3}
abscisses = {"1":0,"2":1,"3":2,"4":3}
#### REPRESENTATION GRAPHIQUE

def afficher_abscisse(grille:list):
    abscisses = "  "
    for i in range(1,len(grille)+1):
        abscisses = abscisses+"   "+str(i)
    return abscisses

def afficher_grille(grille:list) :
    taille = len(grille)
    print(afficher_abscisse(grille))
    for i in range(len(grille)):
        print("   -"+"----"*taille)
        print(f"{i+1} ", end='')
        for j in range(len(grille[i])):
            if grille[i][j] != None:
                print(" | "+str(grille[i][j]), end='')
            else:
                print(" | "+" ", end='')
        print(" |")
    print("   -"+"----"*taille)


#### SAISIE
###fonctions de verification
#jeux de tests
def test_est_dans_grille():
assert ...

#verification dans grille
def est_dans_grille(entree :str):
    if len(entree) == 2:
        lettre,nombre = entree
        if (lettre in ordonnees) and (nombre in abscisses):
            valide = True
        else:
            valide = False
    else:
        valide = False
    return valide

###fonctions de saisie
def saisir_coordonnees(...) :
...

#### CODE PRINCIPAL
# execution affichage sur les 3 grilles et autres variables de jeux
afficher_grille(grille...)
afficher_grille(grille...)
afficher_grille(grille...)

#execution test est_dans_grille
test_est_dans_grille() #uniquement pour la mise au point, a conserver pour le correcteur

#affichage des coordonnees saisies
print(saisir_coordonnees( ... ))