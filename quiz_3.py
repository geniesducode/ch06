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

question = Question("Quelle est la vitesse de pointe d'un thon?", [
    Option("40 km/h"), Option("60 km/h"), Option("80 km/h", True)
])
print(question.is_correct("100 km/h"))
print(question.is_correct("60 km/h"))
print(question.is_correct("80 km/h"))
