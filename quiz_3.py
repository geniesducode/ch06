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

question = Question("Quelle est la vitesse de pointe d'un thon?", [
    Option("40 km/h"), Option("60 km/h"), Option("80 km/h", True)
])
question.show()
