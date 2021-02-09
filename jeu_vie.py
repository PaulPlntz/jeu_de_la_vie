from ast import literal_eval

class Jeu :
    # choix dans le code des cellules vivantes
    def initialiser_Cellules(self, liste_cellules):
        for (i,j) in liste_cellules:
            self.matrice[i][j] = 1
        
    def __init__(self, nb_lignes, nb_colonnes):
        self.nbIterations = 1
        self.matrice = []
        for i in range(0,nb_lignes):
            self.matrice.append([0]*nb_colonnes)

    # affichage graphique dans l'invite de commande
    def afficher_Grille(self):
        #print("\n")
        for i in range(0,len(self.matrice)) :
            for j in range(0,len(self.matrice[0])) :
                if (self.matrice[i][j] == 0):
                    print("|___",end="")
                else:
                    print("|_x_",end="")
            print("|")

    # Obtenir la "nombre de voisins" d'une cellule dans une grille
    # input : matrice m, int ligne, int colonne
    # output : int nbVoisins
    def get_Nombre_Voisins(self, m, ligne, colonne):
        nbVoisins = 0
        i_max = len(m)-1
        j_max = len(m[0])-1
        for i in range(ligne-1,ligne+2):
            if not(i<0 or i>i_max) :
                for j in range(colonne-1,colonne+2):
                    if (not(j<0 or j>j_max) and not(i==ligne and j==colonne) and (m[i][j]==1)):
                        nbVoisins += 1
        return nbVoisins       

    # Obtenir la grille de jeu mise à jour
    def get_Updated_Grille(self):
        old_m = self.matrice
        new_m = [ligne_m[:] for ligne_m in old_m]
        ind_ligne_max = len(old_m)
        ind_colonne_max = len(old_m[0])
        for indice_ligne in range(0, ind_ligne_max):
            for indice_colonne in range(0, ind_colonne_max):
                etatCellule = old_m[indice_ligne][indice_colonne]
                nbVoisins = self.get_Nombre_Voisins(old_m, indice_ligne, indice_colonne)
                # naissance d'une nouvelle cellule
                if ((etatCellule == 0) and (nbVoisins == 3)):
                    new_m[indice_ligne][indice_colonne] = 1
                # mort d'une ancienne cellule
                elif ((etatCellule == 1) and (nbVoisins not in {2,3})):
                    new_m[indice_ligne][indice_colonne] = 0
        return new_m

    def update_Grille(self):
        self.matrice = self.get_Updated_Grille()
        self.nbIterations += 1


def main() :
    print("\nBIENVENUE DANS LE JEU DE LA VIE !")
    input("\nAppuyez sur une touche pour commencer.")

    loopTailleGrille = True
    while (loopTailleGrille):
        try:
            taille_grille = int(input("\nChoisir la taille (un entier) de la grille : "))
            if (taille_grille <= 0):
                print("La taille doit être strictement supérieure à 0.")
            else:
                loopTailleGrille = False
                print("La taille a bien été initialisée et vaut "+str(taille_grille)+".\n")
        except (TypeError, ValueError):
            print("La taille doit être un entier supérieur à 0, veuillez réessayer.")
    notreJeu = Jeu(taille_grille,taille_grille)

    cellules_initiales = []
    #cellules_initiales = [(13,3),(13,4),(14,4),(15,4),(16,4),(16,5),(17,5)]
    boolLoopInitCell = True
    while (boolLoopInitCell) :
        try:
            strInput = input ("Insérer une cellule dans la grille au format '(i,j)', où i et j sont les coordonnées de ligne et de colonne de la cellule : ")
            objInput = literal_eval(strInput)
            if (type(objInput)==tuple and len(objInput)==2 and type(objInput[0])==int and type(objInput[1])==int):
                if (objInput[0]<0 or objInput[0]>=taille_grille or objInput[1]<0 or objInput[1]>=taille_grille):
                    print("Les coordonnées d'une cellule doivent être compris entre 0 et "+str(taille_grille-1))
                else :
                    cellules_initiales.append(objInput)
                    end = input("\nOn place une nouvelle cellule ? ('n' pour finir l'initialisation des cellules) \n")
                    boolLoopInitCell = not(end == "n")
            else :
                print("Entrée invalide, mauvais format de cellule")
        except (SyntaxError, ValueError, NameError, TypeError, ZeroDivisionError):
            print("Entrée invalide, mauvais format de cellule")
    notreJeu.initialiser_Cellules(cellules_initiales)

    print("\nEtat initial du jeu :")
    notreJeu.afficher_Grille()
    inpFin = input("\nOn continue ? ('n' pour finir le jeu) \n")
    end = (inpFin == 'n')
    while (not end) :
        print("\nIteration n°"+str(notreJeu.nbIterations)+" :")
        notreJeu.update_Grille()
        notreJeu.afficher_Grille()
        inpFin = input("\nOn continue ? ('n' pour finir le jeu) \n")
        end = (inpFin == 'n')

if __name__=='__main__' :
    main()
