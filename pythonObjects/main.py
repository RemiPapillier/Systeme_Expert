from .hypothese import *
from .systeme import *
from .equation import *


def get_solution(myDic):
    S = Systeme()
    H = Hypothese()

    hyp = myDic['0']['hypothese']
    for i in hyp:
        if i.isalpha():
            H.append_fact(i)

    indice = len(myDic)
    for i in range(1, indice):
        prem, conc = myDic[str(i)]['premisse'], myDic[str(i)]['conclusion']
        premisse_list=[]
        for i in prem:
            if i.isalpha():
                premisse_list.append(i)
        conclusion_list = []
        for j in conc:
            if j.isalpha():
                conclusion_list.append(j)
        S.append_equation(Equation(premisse_list, conclusion_list))

    #tour d'algorithme pour éliminer les conclusions s'il n'y a pas de premisse
    for e in S.systeme:
        if(not e.premisse and e.conclusion):
            e.remove_conclusion()
            
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
        if(fait not in solution):
            solution.append(fait)
        H.delete_first_item()
    return(str(solution))

