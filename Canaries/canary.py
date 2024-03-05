#2 Materiel
plateau4x4= (
            ('J1', 'J2', 'J3', 'J4'),
            ('J5', 'J6', 'J7', 'J8'),
            ('R5', 'R6', 'R7', 'R8'),
            ('R1', 'R2', 'R3', 'R4')
            )

caracteres = "●○"

#3 Deplacements

def est_case_vide(case :tuple):
    x,y = case
    if plateau4x4[y][x] == None:
        return True
    else:
        return False

def est_case_valide(entree :str):
    if len(entree) == 2:
        lettre,nombre = entree
        if (lettre in ordonnees) and (nombre in abscisses):
            valide = True
        else:
            valide = False
    else:
        valide = False
    return valide

def entree_vers_coordonnee(entree):
    ordonnees = {"A":0,"B":1,"C":2,"D":3,"a":0,"b":1,"c":2,"d":3}
    abscisses = {"1":0,"2":1,"3":2,"4":3}

    case = abscisses[entree[1]],ordonnees[entree[0]]
    return case

def est_direction_valide(direction :str):
    if len(direction) == 1 and direction in "hbgd":
        return True
    else:
        return False
    
def haut(case : tuple[int,int]):
    x, y = case
    case = x , y+1
    return case

def bas(case : tuple[int,int]):
    x, y = case
    case = x , y-1
    return case

def gauche(case : tuple[int,int]):
    x, y = case
    case = x-1 , y
    return case

def droite(case : tuple[int,int]):
    x, y = case
    case = x+1 , y
    return case

test = [[None,"haut",None],
        ["gauche","centre","droite"],
        [None,"bas",None]]

#test
#Cases_utilisateur = [[i+str(j) for j in range(1,5)] for i in ["A","B","C","D"]]
#Cases_plateau = [[f'{i}{j}' for j in range(1,5)] for i in range(1,5)]
ordonnees = {"A":0,"B":1,"C":2,"D":3,"a":0,"b":1,"c":2,"d":3}
abscisses = {"1":0,"2":1,"3":2,"4":3}

def pos(poz):
    x,y = poz
    x in [0,1,2,3]

def deplacement(joueur):
    case = str(input(f"Joueur{joueur} entrez les coordonnées du pion : "))
    valide = est_case_valide(case)
    vide = est_case_vide(case)

    if valide == True:
        direction = str(input(f"Joueur{joueur} entrez la direction : "))
        if est_direction_valide(direction):
            match direction:
                case "h":
                    haut(case)
            new_case = directions[direction]
            x,y = new_case
            abscisse,ordonnee = abscisses[x], ordonnees[y]
            print(test[ordonnee][abscisse])
        else:
            print("pblm")
    else:
        print("Les coordonnées ne sont pas conformes, réessayez !")
        deplacement(joueur)
    


deplacement(1)
    
#print(est_case_valide("a1"))

#print(entree_vers_coordonnee("A2"))
#print(haut((1,2)))