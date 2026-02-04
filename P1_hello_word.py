from datetime import datetime
def greet(nom):
    date = datetime.now().date()
    heure = datetime.now().hour
    if 5 <= heure < 12:
        t_greet = 'good morning'
    if 12 <= heure < 18:
        t_greet = 'good evening'
    if 18 <= heure < 23:
        t_greet = 'good nigth'
    display_user(t_greet , nom , date)

def display_user(t_greet , nom , date):
    print("===== HELLO WORD =====")
    print(f"nous somme le {date},")
    print(f"{t_greet} {nom}. Welcome in my first project")

def get_name():
    tentative = 0
    while True:
        try:
            nom = input("entrez votre nom : ").strip()
            if nom ==" ":
                raise  Exception
            if nom :
                greet(nom)
                break
            else :
                tentative += 1
                print("erreur")
                if tentative == 5:
                    print("vous avez atteint la tentative maximale")
                    break
        except Exception:
            print("ERROR: vous avez fait une erreur!!")

if __name__ == "__main__":
    get_name()


    
    
        
            
                

        
        
    

