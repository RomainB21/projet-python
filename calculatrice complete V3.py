import os
import sys
import json

cur_dir = os.path.dirname(__file__)
calcul_paths = os.path.join(cur_dir, "calcul.json")

if os.path.exists(calcul_paths):
    with open(calcul_paths, "r") as f:
       calcul = json.load(f)
else:
    calcul = []


while True:
    choix_utilisateur = input("Que voulez-vous faire?\n1. Faire une addition\n2. Faire une soustraction\n3. Faire une multiplication\n4. Faire une division\n5. Historique\n6. Quitter\nVotre choix ?\n")

    if choix_utilisateur == "1":
        nb1 = input("Entrez un premier nombre: ")
        nb2 = input("Entrez un deuxième nombre: ")
        if nb1.replace('.', '', 1).isdigit() and nb2.replace('.', '', 1).isdigit():
            result = f"Le résultat de l'addition {nb1} avec {nb2} est égal à {float(nb1) + float(nb2)}"
            print(result)
            calcul.append(result)
        else:
            print("Les nombres saisis ne sont pas valides.")
    if choix_utilisateur == "2":
        nb1 = input("Entrez un premier nombre: ")
        nb2 = input("Entrez un deuxième nombre: ")
        if nb1.replace('.', '', 1).isdigit() and nb2.replace('.', '', 1).isdigit():
            result = f"Le résultat de la soustraction {nb1} avec {nb2} est égal à {float(nb1) - float(nb2)}"
            print(result)
            calcul.append(result)
        else:
            print("Les nombres saisis ne sont pas valides.")
    
    if choix_utilisateur == "3":
        nb1 = input("Entrez un premier nombre: ")
        nb2 = input("Entrez un deuxième nombre: ")
        if nb1.replace('.', '', 1).isdigit() and nb2.replace('.', '', 1).isdigit():
            result = f"Le résultat de la multiplication {nb1} avec {nb2} est égal à {float(nb1) * float(nb2)}"
            print(result)
            calcul.append(result)
        else:
            print("Les nombres saisis ne sont pas valides.")
    
    if choix_utilisateur == "4":
        nb1 = input("Entrez un premier nombre: ")
        nb2 = input("Entrez un deuxième nombre: ")
        if nb1.replace('.', '', 1).isdigit() and nb2.replace('.', '', 1).isdigit():
            result = f"Le résultat de la division {nb1} avec {nb2} est égal à {float(nb1) / float(nb2)}"
            print(result)
            calcul.append(result)
        else:
            print("Les nombres saisis ne sont pas valides.")
    
    if choix_utilisateur == "5":
        print("Historique des opérations :")
        for result in calcul:
            print(result)
    
    elif choix_utilisateur == "6":  # Sauvegarder et quitter
        with open(calcul_paths, "w") as f:
            json.dump(calcul, f, indent=4)
        print("merci d'avoir utiliser notre calculatrice")
        sys.exit()