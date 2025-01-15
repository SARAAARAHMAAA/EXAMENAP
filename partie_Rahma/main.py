import json
import load_users  
import get_user
import main_menu
import save_users
import demarrer_qcm
import mettre_a_jour_historique



# Fonction principale
def main():
    # Charger les utilisateurs depuis le fichier JSON
    users = load_users.load_users()

    # Identifier ou créer un profil utilisateur
    user_id = get_user.get_user(users)
    print(f"Utilisateur sélectionné : {user_id}")
    while True:
        # Afficher le menu principal
        choice = main_menu.main_menu()
        if choice == "1":
            print("Démarrage du QCM...")
            demarrer_qcm.demarrer_qcm(user_id)
        elif choice == "2":
            # Afficher l'historique des QCM
            if users[user_id]["history"]:
                print("Historique des QCM :")
                for entry in users[user_id]["history"]:
                    print(f"Date: {entry['date']}, Score: {entry['score']}")
            else:
                print("Aucun historique disponible.")
        elif choice == "3":
            # Quitter le programme
            print("Au revoir!")
            break
        else:
            print("Option invalide, veuillez réessayer.")

    # Sauvegarder les utilisateurs mis à jour
    save_users.save_users(users)

if __name__ == "__main__":
    main()
