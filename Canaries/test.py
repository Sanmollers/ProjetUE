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

def afficher_abscisse(grille:list):
    abscisses = "  "
    for i in range(1,len(grille)+1):
        abscisses = abscisses+"   "+str(i)
    return abscisses

grille =grille_millieu = [['○', None, '○', '○'], ['○', None, None, '○'], ['●', '○', None, None], [None, None, '●', '●']]

afficher_grille(grille)
print([["○"]*4,["○"]*4,["●"]*4,["●"]*4])