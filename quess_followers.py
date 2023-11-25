from data import data
import random
import os

print("Vítejte ve hře o to kdo má víc sledovanosti na instagramu")

score = 0


# Při správné odpovědi přidá bod do skóre
def score_count(is_correct):
    global score            # Use the global score variable
    if is_correct == True:
        score = score + 1
        return score

# Zjistí pokud jsou dva účty stejné a jeden změní --------- Nefunguje !!!
def diff_acc_control(acc1, acc2):
    new_random_account = random.randint(0, len(data) -1)
    if acc1 == acc2:
        return new_random_account
    
# Zkontroluje správný výsledek a vrátí True nebo False
def compare(answer_check, followers_data_A, followers_data_B):
    """Zkontroluje správný výsledek a vrátí True nebo False""" 
    if answer_check == "A":
        if followers_data_A > followers_data_B:
            return True
        else:
            return False
    elif answer_check == "B":
        if followers_data_B > followers_data_A:
            return True
        else:
            return False     
 <--- NEFUNGUJE    
# má smazat již použité účty, aby se neopakovaly.    
def delete_account(acc1, acc2):
    del data[acc1]
    del data[acc2]

# funkce pro položení otázek a,b
def give_questions(account_A, account_B):
    print(f"Porovnejte A: {account_A['name']}, {account_A['description']} z {account_A['country']}.")
    print(f"Porovnejte B: {account_B['name']}, {account_B['description']} z {account_B['country']}.")

    
# Hlavní strukturované procesy hry
def game():
    
    while True:
        # získání náhodných čísel pro výběr v list "data"
        random_acc1 = random.randint(0, len(data) -1)
        random_acc2 = random.randint(0, len(data) -1)
        # pomocí indexu v seznamu vybereme dictionary s jeho hodnotami a uložíme vše do jednotlivých účtů
        account_A = data[random_acc1]
        account_B = data[random_acc2]
        # vybírání číselné hodnoty 'sledujících'
        followers_data_A = account_A['follower_count']
        followers_data_B = account_B['follower_count']   
        
        diff_acc_control(account_A, account_B)
        give_questions(account_A, account_B)
        answer = input("Kdo má více sledujících na instagramu? A/B ")  
        answer_check = answer.upper()           # formátuje user input na velké písmeno
        is_true = compare(answer_check, followers_data_A, followers_data_B)         # Zkontroluje správný výsledek a vrátí True nebo False
        if is_true == True:
            os.system('cls')
            score_count(is_true)
            print(f"Uhádli jste. Vaše scóre je {score} ")
            
            lets_continue = input("Pokračovat? ano/ne ")
            if lets_continue == "ano":
                game()
            else:
                break
        elif is_true == False:
            os.system('cls')
            print(f"To je špatně. Vaše konečné scóre je {score}")
            break
        else:
            print("ERROR")
        break
                   

game()