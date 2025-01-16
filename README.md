# EXAMENAP

This is the repository for our exam in the Advanced Programming (AP) subject.

## Instructions d’utilisation

### Prérequis

- Python 3.x installé sur votre machine
- installer colorama (pip install colorama )
- Fichier `users.json` (sera généré automatiquement si non présent)

### Installation

1. Clonez ce répertoire :
    ```bash
    git clone https://github.com/votre-repository/examenap.git
    cd examenap
    ```

2. Assurez-vous que tous les fichiers nécessaires sont présents :
    - main.py
    - main_meny.py
    - get_users.py
    - load_users.py
    - load_questions.py
    - poser_questions.py
    - mettre_a_jour_historique.py
    - init_historique.py
    - demarrer_qcm.py
    - decoration.py
    - questions.json
    - users.json (il sera creer automatiquement si il n'existe pas)

### Exécution de l’application

1. Lancez le fichier principal :
    ```bash
    python main.py
    ```

2. Suivez les instructions affichées dans la console :
    - Entrez votre identifiant utilisateur.
    - Choisissez une action dans le menu (Démarrer un QCM, Afficher l'historique, Quitter).

### Exemple d’exécution

```bash

         ███████╗██╗   ██╗███████╗     ██████╗  ██████╗███╗   ███╗
         ██╔════╝╚██╗ ██╔╝██╔════╝    ██╔═══██╗██╔════╝████╗ ████║
         ███████╗ ╚████╔╝ ███████╗    ██║   ██║██║     ██╔████╔██║
         ╚════██║  ╚██╔╝  ╚════██║    ██║▄▄ ██║██║     ██║╚██╔╝██║
         ███████║██╗██║██╗███████║    ╚██████╔╝╚██████╗██║ ╚═╝ ██║
         ╚══════╝╚═╝╚═╝╚═╝╚══════╝     ╚══▀▀═╝  ╚═════╝╚═╝     ╚═╝
       
           
✨ S.Y.S QCM – Testez vos connaissances ! ✨


Chargement du QCM, veuillez patienter...
[==============================] 100%

✅ Chargement terminé ! Bonne chance ! 💪

🔍 Identification utilisateur
Entrez votre nom d'utilisateur : rahma

🆕 Nouvel utilisateur détecté. Création du profil avec ID 3...

✅ Profil utilisateur mis à jour avec succès.
Utilisateur sélectionné : 3
+----------------------------------------+
|          MENU PRINCIPAL            |
+----------------------------------------+
|  1. 🏁 Démarrer un QCM                 |
|  2. 📜 Afficher l'historique           |
|  3. 🔄 Changer d'utilisateur           |
|  4. 🧹 Initialiser votre historique    |
|  5. ❌ Quitter                         |
+----------------------------------------+
👉 Choisissez une option (1-5) : 2
Aucun historique trouvé.
+----------------------------------------+
|          MENU PRINCIPAL            |
+----------------------------------------+
|  1. 🏁 Démarrer un QCM                 |
|  2. 📜 Afficher l'historique           |
|  3. 🔄 Changer d'utilisateur           |
|  4. 🧹 Initialiser votre historique    |
|  5. ❌ Quitter                         |
+----------------------------------------+
👉 Choisissez une option (1-5) : 1
Démarrage du QCM...

Catégories disponibles :
1. Python
2. Réseaux
3. Algorithmes
4. Systèmes d'exploitation
5. Mathématiques
Choisissez une catégorie (numéro) : 1

Vous avez choisi la catégorie : Python

#les questions de la categories python
Question 5/6: Quelle méthode est utilisée pour ajouter un élément à une liste en Python ?
1. push()
2. append()
3. insert()
4. add()
( Temps restant : 24 secondes ) => Votre réponse (1-4) : 2
Bonne réponse ! 🎉
Score actuel : 4/5
.
.
.
+----------------------------------------+
|          MENU PRINCIPAL            |
+----------------------------------------+
|  1. 🏁 Démarrer un QCM                 |
|  2. 📜 Afficher l'historique           |
|  3. 🔄 Changer d'utilisateur           |
|  4. 🧹 Initialiser votre historique    |
|  5. ❌ Quitter                         |
+----------------------------------------+
👉 Choisissez une option (1-5) : 2
Historique de rahma:
Date: 2025-01-16 00:44:55, Score: 5
+----------------------------------------+
|          MENU PRINCIPAL            |
+----------------------------------------+
|  1. 🏁 Démarrer un QCM                 |
|  2. 📜 Afficher l'historique           |
|  3. 🔄 Changer d'utilisateur           |
|  4. 🧹 Initialiser votre historique    |
|  5. ❌ Quitter                         |
+----------------------------------------+
👉 Choisissez une option (1-5) : 5
Au revoir!
```

### Contributeurs

- **Sadaoui sara rahma** : Gestion des utilisateurs, interface utilisateur principale,changement d'utilisateur
- **Aibeche yasmine** : Gestion des questions et réponses, évaluation et feedback, nettoyage de l'historique 
- **Toutou salsabila** : Gestion avancée (chronométrage, exportation des résultats, catégories de questions), decoration du qcm

### Remarques

- Assurez-vous que le fichier `users.json` est accessible en lecture et écriture pour enregistrer l’historique des utilisateurs.
- L’application fonctionne en mode console et peut être exécutée sur toute machine disposant de Python 3.x.

---

Merci d’utiliser notre application QCM pour l’examen en Advanced Programming.


