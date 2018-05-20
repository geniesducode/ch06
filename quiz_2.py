def show_question(question, correct_answer, options):
    print(question)
    for option in options:
        print("- " + option)

    print("Entrez une réponse:")
    answer = input()
    if answer == correct_answer:
        print("Bravo!")
        return True
    else:
        print("La réponse n'est pas correcte")
        return False

score = 0
questions = [
    ["Quelle est la vitesse de pointe d'un thon?", "80 km/h", ["20 km/h", "40 km/h", "80 km/h"]],
    ["Les poissons ont-ils tous des écailles?", "Non", ["Oui", "Non"]]
]

for question in questions:
    is_correct = show_question(question[0], question[1], question[2])

    if is_correct:
        score += 1

print("Vous avez répondu correctement à " + str(score) + " questions sur " + str(len(questions)))
