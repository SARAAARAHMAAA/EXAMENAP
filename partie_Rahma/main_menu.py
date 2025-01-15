import json

# Affichage du menu principal
def main_menu():
    print("\nMenu Principal:")
    print("1. Démarrer un QCM")
    print("2. Afficher l'historique")
    print("3. Changer d'utilisateur")
    print("4. Initialiser votre historique")
    print("5. Quitter")
    return input("Choisissez une option : ").strip()
