#Un certain nombre d'équations
from .equation import *

class Systeme:

    #Constructeur par défaut qui initialise un attribut systeme correspondant à une liste vide qui sera ensuite composé d'objets Equation
    def __init__(self):
        self.systeme = []

    #Fonction pour ajouter une équation dans la liste systeme
    def append_equation(self, eq):
        self.systeme.append(eq)