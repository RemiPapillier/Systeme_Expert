#Premisse (avant le égal) Conclusion (apres le egal)
class Equation:

    #Constructeur qui prend en parametre la premisse et la conclusion de l'equation sous forme de liste
    #La premisse et la conclusion sont des attributs de l'objet equation
    def __init__(self, premisse, conclusion):
        self.premisse = premisse
        self.conclusion = conclusion

    #On vide l'attribut conclusion d'une equation
    def remove_conclusion(self):
        self.conclusion = []