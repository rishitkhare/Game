import random

#Let's Make a game!!
#
#Recommendations:
#
# - multiple dimensions
#     1. survival (energy consumption)
#     2. upgrades (tools) (Either earn more, or less energy)
#     3. unexpected events (Fired from job, enemy attacks, robbery)
#     4. Add Konami Code?

# Main functions:

def ask_Location():
    global money
    global energy
    
    print('\nType S for shop\n\nType B to build\n\nType I for inventory\n\n\n\nMoney: $', money, '\n\nEnergy:',energy, "/10\n\n\n\n")
    location = input(">>>")
    return location

def enter_Shop():
    global money
    global games
    global pizza
    while True:
        ans = ' '
        if(money == 0):
            print("STOREKEEPER: If you don\'t have money, what good are you to me?")
            print("Come back when you have something useful!!")
        else:
            print("STOREKEEPER: What would you like? G for video game ($ 5), P for pizza ($ 2)! \nThat's all we sell!\n\n(E to exit)")
            ans = input("\n\n>>>")
            if(ans.lower() == 'g'):
                if(money > 4):
                    print('\n\n',name,'paid $ 5 and recieved 1 game!')
                    money = money - 5
                    games = games + 1
                else:
                    print("SHOPKEEPER: You don' have enough money for that game!!")
            if(ans.lower() == 'p'):
                if(money > 2):
                    print('\n\n',name,'paid $ 2 and recieved one pizza!')
                    money = money -2
                    pizza = pizza + 1
                else:
                    print("SHOPKEEPER: You don' have enough money for that pizza!!")
            if(ans.lower() == 'e'):
                print("SHOPKEEPER: Come again soon!")
                break
    
def show_Inventory():
    global games
    global pizza
    
    print('Select an energy fufiller! \n\nInventory:\n\nPizzas: p, Games: g, Exit: e')
    print('Pizzas:',pizza)
    print('Games:',games)

def enter_StorageRoom():
    global games
    global pizza
    global energy
    while True:
        show_Inventory()
        ans = input('\n\n>>>')
        if(ans.lower() == 'p'):
            print(name, 'ate 1 pizza and earned 2 energy!')
            pizza = pizza - 1
            energy = energy +2
        if(ans.lower() == 'g'):
            print(name, 'played 1 game and earned 4 energy!')
            games = games - 1
            energy = energy + 4
        if(ans.lower() == 'e'):
            print("SHOPKEEPER: Come again soon!")
            break

def enter_Workplace():
    global job
    global money
    global salary
    global energy
    global name
    global findJob
                  
    if(job):
        print(name, 'built a bunch of stuff and earned $', salary)
        money = money + salary
        energy = energy-1
    else:
        print("You are currently searching for a job...\n\n", findJob, "more days until you find a job!")
    

def generate_RandomEvent():
    global job
    global findjob
    global money
    global salary
    
    event = int(random.uniform(0,4))
    print("Oh! you", event_list[event], "\n")
    if(event == 0):
        job = False
        daysLeftForJob = 2
    elif(event == 1):
        print("The robber stole $4!")
        money = money - 4
        print("\n\nMoney: $", money)
    elif(event == 2):
        print("salary increased by $1")
        salary = salary + 1
    else:
        print("you won $70!")
        money = money + 70
        print("\n\nMoney: $", money)
 
                  
def is_Failed():
    if(energy == 0):
        print('But, you ran out of energy! You failed!')
        return True
    if(money < 0):
        print("YOU ARE IN DEBT! YOU FAILED!!")
        return True
    return False






def init_event_Variables():
    #Event variables
    global location
    global event_list
    global nextEvent
    global event
    location = "B"
    event_list = ["were fired","were robbed", "were promoted", "won the lottery"]
    nextEvent = int(random.uniform(3,10))
    event = 0

def init_job_Variables():    
    #Job variables
    global job 
    global daysLeftForJob
    global salary
    job = True
    daysLeftForJob = 0
    salary = 1

def init_inventory_Variables():   
    #Inventory & Misc Variables
    global pizza
    global games
    global energy
    global money
    pizza = 5
    games = 2
    energy = 10
    money = 4
    
 
init_event_Variables()
init_job_Variables()
init_inventory_Variables()

global money
global energy
global location
global name
                  

#local variables
turn = 0
ans = ''

print("Welcome!\n\n")
name = input ("Enter name:\n\n>>>")
print("\n\nHello,", name)

while True:
    turn = turn + 1
    energy = energy - 1
    location = ask_Location()
                  
    if(location.lower() == 's'):
        enter_Shop()
    elif(location.lower() == 'i'):
        enter_StorageRoom()
    elif(location.lower() == 'b'):
        enter_Workplace()
    elif(location.lower == 'e'):
        break

    if(nextEvent == turn):
        generate_RandomEvent()
        nextEvent = int(random.uniform(3,10))
        turn = 0
                 
    if(daysLeftForJob == 0):
        job = True
    else:
        daysLeftForJob = daysLeftForJob - 1
    
    if(energy > 10):
        energy = 10                 
    
    if(is_Failed()):
        break







        
        
