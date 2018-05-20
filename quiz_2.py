def show_question(question, correct_answer, options):
    print(question)
    print(options)

    print("Entrez une réponse:")
    answer = input()
    if answer == correct_answer:
        print("Bravo!")
        return True
    else:
        print("La réponse n'est pas correcte, la bonne réponse était " + correct_answer)
        return False

score = 0
is_correct = show_question("Quelle est la vitesse de pointe d'un thon?", "80 km/h", ["20 km/h", "40 km/h", "80 km/h"])

if is_correct:
    score += 1

is_correct = show_question("Les poissons ont-ils tous des écailles?", "Non", ["Oui", "Non"])

if is_correct:
    score += 1

print("Vous avez répondu correctement à " + str(score) + " questions sur 2")
