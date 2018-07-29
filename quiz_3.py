class Option:
    def __init__(self, label, correct=False):
        self.label = label
        self.correct = correct

class Question:
    def __init__(self, label, options):
        self.label = label
        self.options = options

    def is_correct(self, answer):
        for option in self.options:
            if option.label == answer:
                return option.correct

        return False

    def show(self):
        print(self.label)
        for option in self.options:
            print("- " + option.label)
        print("Entrez une réponse:")
        answer = input()
        if self.is_correct(answer):
            print("Bravo!")
            return True
        else:
            print("La réponse n'est pas correcte")
            return False

questions = [
    Question("Quelle est la vitesse de pointe d'un thon?",
              [Option("20 km/h"), Option("40 km/h"),
               Option("80 km/h", True)]),
    Question("Les poissons ont-ils tous des écailles?",
              [Option("Oui"), Option("Non", True)])
]

score = 0
for question in questions:
    is_correct = question.show()
    if is_correct:
        score += 1

score_percentage = int(score / len(questions) * 100)
print("Vous avez répondu correctement à " + str(score) +
      " questions sur " + str(len(questions)))
print("Ce qui fait un score de " + str(score_percentage) + "%")
