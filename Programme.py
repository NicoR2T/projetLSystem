#!/usr/bin/env python3
"""
Programme L-System
Auteur: Gauthier CUSSONNEAU - Nicolas TIREL
But: A partir d'un fichier d'entrée, ce programme génère un programme python qui sera capable de construire un dessin grâce au module tortle
"""


import sys #Ce module servira à stopper le programme en cas d'erreur

"""
Nom de la fonction: lecture
Auteur: Gauthier CUSSONNEAU
But: Ouvrir un fichier en mode lecture
"""
def lecture(fichier):
    return open(fichier,"r")

"""
Nom de la fonction: fermeture
Auteur: Gauthier CUSSONNEAU
But: Fermer un fichier ouvert auparavant
"""
def fermeture(fichier):
    return fichier.close()

"""
Nom de la procédure: InitialisationLecture
Auteur: Gauthier CUSSONNEAU
But: Initialise la lecture du fichier d'entrée
"""
def InitialisationLecture(fichier):
    global lirefichier, axiomeTrouvé, niveauTrouvé, tailleTrouvé, reglesTrouvé, angleTrouvé
    try:
        lirefichier = lecture(fichier)
    except:
        print("Le fichier "+str(fichier)+" n'existe pas ou n'est pas dans le même dossier que le programme")
        sys.exit()
    axiomeTrouvé = niveauTrouvé = tailleTrouvé = reglesTrouvé = angleTrouvé = False

"""
Nom de la fonction: condition
Auteur: Nicolas TIREL
But: Lire le fichier une première fois afin de vérifier si celui-ci est bien renseigné
"""
def condition(fichier, début, fin):
    global nombreRegles, axiomeTrouvé, niveauTrouvé, tailleTrouvé, reglesTrouvé, angleTrouvé
    print(début)
    if début==fin:
        fermeture(lirefichier)
    elif début[0:10]=="axiome = \"" and axiomeTrouvé == False:
        axiomeTrouvé = True
        return condition(fichier, lirefichier.readline(), "")
    elif début[0:8]=="regles =" and reglesTrouvé == False:
        nombreRegles = 0
        reglesTrouvé = True
        return condition(fichier, lirefichier.readline(), "")
    elif début[0] == "\"" and reglesTrouvé == True:
        nombreRegles = nombreRegles + 1
        return condition(fichier, lirefichier.readline(), "")
    elif début[0:8]=="angle = " and angleTrouvé == False:
        angleTrouvé = True
        return condition(fichier, lirefichier.readline(), "")
    elif début[0:9]=="taille = " and tailleTrouvé == False:
        tailleTrouvé = True
        return condition(fichier, lirefichier.readline(), "")
    elif début[0:9]=="niveau = " and niveauTrouvé == False:
        niveauTrouvé = True
        return condition(fichier, lirefichier.readline(), "")
    else:
        print("Le fichier d'entrée est mal renseigné!")
        fermeture(lirefichier)
        sys.exit()

"""
Nom de la fonction: TrierAxiome
Auteur: Gauthier CUSSONNEAU
But: Trouver et récuperer l'axiome dans le fichier
"""
def TrierAxiome():
    lirefichier=lecture(fichier)
    ligne = lirefichier.readline()
    while(ligne[0:10] !="axiome = \""):
        ligne = lirefichier.readline()
        if ligne=="":
            print("Aucun axiome n'a été précisé")
            sys.exit()
    fermeture(lirefichier)
    return ligne.split("\"")[1]

"""
Nom de la fonction: TrierRegles
Auteur: Nicolas TIREL
But: Trouver et récuperer la ou les règles dans le fichier
"""
def TrierRegles():
    lirefichier=lecture(fichier)
    ligne = lirefichier.readline()
    while(ligne[0:8]!="regles ="):
        ligne = lirefichier.readline()
        if ligne == "":
            print("Aucune règle n'a été précisée")
            sys.exit()
        regles = ""
    for i in range(0,nombreRegles):
        regles += lirefichier.readline()
    regles = regles.split("\"")
    for i in range(0,nombreRegles):
        del regles[i]
    del regles[-1]
    fermeture(lirefichier)
    return regles

"""
Nom de la fonction: TrierAngle
Auteur: Gauthier CUSSONNEAU
But: Trouver et récuperer l'angle dans le fichier
"""
def TrierAngle():
    lirefichier=lecture(fichier)
    ligne = lirefichier.readline()
    while(ligne[0:8]!="angle = "):
        ligne = lirefichier.readline()
        if ligne == "":
            print("Aucun angle n'a été précisé")
            sys.exit()
    fermeture(lirefichier)
    return ligne.split("=")[1]

"""
Nom de la fonction: TrierTaille
Auteur: Gauthier CUSSONNEAU
But: Trouver et récuperer la taille dans le fichier
"""
def TrierTaille():
    lirefichier=lecture(fichier)
    ligne = lirefichier.readline()
    while(ligne[0:9]!="taille = "):
        ligne = lirefichier.readline()
        if ligne == "":
            print("Aucune taille n'a été précisé, elle est donc définie à 5 par défaut")
            fermeture(lirefichier)
            return 5
    fermeture(lirefichier)
    return ligne.split("=")[1]

