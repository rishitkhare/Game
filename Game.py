#Let's Make a game!!
#
#Recommendations:
#
# - multiple dimensions
#     1. survival (energy consumption)
#     2. upgrades (tools) (Either earn more, or less energy)
#     3. unexpected events (Fired from job, enemy attacks, robbery)

pizza = 5
games = 0
energy = 10
money = 0
ans = 0
print("Welcome!\n\n")
name = input ("Enter name:\n\n>>>")
print("\n\nHello,", name)



while True:
    print('\nType S for shop\n\nType B to build\n\nType I for inventory\n\n\n\nMoney: $', money, '\n\nwillpower:',energy, "/10\n\n\n\n\n\n\n\n")
    location = input('>>>')
    if(location == 'S' or location == 's'):
        if(money == 0):
            print("STOREKEEPER: If you don't have money, what good are you to me? \n\nCome back when you have something useful!!")
        else:
            print("STOREKEEPER: What would you like? G for video game ($ 5), P for pizza ($ 2)! \nThat's all we sell!\n\n(E to exit)")
            ans = input("\n\n>>>")
            if(ans == 'G' and money > 4):
                print('\n\n',name,'paid $ 5 and recieved 1 game!')
                money = money - 5
                games = games + 1
            elif(money < 5 and ans == 'G'):
                    print("SHOPKEEPER: You don' have enough money!!")
            if(ans == 'P' and money > 1):
                print('\n\n',name,'paid $ 2 and recieved one pizza!')
                money = money -2
                pizza = pizza + 1
            elif(money < 2):
                    print("SHOPKEEPER: You don' have enough money for that!!")
                
                
    if(location == 'b' or location == 'B'):
        print(name, 'built a bunch of stuff and earned $ 1!')
        money = money + 1
    if(location == 'E' or location == 'e'):
        break
    if(location == 'I' or location == 'i'):
        print('Select an energy fufiller! \n\nInventory:\n\nPizzas:',pizza, '\nGames:',games, '\n\n(E to exit)')
        ans = input('\n\n>>>')
        if(ans == 'P'):
            print(name, 'ate 1 pizza and earned 2 willpower!')
            pizza = pizza - 1
            energy = energy +2
        if(ans == 'G'):
            print(name, 'played 1 game and earned 4 willpower!')
            games = games - 1
            energy = energy + 4
    if(energy > 10):
        energy = 10
    if(ans == 'E' or  ans == 'e' or ans == ''):
        print('\n\nExited inventory!')
    else:
        energy = energy - 1
    if(energy == 0):
        print('But, you ran out of willpower! You failed!')
        break













        
        
