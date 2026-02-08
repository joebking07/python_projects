from random import randint
import time
history_list = []

def game(min_num, max_num, max_attempts, score_bonus, level_name):

    attempt = 0
    score = 0
    start_time = time.time()
    mystery_num = randint(min_num, max_num)
    while attempt  < max_attempts:
        
        try:
            choice =  int(input(f"enter a number between {min_num} and {max_num}:"))
            attempt +=1
            if choice == mystery_num:
                elapsed_T = time.time() - start_time
                score = score_bonus + (30 if elapsed_T < 30 else 0)
                print(f"Well done!! \u2713 you have win in {attempt} attempt , you have +{score}, record time: {elapsed_T:.2f} second")
                history_list.append(f" level: {level_name}; score: {score}; attempt before win {attempt}")
                if len(history_list) > 3: history_list.pop(0)
                return score
            
            if choice < mystery_num :
                print("Oups!! it's too low")
            else:
                print("Oups!! it's too high")
                continue
        except ValueError:
            print("Error: invalid entry")
    print(f"you'r lose  the mystery number was{mystery_num} and your score: -5")
    history_list.append(f"level: {level_name} ; score: {score}; attempt: {max_attempts}")
    if len(history_list) > 3: history_list.pop(0)
    return -5

#principal function   
def principal():
    total_score = 0
    while True:
       
        level_input = input("enter your desired level between: easy / 1, normal / 2, difficult / 3: ").lower().strip()
        if level_input in ["easy","1"]:
            level_input = 1
            params = (1, 50,float('inf') ,10 ,'easy')
        elif level_input in ["normal","2"]:
            level_input = 2
            params = (1, 100,10 ,20 ,'normal')
        elif level_input in ["hard","3"]:
            level_input = 3
            params = (1, 500, 5, 30 ,'hard')
        else:
            print("Error: invalid level")
            continue
       
        round_score = game(*params)
        total_score += round_score
        print(f"score total:{total_score}")

        #history of scores
        
        hist = input("Do you want to see history of score's (y/n): ").lower()
        while hist not in ["y","n"]:
            hist = input("Error:  enter y /n").lower()
        if hist == "y":
                
            if not history_list:
                print("your score history is empty")
            else:
                print("Tree last game parties: ")
                for i,info in enumerate(history_list, start= 1):
                    print(f"{i} \u2192 {info}")
        replay = input("Do you want to replay? (y/n): ").lower()
        while replay not in ["y","n"]:
            replay = input("enter y/n to replay or not : ").lower() 
        if replay =='n':
            print("Bye!!")
            break
        
if __name__=="__main__":
    principal()



            