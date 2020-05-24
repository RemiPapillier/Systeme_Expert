#Comporte les faits
class Hypothese:

    #Constructeur par defaut de l'hypothese qui cree un attribut facts correspondant à une liste vide
    def __init__(self):
        self.facts = []

    #Fonction pour ajouter un fait à l'attribut
    def append_fact(self, fact):
        self.facts.append(fact)

    #Fonction pour récupérer le premier fait de la liste
    def first_item(self):
        return self.facts[0]

    #Fonction pour supprimer le premier fait de la liste
    def delete_first_item(self):
        del self.facts[0]