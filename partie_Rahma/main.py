import json
import load_users
import get_user
import main_menu
import save_users
import demarrer_qcm
import init_historique
import mettre_a_jour_historique
import decoration

def main():
    # Charger les utilisateurs à chaque fois pour prendre en compte les modifications dans users.json
    def reload_users():
        return load_users.load_users()

    data = reload_users()  # Charger les utilisateurs dès le début
    user_id = get_user.get_user(data)
    print(f"Utilisateur sélectionné : {user_id}")
    
    # Trouver l'utilisateur correspondant
    user = next((user for user in data if user['user_id'] == user_id), None)

    while True:
        choice = main_menu.main_menu()

        if choice == "1":
            print("Démarrage du QCM...")
            score = demarrer_qcm.demarrer_qcm(user_id)  # Suppose que cela retourne un score
            mettre_a_jour_historique.mettre_a_jour_historique(user_id, user['username'], score)
            
            # Relire les utilisateurs pour mettre à jour les informations
            data = reload_users()

        elif choice == "2":
            # Relire les utilisateurs pour prendre en compte les mises à jour
            data = reload_users()
            user = next((user for user in data if user['user_id'] == user_id), None)

            if user and user.get("history"):
                print(f"Historique de {user['username']}:")
                for entry in user["history"]:
                    print(f"Date: {entry['date']}, Score: {entry['score']}")
            else:
                print("Aucun historique trouvé.")

        elif choice == "3":
            user_id = get_user.get_user(data)  # Permet de changer d'utilisateur
            print(f"\n\nUtilisateur sélectionné : {user_id}\n\n\n")

        elif choice == "4":
            init_historique.init_historique(user["user_id"], user["username"])
            data = reload_users()  # Relire les utilisateurs

        elif choice == "5":
            print("Au revoir!")
            save_users.save_users(data)  # Sauvegarde les utilisateurs mis à jour
            break

        else:
            print("Option invalide, veuillez réessayer.")

    # Sauvegarder les utilisateurs mis à jour à la fin
    save_users.save_users(data)

if __name__ == "__main__":
    decoration.show_intro()
    main()
