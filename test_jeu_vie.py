import jeu_vie

def test_creation_jeu():
    for nb_lignes in range(1,101):
        for nb_colonnes in range(1,101):
            jeu_test = jeu_vie.Jeu(nb_lignes, nb_colonnes)
            grille = jeu_test.matrice
            assert (len(grille) == nb_lignes)
            assert (len(grille[0]) == nb_colonnes)
            for i in range(0,nb_lignes):
                for j in range(0,nb_colonnes):
                    assert (grille[i][j] == 0)

def test_initialisation_cellules():
    jeu_test_1 = jeu_vie.Jeu(10,10)
    cellules_test_1 = [(0,0), (0,1), (1,0), (3,4), (0,9), (9,0), (9,9)]
    jeu_test_1.initialiser_Cellules(cellules_test_1)
    grille = jeu_test_1.matrice
    assert (grille[i][j] == 1 for (i,j) in cellules_test_1)
    for i in range(0,10):
        for j in range(0,10): 
            if ((i,j) not in cellules_test_1):
                assert (grille[i][j]==0)

    # toutes les cellules sont mortes
    jeu_test_2 = jeu_vie.Jeu(10,10)
    cellules_test_2 = []
    jeu_test_2.initialiser_Cellules(cellules_test_2)
    assert (jeu_test_2.matrice == [[0]*10]*10)

    # toutes les cellules sont vivantes
    jeu_test_3 = jeu_vie.Jeu(10,10)
    cellules_test_3 = [(i,j) for i in range (0,10) for j in range(0,10) ]
    jeu_test_3.initialiser_Cellules(cellules_test_3)
    assert (jeu_test_3.matrice == [[1]*10]*10)

def test_nombre_voisins():
    jeu_test_1 = jeu_vie.Jeu(10,10)
    cellules_test_1 = [(0,7), (0,8), (3,1), (3,2), (4,1), (5,1), (9,9)]
    jeu_test_1.initialiser_Cellules(cellules_test_1)
    grille1 = jeu_test_1.matrice
    assert(jeu_test_1.get_Nombre_Voisins(grille1, 0, 0) == 0)
    assert(jeu_test_1.get_Nombre_Voisins(grille1, 1, 7) == 2)
    assert(jeu_test_1.get_Nombre_Voisins(jeu_test_1.matrice, 1, 7) == 2)
    assert(jeu_test_1.get_Nombre_Voisins(grille1, 0, 9) == 1)
    assert(jeu_test_1.get_Nombre_Voisins(grille1, 4, 0) == 3)
    assert(jeu_test_1.get_Nombre_Voisins(grille1, 2, 1) == 2)
    assert(jeu_test_1.get_Nombre_Voisins(grille1, 4, 2) == 4)
    assert(jeu_test_1.get_Nombre_Voisins(grille1, 6, 1) == 1)
    assert(jeu_test_1.get_Nombre_Voisins(grille1, 9, 8) == 1)

def test_updated_matrice():
    jeu_test_1 = jeu_vie.Jeu(10,10)
    cellules_test_1 = [(4,3), (4,4), (4,5)]
    jeu_test_1.initialiser_Cellules(cellules_test_1)
    grille1 = jeu_test_1.matrice

    grille2 = []
    for i in range(0,10):
        grille2.append([0]*10)
    cellules_test_2 = [(3,4),(4,4),(5,4)]
    for (i,j) in cellules_test_2:
        grille2[i][j] = 1

    assert(jeu_test_1.get_Updated_Grille() == grille2)

def main():
    print("Ce script sert à tester mon jeu.")
    #test_creation_jeu()
    #test_initialisation_cellules()
    test_nombre_voisins()
    test_updated_matrice()
    print("Pas d'erreur.")

if __name__=='__main__' :
    main()