
import random
from termcolor import colored

name = ("  ______   ________  ________  __        ______\n"+
" /      \ |        \|        \|  \      /      \ \n"+
"|  $$$$$$\| $$$$$$$$| $$$$$$$$| $$     |  $$$$$$\ \n" +
"| $$   \$$| $$__    | $$__    | $$     | $$  | $$\n"+
"| $$      | $$  \   | $$  \   | $$     | $$  | $$\n"+
"| $$   __ | $$$$$   | $$$$$   | $$     | $$  | $$\n"+
"| $$__/  \| $$_____ | $$_____ | $$_____| $$__/ $$\n"+
" \$$    $$| $$     \| $$     \| $$     \\ $$    $$\n"+
"  \$$$$$$  \$$$$$$$$ \$$$$$$$$ \$$$$$$$$ \$$$$$$\n")

print (colored(name , "green"))


players = input("Enter the number of players (between 2 to 6): ")
if players.isnumeric() == False or float(players) - round(float(players)) !=0 or int(players) < 2 or int(players) > 6:
    players = 3
    print("I expected between 2 and 6 players\nI'm setting the number of players to 3\n")


coins = input("Enter the number of coins per player (between 5 to 100): ")
if coins.isnumeric() == False or float(coins) - round(float(coins)) !=0 or int(coins) < 5 or int(coins) > 100:
    coins = 10
    print("I expected between 5 and 100 coins\nI'm setting the number of coins to 10\n")


print("Players:", players , "\n" + "Coins per player:", coins)


#player generator 6.0
plst = []
def playergenerator():
    for i in range (1,int(players)+1):
        plst.append("Player"+""+str(i))


#player balance
def currentbalance():
    print("\nCurrent balance:")
    for i in range (0,int(players)):
        print(plst[i],"has",balance[i],"coins")


balance = []
def newbalance():
    for i in range (1,int(players)+1):
        balance.append(int(coins))


#banker
currentbanker = [0]
def newbanker():
    banker = plst.index(plst[random.randint(0,len(plst)-1)])
    if banker is not currentbanker[0]:
        currentbanker[0] = plst[banker]
    else:
        newbanker()


#bet
pbet =[0,0,0,0,0,0]
B = [0]
def bankerbet():
    print("\n --------\n|" + " Banker |\n --------\n")
    bank = input("\nPlease enter a valid bank amount: ")
    if bank.isnumeric() == True and int(bank) <= balance[plst.index(currentbanker[0])]:
        B[0] = int(bank)
        balance[plst.index(currentbanker[0])] -= B[0]
        print("Bank amount set to :", B[0])
    else:
        bankerbet()


whobets = []
def playerbet():
    for i in pbet:
        pbet[i] = 0
    for i in range(0,int(players)):
        if plst[i] is not currentbanker[0] and B[0] - sum(pbet) > 0:
            whobets.append(plst[i])
            betting()

def betting():
    print(" -------\n|"+whobets[0]+"|\n -------")
    bet = input("\nPlease enter a valid bet: ")
    if bet.isnumeric() == True and int(bet) <= balance[plst.index(whobets[0])] and int(bet) <= B[0] and int(bet) <= B[0] - sum(pbet):
        pbet[plst.index(whobets[0])] = int(bet)
        balance[plst.index(whobets[0])] -= int(bet)
        whobets.clear()
    else:
        betting()



def bet():
    bankerbet()
    playerbet()
    if sum(pbet) == 0:
        print("\nNone of the players has bet. Bet restarts")
        bet()


#rolldice
dice = []
def rolldice():
    dice.clear()
    for i in range (0,3):
        dice.append(random.randint(1,6))
        dice.sort()
    print("You rolled",dice)
    return dice


#newround
score = []
def newround():
    if len(endgame) == 0:
        if score.count(0) != len(score) and len(win) == 0:
            scorecheck()
        currentbalance()

        if len(currentbanker) != 0:
            bankrupt()


        if len(endgame) != 0:
            print("Game Ends")


        else:
            score.clear()
            for i in range (0,int(players)):
                score.append(0)
            if len(win) != 0:
                if win[0] is currentbanker[0]:
                    print("\n"+currentbanker[0],"stays as the Banker")
                    playloop()

                else:
                    currentbanker[0] = win[0]
                    print("\n"+currentbanker[0],"is the new Banker")
                    playloop()
            else:
                newbanker()
                print("\n"+currentbanker[0],"is the new Banker")
                playloop()


#playloop
whoplays = []
def playloop():
    win.clear()
    bet()
    print("   ______________\n  /             / \n / Game starts /\n/_____________/\n")


    for i in range (0,int(players)):
        if plst[i] is currentbanker[0]:
            print(plst[i],": Banker with a bank amount of",B[0])
        else:
            if pbet[i] != 0:
                print(plst[i],": has bet",pbet[i])
    whoplays.append(plst.index(currentbanker[0]))
    print("\n --------\n|" + " Banker |, its your turn\n --------\n")
    play()
    whoplays.clear()
    for player in plst:
        if len(endgame) == 0 and player is not currentbanker[0] and pbet[plst.index(player)] != 0:
            whoplays.append(plst.index(player))
            print("\n -------\n|"+ player + "|,its your turn\n -------\n")
            play()
            whoplays.clear()
    if len(win) == 0:
        newround()


#play
def play():
    roll = input("Press <ENTER> to roll the dice: \n")
    if roll == "":
        rolldice()
        rules()
    else:
        play()


#rules
win = []
def rules():
    #auto-win
    if 4 in dice and 5 in dice and 6 in dice:
        print("You won!")
        balance[whoplays[0]] += sum(pbet) + B[0]
        win.append(plst[whoplays[0]])
        newround()


    elif dice[0] == dice[1] == dice[2]:
        print("You won!")
        balance[whoplays[0]] += sum(pbet) + B[0]
        win.append(plst[whoplays[0]])
        newround()


    elif 6 in dice and (dice[0]==dice[1]!=6 or dice[0]==dice[2]!=6 or dice[1]==dice[2]!=6):
        print("You won!")
        balance[whoplays[0]] += sum(pbet) + B[0]
        win.append(plst[whoplays[0]])
        newround()


    #auto-lose
    elif 1 in dice and 2 in dice and 3 in dice:
        print("You lose")


    elif 1 in dice and (dice[0]==dice[1]!=1 or dice[0]==dice[2]!=1 or dice[1]==dice[2]!=1):
        print("You lose")


    #score
    else:
        for i in range (1,7):
            if dice.count(i) == 2:
                while i in dice:
                    dice.remove(i)


        if len(dice) == 1:
            if dice[0] in range(2,6):
                print("\n")
                print(plst[whoplays[0]] , "scored",dice[0],"points")
                score[whoplays[0]] = dice[0]


        else:
            print("Roll again")
            play()


#scorecheck
def scorecheck():
    print(plst[score.index(max(score))],"wins by score\n")
    balance[score.index(max(score))] += sum(pbet) + B[0]


#bankrupt
endgame = []
def bankrupt():
    if 0 in balance:
        print(plst[balance.index(0)],"is bankrupt")
        endgame.append(1)
        newround()


#newgame
def newgame():
    playergenerator()
    newbalance()
    newround()


newgame()
