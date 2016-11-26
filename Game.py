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

def mainMenu():
    print('\nType S for shop\n\nType B to build\n\nType I for inventory\n\n\n\nMoney: $', money, '\n\nEnergy:',energy, "/10\n\n\n\n\n\n\n\n")

def enter_Shop():
    global money
    global games
    global pizza
    
    if(money == 0):
        print("STOREKEEPER: If you don't have money, what good are you to me? \n\nCome back when you have something useful!!")
    else:
        print("STOREKEEPER: What would you like? G for video game ($ 5), P for pizza ($ 2)! \nThat's all we sell!\n\n(E to exit)")
        ans = input("\n\n>>>")
    if(ans.lower() == 'g' and money > 4):
        print('\n\n',name,'paid $ 5 and recieved 1 game!')
        money = money - 5
        games = games + 1
    elif(money < 5 and ans.lower() == 'g'):
        print("SHOPKEEPER: You don' have enough money for that game!!")
    if(ans.lower == 'p' and money > 1):
        print('\n\n',name,'paid $ 2 and recieved one pizza!')
        money = money -2
        pizza = pizza + 1
    elif(money < 2):
        print("SHOPKEEPER: You don' have enough money for that pizza!!")

def display_Inventory():
    global games
    global pizza
    print('Select an energy fufiller! \n\nInventory:\n\nPizzas: p, Games: g, Exit: e')
    print('Pizzas:',pizza)
    print('Games:',games)

def init_event_Variables():
    #Event variables
    global location
    global event_list
    global eventTiming
    global event
    location = "B"
    event_list = ["were fired","were robbed", "were promoted", "won the lottery"]
    eventTiming = int(random.uniform(3,10))
    event = 0

def init_job_Variables():    
    #Job variables
    global job 
    global findJob
    global salary
    job = True
    findJob = 0
    salary = 1

def init_inventory_Variables():   
    #Inventory & Misc Variables
    global turn
    global pizza
    global games
    global energy
    global money
    global ans
    turn = 0
    pizza = 5
    games = 2
    energy = 10
    money = 4
    ans = ''
    
 

 

 

init_event_Variables()
init_job_Variables()
init_inventory_Variables()

global money
global turn
global energy
global location
global ans

print("Welcome!\n\n")
name = input ("Enter name:\n\n>>>")
print("\n\nHello,", name)

while True:
    turn = turn + 1
    #Main Menu
    mainMenu()
    location = input(">>>")
    #Shop
   
    if(location.lower() == 's'):
        enter_Shop()
    if(findJob == 0):
        job = True
    else:
        findJob = findJob - 1
    if(location.lower() == 'b'):
        if(job):
            print(name, 'built a bunch of stuff and earned $', salary)
            money = money + salary
            energy = energy-1
        else:
            print("You are currently searching for a job...\n\n", findJob, "more days until you find a job!")
    if(location.lower == 'e'):
        break
    if(location.lower() == 'i'):
        display_Inventory()
        ans = input('\n\n>>>')
        if(ans.lower() == 'p'):
            print(name, 'ate 1 pizza and earned 2 energy!')
            pizza = pizza - 1
            energy = energy +2
        if(ans.lower() == 'g'):
            print(name, 'played 1 game and earned 4 energy!')
            games = games - 1
            energy = energy + 4
    if(energy > 10):
        energy = 10
    if(ans.lower() == 'e'):
        print('\n\nExited inventory!')
    elif(not location.lower == "i"):
        energy = energy - 1
    if(eventTiming == turn):
        event = int(random.uniform(0,4))
        print("Oh! you", event_list[event], "\n")
        if(event == 0):
            job = False
            findJob = 2
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
        turn = 0
        eventTiming = int(random.uniform(3,10))
    if(energy == 0):
        print('But, you ran out of energy! You failed!')
        break
    if(money < 0):
        print("YOU ARE IN DEBT! YOU FAILED!!")
        break













        
        
