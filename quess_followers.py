from data import data
import random
import os

print("Vítejte ve hře o to kdo má víc sledovanosti na instagramu")

score = 0

# získání náhodných čísel pro výběr v list "data"
random_acc1 = random.randint(0, 10)
random_acc2 = random.randint(0, 10)
# pomocí indexu v seznamu vybereme dictionary s jeho hodnotami a uložíme vše do jednotlivých účtů
account_A = data[random_acc1]
account_B = data[random_acc2]

# vybírání číselné hodnoty 'sledujících'
followers_data_A = account_A['follower_count']
followers_data_B = account_B['follower_count']

# Při správné odpovědi přidá bod do skóre
def score_count(Boolean):
    global score            # Use the global score variable
    if Boolean == True:
        score = score + 1
        return score

# Zkontroluje správný výsledek a vrátí True nebo False
def compare(answer_check):
    """Zkontroluje správný výsledek a vrátí True nebo False""" 
    if answer_check == "A":
        if followers_data_A > followers_data_B:
            print(f"Uhádli jste. Vaše scóre je {score} ")
            return True
        else:
            print(f"To je špatně. Vaše konečné scóre je {score}")
            return False
    elif answer_check == "B":
        if followers_data_B > followers_data_A:
            print(f"Uhádli jste. Vaše scóre je {score} ")
            return True
        else:
            print(f"To je špatně. Vaše konečné scóre je {score}") 
            return False       


# funkce pro položení otázek a,b
def give_questions():
    print(f"Porovnejte A: {account_A['name']}, {account_A['description']} z {account_A['country']}.")
    print(f"Porovnejte B: {account_B['name']}, {account_B['description']} z {account_B['country']}.")
    
# Hlavní strukturované procesy hry
def game():
    while True:
        give_questions()
        answer = input("Kdo má více sledujících na instagramu? A/B ")  
        answer_check = answer.upper()           # formátuje user input na velké písmeno
        is_true = compare(answer_check)         # Zkontroluje správný výsledek a vrátí True nebo False
        if is_true == True:
            score_count(is_true)
            print(score)
            os.system('cls')
            break
            
            
        else:
            os.system('cls')
            break
        

game()