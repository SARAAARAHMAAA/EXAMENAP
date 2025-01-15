

def poser_questions(questions):
    """Pose les questions à l'utilisateur et retourne le score."""
    score = 0
    for category, questions_list in questions.items():
        print(f"\nCatégorie : {category}")
        for index, question in enumerate(questions_list):
            print(f"\nQuestion {index + 1}: {question['question']}")
            for i, option in enumerate(question['options']):
                print(f"{i + 1}. {option}")
            
           
            while True:
                try:
                    reponse = input("Votre réponse (1-4) : ").strip()
                    index_reponse = int(reponse) - 1
         
                    if 0 <= index_reponse < len(question['options']):
                        if question['options'][index_reponse] == question['bonne_reponse']:
                            print("Bonne réponse !")
                            score += 1
                        else:
                            print("Mauvaise réponse.")
                        break
                    else:
                        print("Veuillez entrer un nombre entre 1 et 4.")
                except ValueError:
                    print("Entrée invalide. Veuillez entrer un numéro valide.")
    
    return score, None



