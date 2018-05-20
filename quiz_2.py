def show_question(question, correct_answer, options):
    print(question)
    print(options)

    print("Entrez une réponse:")
    answer = input()

    if answer == correct_answer:
        print("Bravo!")
    else:
        print("La réponse n'est pas correcte")

show_question("Quelle est la vitesse de pointe d'un thon?", "80 km/h", ["20 km/h", "40 km/h", "80 km/h"])
show_question("Les poissons ont-ils tous des écailles?", "Non", ["Oui", "Non"])