"""
Nom de la fonction: TrierNiveau
Auteur: Gauthier CUSSONNEAU
But: Trouver et récuperer le niveau dans le fichier
"""
def TrierNiveau():
    lirefichier=lecture(fichier)
    ligne = lirefichier.readline()
    while(ligne[0:9]!="niveau = "):
        ligne = lirefichier.readline()
        if ligne == "":
            print("Aucun niveau n'a été précisé")
            sys.exit()
    fermeture(lirefichier)
    return ligne.split("=")[1]

"""
Nom de la procédure: RécupérationVariable
Auteur: Gauthier CUSSONNEAU
But: Vérifier si chaque variable est bien renseignée
"""
def RécupérationVariable():
    global axiome, angle, regles, niveau, taille
    axiome = str(TrierAxiome())
    angle = float(TrierAngle())
    regles = list(TrierRegles())
    niveau = int(TrierNiveau())
    taille = float(TrierTaille())
    if(niveau<0):
        print("Le niveau ne peut pas être négatif")
        sys.exit()

"""
Nom de la procédure: InitialisationEcriture
Auteur: Nicolas TIREL
But: Ecrire le début du fichier de sortie
Cette procédure contient deux autres procédures qui vont permettre de gérer les crochets.
Cette procédure aurait pu être simplifié en seulement quelques lignes mais elle a été écrites afin de bien voir les procédures en sortie
"""
def InitialisationEcriture(sortie):
    écriresortie = open(sortie, "w")
    écriresortie.write("#!/usr/bin/env python3\n")
    écriresortie.write("from turtle import *\n")
    écriresortie.write("color('black')\n")
    écriresortie.write("tracer(1000.0)\n")
    écriresortie.write("title('Dessin en cours...')\n")
    écriresortie.write("X = []\n")
    écriresortie.write("Y = []\n")
    écriresortie.write("angle_list = []\n\n")
    écriresortie.write("def sauvegarder():\n")
    écriresortie.write("    x = xcor()\n")
    écriresortie.write("    y = ycor()\n")
    écriresortie.write("    X.append(x)\n")
    écriresortie.write("    Y.append(y)\n")
    écriresortie.write("    angle_list.append(heading())\n\n")
    écriresortie.write("def déplacer():\n")
    écriresortie.write("    if(len(X)==0):\n")
    écriresortie.write("     print(\"La règle ou l'axiome est mal renseignée\")\n")
    écriresortie.write("    else:\n")    
    écriresortie.write("     x = X[-1]\n")
    écriresortie.write("     y = Y[-1]\n")
    écriresortie.write("     angle = angle_list[-1]\n")
    écriresortie.write("     del X[-1]\n")
    écriresortie.write("     del Y[-1]\n")
    écriresortie.write("     del angle_list[-1]\n")
    écriresortie.write("     goto(x,y)\n")
    écriresortie.write("     setheading(angle)\n\n")
    écriresortie.close()  

"""
Nom de la fonction: croissance
Auteur: Nicolas TIREL
But: appliquer la ou les règles à l'axiome selon le niveau
"""
def croissance(axiome, début, fin):
    if début==fin:
        return axiome
    else:
        for i in range(0,nombreRegles):
                axiome = axiome.replace(regles[i][0],regles[i].split("=")[1])
        return croissance(axiome, début+1, fin)

"""
Nom de la procédure: écriture
Auteur: Nicolas TIREL
But: Ecrire les commandes turtle dans le fichier de sortie
"""
def écriture(croissance, fin):
    écriresortie = open(sortie, "a")
    for i in range(0,fin):
        if(croissance[i]=="-"):
                écriresortie.write("left("+str(angle)+");\n")
        elif(croissance[i]=="+"):
                écriresortie.write("right("+str(angle)+");\n")
        elif(croissance[i]=="a"):
                écriresortie.write("pd(); fd("+str(taille)+");\n")
        elif(croissance[i]=="*"):
                écriresortie.write("right(180);\n")
        elif(croissance[i]=="["):
                écriresortie.write("sauvegarder()\n")
        elif(croissance[i]=="]"):
                écriresortie.write("déplacer()\n")
        else:
                print("La règle ou l'axiome est mal renseignée!")
                sys.exit()
    écriresortie.write("title('Dessin fini')\n")
    écriresortie.write("exitonclick()")

if __name__ == '__main__':
    fichier = str(input("Entrez le nom de votre fichier d'entrée avec son extension:"))
    InitialisationLecture(fichier)
    print(reglesTrouvé,angleTrouvé,niveauTrouvé,tailleTrouvé,axiomeTrouvé)
    condition(lirefichier, lirefichier.readline(), "")
    RécupérationVariable()
    sortie = str(input("Entrez le nom du fichier de sortie (n'oubliez pas l'extension en .py):"))
    InitialisationEcriture(sortie)
    croissance = croissance(axiome, 0, niveau)
    print(croissance)
    écriture(croissance, len(croissance))