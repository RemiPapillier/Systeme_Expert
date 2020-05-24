from .hypothese import *
from .systeme import *
from .equation import *

#Fonction principale appelée lorsqu'on appuie sur Start et qui prend en paramètre un dictionnaire de dictionnaire contenant toutes les données
def get_solution(myDic):
    #Initialisation d'un système et d'une hypothèse
    S = Systeme()
    H = Hypothese()

    #Boucle pour récupérer les faits dans l'hypothese
    hyp = myDic['0']['hypothese']
    for i in hyp:
        if i.isalpha():
            H.append_fact(i)

    #Boucle pour créer les equations avec leur premisse et conclusion puis ajoutant l'équation au systeme
    indice = len(myDic)
    for i in range(1, indice):
        prem, conc = myDic[str(i)]['premisse'], myDic[str(i)]['conclusion']
        #Récupération de la premisse de l'equation i
        premisse_list=[]
        for i in prem:
            if i.isalpha():
                premisse_list.append(i)
        #Récupération de la conclusion de l'equation i
        conclusion_list = []
        for j in conc:
            if j.isalpha():
                conclusion_list.append(j)
        #Création de l'equation et ajout au systeme
        S.append_equation(Equation(premisse_list, conclusion_list))

    #tour d'algorithme pour éliminer les conclusions s'il n'y a pas de premisse
    for e in S.systeme:
        if(not e.premisse and e.conclusion):
            e.remove_conclusion()

    #Algorithme principal pour récupérer la solution
    solution = []
    #Tant qu'on a des faits
    while H.facts:
        fait = H.first_item()
        #On parcours les equations du systeme
        for e in S.systeme:
            if(fait in e.premisse):
                e.premisse.remove(fait)
            #Condition qui permet d'éviter de relire une ligne dont on a déjà récupéré la conclusion
            if(not e.premisse and e.conclusion):
                for f in e.conclusion:
                    H.append_fact(f)
                e.remove_conclusion()
        #Si le fait n'est pas deja dans la solution, on l'ajout
        if(fait not in solution):
            solution.append(fait)
        H.delete_first_item()
    #On renvoie la solution en chaine de caractere
    return(str(solution))

