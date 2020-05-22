from .hypothese import *
from .systeme import *
from .equation import *

S = Systeme()
H = Hypothese()

def reset_systeme():
    S = Systeme()
    H = Hypothese()

def add_eq(prem, conc):
    premisse_list=[]
    for i in prem:
        if i.isalpha():
            premisse_list.append(i)
    conclusion_list = []
    for j in conc:
        if j.isalpha():
            conclusion_list.append(j)
    S.append_equation(Equation(premisse_list, conclusion_list))

def add_hyp(hyp):
    for i in hyp:
        if i.isalpha():
            H.append_fact(i)

def get_solution():
    solution = []
    while H.facts:
        fait = H.first_item()
        for e in S.systeme:
            if(fait in e.premisse):
                e.premisse.remove(fait)
            #Condition qui permet d'éviter de relire une ligne dont on a déjà récupéré la conclusion
            if(not e.premisse and e.conclusion):
                for f in e.conclusion:
                    H.append_fact(f)
                e.remove_conclusion()
        solution.append(fait)
        H.delete_first_item()
    return(str(solution))
    

def display():
    for e in S.systeme:
        print(e.premisse)
        print(e.conclusion)
    for f in H.facts:
        print(f)


"""
state = False
#Récupérer le nombre d'équations du système avec une entrée user
while(state == False):
    nb_eq = input("Combien d'équations possède votre système : ")
    print("")
    try:
        nb_eq = int(nb_eq)
        state = True
    except:
        print("-- Veuillez entrer un nombre entier --")


S = Systeme()
#Alimenter le système avec les entrées users
for i in range(nb_eq):

    #Récupérer la prémisse de l'équation numéro i
    premisse = input("Insérez la prémisse de l'équation " +  str(i+1) + " : ")
    premisse_list = []
    for j in premisse:
        if j.isalpha():
            premisse_list.append(j)

    #Récupérer la conclusion de l'équation numéro i
    conclusion = input("Insérez la conclusion de l'équation " +  str(i+1) + " : ")
    conclusion_list = []
    for k in conclusion:
        if k.isalpha():
            conclusion_list.append(k)

    #On ajoute l'équation au système
    S.append_equation(Equation(premisse_list, conclusion_list))
    print("")


H = Hypothese()
#Récupérer l'hypothèse avec une entrée user
facts = input("Listez les faits de l'hypothèse : ")
print("")
for i in facts:
    if i.isalpha():
        H.append_fact(i)


#Algorithme de calcul
solution = []
while H.facts:
    fait = H.first_item()
    for e in S.systeme:
        if(fait in e.premisse):
            e.premisse.remove(fait)
        #Condition qui permet d'éviter de relire une ligne dont on a déjà récupéré la conclusion
        if(not e.premisse and e.conclusion):
            for f in e.conclusion:
                H.append_fact(f)
            e.remove_conclusion()
    solution.append(fait)
    H.delete_first_item()

print(solution)
"""