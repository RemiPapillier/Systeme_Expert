#Comporte les faits
class Hypothese:

    def __init__(self):
        self.facts = []

    def append_fact(self, fact):
        self.facts.append(fact)

    def first_item(self):
        return self.facts[0]

    def delete_first_item(self):
        del self.facts[0]