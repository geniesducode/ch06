def show_question(question, options):
    print(question)

    for option in options:
        print("- " + option)

    print("Entrez une réponse:")

    answer = input()
    if options[answer]:
        print("Bravo!")
        return True
    else:
        print("La réponse n'est pas correcte")
        return False

score = 0
questions = [
    ["Quelle est la vitesse de pointe d'un thon?", {"20 km/h": False, "40 km/h": False, "80 km/h": True}],
    ["Les poissons ont-ils tous des écailles?", {"Oui": False, "Non": True}]
]

for question in questions:
    is_correct = show_question(question[0], question[1])

    if is_correct:
        score += 1

print("Vous avez répondu correctement à " + str(score) + " questions sur " + str(len(questions)))
