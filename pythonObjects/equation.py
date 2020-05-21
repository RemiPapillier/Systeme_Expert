#Premisse (avant le égal) Conclusion (apres le egal)
class Equation:

    def __init__(self, premisse, conclusion):
        self.premisse = premisse
        self.conclusion = conclusion

    def remove_conclusion(self):
        self.conclusion = []