
def advanced_calculator():
    historique = []
    while True:
        calc = 'bienvenue dans votre calculatrice avancée'
        print(f"{calc:=^51}")  

        print("1: Addition (+)")
        print("2: Soustraction (-)")
        print("3: Multplication (*)")
        print("4: Division (/)")
        print("5: Puissance (^ ou **)")
        print("6: Modulo (%)")
        print("7: Afficher l'historique")
        print("8: Quitter")

        try:
            choix = input("entrez votre choix :")
            if choix == "+" or choix == "1" : choix = 1
            elif choix == "-" or choix =="2" : choix = 2
            elif choix == "*" or choix == "3" : choix = 3
            elif choix == "/" or choix == "4" : choix = 4 
            elif choix == "^" or choix == "**" or  choix == "5" : choix = 5
            elif choix == "%" or choix =="6" : choix = 6
            elif choix == "7" : choix = 7
            elif choix == "8" : choix = 8
            else: raise ValueError
            choix = int(choix)
        except ValueError:
            print(" Erreur : veullier réesayer")

        if choix == 8:
            try:
                quitter = input("voulez vous quitter? \u2192 (oui/non) :")
                if quitter == "oui":
                    quit = " MERCI ET A BIENTOT "
                    print(F"{quit:_^50}")
                    break
                else:
                    continue
            except ValueError:
                print("Entrée  soit oui ou non")

        if choix == 7:
            if not historique:
                print("vous n'avez aucun calcul dans l'historique")
            else:
                print("l'historique des cinq derniers calculs")
                for calcs in historique:
                    print(calcs)
            continue

        try:
            nbr1 = float(input("entrez le premier nombre: ").strip())
            nbr2 = float(input("entrez le deuxième nombre: ").strip())
        except ValueError:
            print("Erreur : entrée de nombre invalide.")
            continue
        if choix == 1:
                result = nbr1 + nbr2
                clcf = "addition"
                sn_calc = "+"
        elif choix == 2:
            result  =  nbr1 - nbr2
            clcf = "soustraction"
            sn_calc = "-"
        elif choix == 3:
            result = nbr1 * nbr2
            clcf = "multiplication"
            sn_calc = "*"
        elif choix == 4:
            if nbr2 == 0:
                print("Erreur: aucun nombre n'est divisible par zero")
                raise ZeroDivisionError
            else:
                result = nbr1 / nbr2
                result = round(result,2)
                clcf = "division"
                sn_calc = "/"
        elif choix == 5:
            nbr2 = int(nbr2)
            result = pow(nbr1,nbr2)
            result = round(result,2)
            clcf = "puissance"
            sn_calc ="^" 
        elif choix == 6:
            if nbr2 == 0: 
                print("Erreur: aucun nombre n'est divisible par zero")
                raise ZeroDivisionError
            else:
                result = nbr1 % nbr2
                result = round(result,2)
                clcf = "modulo"
                sn_calc = "%"
        print(f"votre calcul : {clcf} a pour résultat:{result:.2f} ")
                    
        historique.append(f"{nbr1} {sn_calc} { nbr2} = {result:.2f}")
        if len(historique) > 5:
            historique.pop(0)
                    
    
if __name__== "__main__":
    advanced_calculator()   
                    
            
                        
                        
                            

                        



            