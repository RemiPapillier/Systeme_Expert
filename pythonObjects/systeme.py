#Un certain nombre d'équations
from Equation import Equation

class Systeme:

    def __init__(self):
        self.systeme = []

    def append_equation(self, eq):
        self.systeme.append(eq)