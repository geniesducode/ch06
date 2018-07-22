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
