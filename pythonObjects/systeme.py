#Un certain nombre d'équations
from .equation import *

class Systeme:

    def __init__(self):
        self.systeme = []

    def append_equation(self, eq):
        self.systeme.append(eq)