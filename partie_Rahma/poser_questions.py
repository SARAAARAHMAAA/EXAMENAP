

def poser_questions(questions):
    """Pose les questions à l'utilisateur et retourne le score."""
    score = 0
    for category, questions_list in questions.items():
        print(f"\nCatégorie : {category}")
        for index, question in enumerate(questions_list):
            print(f"\nQuestion {index + 1}: {question['question']}")
            for i, option in enumerate(question['options']):
                print(f"{i + 1}. {option}")
            # Demander à l'utilisateur de répondre
            reponse = input("Votre réponse (1-4) : ")
            if question['options'][int(reponse) - 1] == question['bonne_reponse']:
                score += 1
    return score, None
