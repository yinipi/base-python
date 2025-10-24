import os
import json


#declaration d'une listes
menu = []

#recuperer le chemin courant
cur_dir = os.path.dirname(__file__)

#le chemin d'acces au fichier json creer  et jointure sur avec le chemin courant
menu_chemin = os.path.join(cur_dir, 'menu.json')

# ouvetrure du fichier pour les sauvegardes
if os.path.exists(menu_chemin):
    with open(menu_chemin, 'r') as file : # r pour read pour permettre l'ecriture dans le fichier file et qui est transmise dans le fichier json
        menu = json.load(file)


#ajout d'un element dans la liste
option = str(input("entrer un element dans votre menu : "))
menu.append(option)

#afficher les elements de la listes et la taille du tableau
taille = len(menu)
print(f"la taille du tableau est : {taille}")

#remplire le tableau de facon sequence
nbre_elements = int(input("entrer un nombre d'element du menu :"))
for i in range(nbre_elements):
    # demande un element a l'utilisateur et l'ajoute diretement dans la liste
    menu.append(str(input("entrer un element dans votre menu : ")))

    # ou encore
    # element = str(input("entrer un element dans votre menu " )
    # menu.append(element)

# afficher tout les elements du menu
print("** MENU **")
for i in range(nbre_elements):
    print(f"{i}. {menu[i]}")

#supprimer un element dans la liste
supp = str(input("entrer le nom de l'element a supprimer du menu "))
for i in range(nbre_elements):
    if supp == menu[i]:
        menu.remove(supp)
        print(f"{supp} supprimer avec success")


print(f"la taille du menu est : {len(menu)}")

#stocker les valeurs de la liste dans un fichier json
with open(menu_chemin, 'w') as file :
    json.dump(menu, file,indent=4)
    print(f"sauvegarde reussir ")
