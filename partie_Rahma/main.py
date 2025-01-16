import json
import load_users  
import get_user
import main_menu
import save_users
import demarrer_qcm
import init_historique
import mettre_a_jour_historique
import decoration

user = None 
data = None
user_id = None

def main():
    global data
    data = load_users.load_users()
    global user_id
    user_id = get_user.get_user(data)
    print(f"Utilisateur sélectionné : {user_id}")
    
    global user
    user = next((user for user in data if user['user_id'] == user_id), None)

    while True:
        choice = main_menu.main_menu()
        
        if choice == "1":
            print("Démarrage du QCM...")
            demarrer_qcm.demarrer_qcm(user_id)
        
        elif choice == "2":
        # Chargement des données et récupération de l'utilisateur
           data = load_users.load_users()
           user = next((user for user in data if user['user_id'] == user_id), None)

                # Vérification si l'utilisateur existe
           if user:
              print("\n")
              print("=" * 45)
              print(f"✨ Historique de l'utilisateur : {user['username']} ✨")
              print("=" * 45)

           # Vérification si l'utilisateur a un historique
              if user["history"]:
                print(f"🔍 {len(user['history'])} entrée(s) trouvée(s) :")
                print("-" * 45)
                for entry in user["history"]:
                  print(f"📅 Date : {entry['date']}")
                  print(f"🏆 Score : {entry['score']}")
                  print("-" * 45)
              else:
               print("❌ Aucun historique trouvé pour cet utilisateur.")
           else:
             print("❌ Utilisateur introuvable.")

           print("\n\n")

        elif choice == "3":
            user_id = get_user.get_user(data)  # Permet de changer d'utilisateur
            
            print(f"\n\nUtilisateur sélectionné : {user_id}\n\n\n")

        elif choice == "4":
            init_historique.init_historique(user["user_id"], user["username"])

        elif choice == "5":
            print("Au revoir!")
            break
        
        else:
            print("Option invalide, veuillez réessayer.")


if __name__ == "__main__":
    decoration.show_intro()
    main()
