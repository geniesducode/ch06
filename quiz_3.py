class Option:
    def __init__(self, label, correct=False):
        self.label = label
        self.correct = correct

class Question:
    def __init__(self, label, options, points=1):
        self.label = label
        self.options = options
        self.points = points

    def is_correct(self, answer):
        answer = answer.lower()

        for option in self.options:
            if option.label.lower() == answer:
                return option.correct

        return False

    def show(self):
        # La méthode `format` remplace les caractères {} dans la chaîne de caractères par les paramètres qui lui sont
        # passés. Ici le premier {} sera remplacé par la question, et le deuxième par le nombre de points. Cette méthode
        # convertit automatiquement les paramètres en type str, pas besoin de le faire manuellement!
        print("{} ({} points)".format(self.label, self.points))
        for option in self.options:
            print("- " + option.label)
        print("Entrez une réponse:")
        answer = input()
        if self.is_correct(answer):
            print("Bravo!")
            return self.points
        else:
            print("La réponse n'est pas correcte. La bonne réponse était " + self.get_correct_answer().label)
            return 0

    def get_correct_answer(self):
        for option in self.options:
            if option.correct:
                return option

questions = [
    Question("Quelle est la vitesse de pointe d'un thon?",
              [Option("20 km/h"), Option("40 km/h"),
               Option("80 km/h", True)], 3),
    Question("Les poissons ont-ils tous des écailles?",
              [Option("Oui"), Option("Non", True)])
]

score = 0
total_points = 0
for question in questions:
    scored_points = question.show()
    score += scored_points
    total_points += question.points

score_percentage = int(score / total_points * 100)
print("Votre score est de {} sur un total de {}".format(score, total_points))
print("Votre taux de réussite est de " + str(score_percentage) + "%")
