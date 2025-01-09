# EXAMENAP

This is the repository for our exam in the Advanced Programming (AP) subject.

## Instructions d’utilisation

### Prérequis

- Python 3.x installé sur votre machine
- Fichier `users.json` (sera généré automatiquement si non présent)

### Installation

1. Clonez ce répertoire :
    ```bash
    git clone https://github.com/votre-repository/examenap.git
    cd examenap
    ```

2. Assurez-vous que tous les fichiers nécessaires sont présents :
    - `user_management.py`
    - `qcm_handler.py`
    - `main.py`
    - `users.json` (créé automatiquement après la première exécution)

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
Entrez votre identifiant : user123
Bienvenue de retour, user123! Voici votre historique :
Date: 2025-01-01, Score: 80
Date: 2025-01-08, Score: 90

Menu Principal:
1. Démarrer un QCM
2. Afficher l'historique
3. Quitter
Choisissez une option :
```

### Structure du projet

- `main.py` : Fichier principal pour l’exécution de l’application.
- `user_management.py` : Gestion des utilisateurs (chargement, sauvegarde, affichage de l’historique).
- `qcm_handler.py` : Gestion des questions et de l’évaluation du QCM (développé par la deuxième personne).

### Contributeurs

- **Personne 1** : Gestion des utilisateurs, interface utilisateur principale
- **Personne 2** : Gestion des questions et réponses, évaluation et feedback
- **Personne 3** : Gestion avancée (chronométrage, exportation des résultats, catégories de questions)

### Remarques

- Assurez-vous que le fichier `users.json` est accessible en lecture et écriture pour enregistrer l’historique des utilisateurs.
- L’application fonctionne en mode console et peut être exécutée sur toute machine disposant de Python 3.x.

---

Merci d’utiliser notre application QCM pour l’examen en Advanced Programming.


