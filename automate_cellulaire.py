import pygame
import time
import os


# initialisation de la taille de la fenêtre et de la fenêtre de jeu
taille_win = (900, 900)
win = pygame.display.set_mode((taille_win))


def binaire(nb:int)->str:
    """
    converti un nombre décimale en binaire 8bit
    """
    return [str(i) for i in format(nb,'08b')]


def voisins(liste:list, i:int)->list:
    """
    Met la valeur des voisins dans une liste
    """
    liste_voisins = []
    for x in range(-1,2):
        if 0 <= i+x <= len(liste)-1:
            if liste[i+x] == '1':
                liste_voisins.append('1')
            else:
                liste_voisins.append('0')
        else:
            liste_voisins.append('0')
    return liste_voisins



def applique_regle(liste:list, i:int, regle:list)->int:
    """
    Renvoie 0 ou 1 selon la règles
    """
    # Définit les possibilités de configurations de voisins
    liste_possibilite = [['1','1','1'],['1','1','0'],['1','0','1'],['1','0','0'],['0','1','1'],['0','1','0'],['0','0','1'],['0','0','0']]
    # 8 possibilités binaire des possibilités
    for i_possibilite in range(8):
        # Vérifie voisins et applique règle
        
        if voisins(liste, i) == liste_possibilite[i_possibilite]:
            return regle[i_possibilite]



def vie(liste:list, regle:list)->list:
    """
    Effectue une itération de l'automate cellulaire
    """
    nv_liste = []
    # Parcours la ligne de jeu
    for i_liste in range(len(liste)):
        # Applique la règle
        nv_liste.append(applique_regle(liste,i_liste,regle))

    return nv_liste



def affiche(historique:list)->None:
    """
    Affiche la ligne de jeu avec pygame
    """
    taille_case = taille_win[0] / len(historique[0])

    if len(historique)*taille_case >= taille_win[1]:
        historique.pop(0)
    i = len(historique)-1

    win.fill((255,255,255))

    for y in range(i+1):
        for x in range(len(historique[0])):
            if historique[y][x] == '1':
                pygame.draw.rect(win, (0,0,0), [x*taille_case, y*taille_case, taille_case, taille_case])
            # elif historique[y][x] == '0':
            #     pygame.draw.rect(win, (255,255,255), [x*taille_case, y*taille_case, taille_case, taille_case])
    pygame.display.flip()



def jeu(liste:list, nb_regle:list)->None:
    """
    Effectue le jeu de l'automate cellulaire
    """
    regle = binaire(nb_regle)
    print(regle)
    historique = []

    while True:
        # Events
        for event in pygame.event.get():
            # Fermeture si ferme la page
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
        historique.append(liste)
        affiche(historique)
        liste = vie(liste, regle)
        time.sleep(0.01)
        
BestOfTheBest = [22, 129, 169, 225]
Best = [21, 30, 131, 135, 137, 143, 146, 150, 151, 153, 158, 161, 165, 167, 177, 178, 182, 183, 185, 190, 193, 210, 213, 218, 227, 246]

longueur = 300
liste = ['1' if i == longueur//2 else '0' for i in range(longueur)]

regle = -1
while not 0 <= regle <= 255:
    os.system('cls')
    regle = int(input("Choisissez une règle entre 0 et 255 : "))

jeu(liste, regle)

pygame.quit()
quit()