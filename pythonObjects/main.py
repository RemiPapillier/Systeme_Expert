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
