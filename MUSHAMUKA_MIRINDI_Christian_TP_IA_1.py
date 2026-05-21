# TP num1 : Opérations  de base de calcul en python sur les verteurs et les matrices
# Code ecrit MUSHAMUKA MIRINDI Christian
# Etudiant de BAC2 Génie minier/école des mines

# 1. Rappel sur les opération de base de calcul en général
def addition(a, b):
    resultat = a + b
    return resultat

def soustraction(a, b):
    resultat = a - b
    return resultat

def multiplication(a, b):
    resultat = a * b
    return resultat

def division(a, b):
    if b == 0:
        print("Erreur : Division par zéro !")
        return None
    resultat = a / b
    return resultat

    # 2. Pour les vecteurs 

def addition_vecteurs(v1, v2):
    v_resultat = []
    # On suppose que les deux vecteurs ont la même taille
    for i in range(len(v1)):
        somme = v1[i] + v2[i]
        v_resultat.append(somme)
    return v_resultat

def produit_scalaire(v1, v2):
    total = 0
    for i in range(len(v1)):
        total = total + (v1[i] * v2[i])
    return total

# Exemple pour les vecteurs

vecteur_A = [2, 4, 6]
vecteur_B = [8, 10, 12]
print("Addition vecteurs :", addition_vecteurs(vecteur_A, vecteur_B))

    # 3. Pour les matrices

def addition_matrices(M1, M2):
    M_resultat = []
    nb_lignes = len(M1)
    nb_colonnes = len(M1[0])
    
    for i in range(nb_lignes):
        ligne = []
        for j in range(nb_colonnes):
            somme = M1[i][j] + M2[i][j]
            ligne.append(somme)
        M_resultat.append(ligne)
        
    return M_resultat

# Exemple pour les matrices

matrice_A = [
    [1, 3],
    [5, 7]
]
matrice_B = [
    [9, 11],
    [13, 15]
]
print("Addition matrices :", addition_matrices(matrice_A, matrice_B))