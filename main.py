import os

# On definit le chemin du dossier cible
path = "/home/l_kanan/Téléchargements/formation django"
chiffre = ""

# Initialisation du dossier à utiliser pour tous le traitement
os.chdir(path)

# t = "Apprendre Django fonctionnement du setting.py #04 _ formation Django débutant.mp4"
# print(t.replace("#04", ""))
# print("#04"+t)

for file_name in os.listdir():
    print(file_name)
    chiffre = ""
    # La methode rfind() permet de renvoyer la position de la dernière aucurence d'un caractere dans une chaine de caracteres et renvoi -1 si le caractère n'est pas trouvé
    position = file_name.rfind("#")
    if position != -1:
        for i in range(1, 3):
            if file_name[position + i].isdigit():
                chiffre += file_name[position + i]
        print(chiffre)
        new_format_name = file_name.replace("#" + str(chiffre), "")
        # On renome un fichier avec le nom filename en la chaine de caractère 2iem parametre
        os.rename(file_name, "#"+str(chiffre)+new_format_name)
