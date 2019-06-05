import random

count = 1

discardedDeck=[]
class Game:

    def __init__(self):
        self.Name = ""# make it cpu for computer
        self.playerNumber = 0
        self.score = 0
        self.cardDeck = []
        self.spellGod = True
        self.spellRes = True
        self.chance = False

    def playerName(self):
        global count
        print("Enter a name for player : ", count)
        self.Name = raw_input()
        if(count == 1):
            self.playerNumber = 1
            count = 2
        else:
            self.playerNumber = 2
            count = 1

    def deal(self):
        if(self.playerNumber == 2):
            for i, v in enumerate(list1):
                if(i % 2 == 0):
                    self.cardDeck.append(list1[i])
        else:
            for i, v in enumerate(list1):
                if(i % 2 != 0):
                    self.cardDeck.append(list1[i])
# method playing and comparing cards
    def playCard(self):  # Called by method inside class with refference to object
        # print("Debugger>>>>>1",player1.cardDeck,player2.cardDeck)
        print("Your Card Is:")
        # print("Debug>>>>2",self.cardDeck)
        card = self.cardDeck.pop(0)
        # print("Debug>>>3",self.cardDeck)
        if(self.playerNumber == 1):
            card2 = getCard(2)
        else:
            card2 = getCard(1)

        # print("Debugger>>>>>4",player1.cardDeck,player2.cardDeck)
        print("Name : ", card['Name'])
        print("Rank : ", card['Rank'])
        print("Weight : ", card['Weight'])
        print("Height : ", card['Height'])
        # print("Check",p1Deck)
        ch = input("Choose power to play with [Press : 1->Rank 2->Weight 3->Height]")
        global discardedDeck
        print("GlobalDiscard",discardedDeck)      
        discardedDeck.append(card)
        discardedDeck.append(card2)
        if(ch == 1):
            if(card['Rank'] > card2['Rank']):
                player1.score = player1.score+1
                
                print (player1.playerName+" Wins!!  Score : ", player1.score)
                if(len(player2.cardDeck) > 0 and len(player1.cardDeck) > 0):
                    player1.play()
                else:
                    gameEnds()
            elif(card['Rank'] < card2['Rank']):
                    player2.score = player2.score+1
                    
                    print(player2.playerName + "Wins!!  Score : ")
                    if(len(player2.cardDeck) > 0 and len(player1.cardDeck) > 0):
                        player2.play()
                    else:
                        gameEnds()
        if(ch == 2):
            if(card['Weight'] > card2['Weight']):
                player1.score = player1.score+1
                print (player1.playerName + " Wins!!  Score : ", player1.score)
                if(len(player2.cardDeck) > 0 and len(player1.cardDeck) > 0):
                    player1.play()
                else:
                    gameEnds()
            elif(card['Weight'] < card2['Weight']):
                player2.score = player2.score+1
                print (player2.playerName + "Wins!!  Score : ", player2.score)
                if(len(player2.cardDeck) > 0 and len(player1.cardDeck) > 0):
                    player2.play()
                else:
                    gameEnds()
        if(ch == 3):
            print("asc",card,card2,card['Height'] > card2['Height'],card['Height'] ,card2['Height'],type(card2['Height']),type(card['Height']))
            if(card['Height'] > card2['Height']):
                player1.score = player1.score+1
                print (player1.playerName + "Wins!!  Score : ", player1.score)
                if(len(player2.cardDeck) > 0 and len(player1.cardDeck) > 0):
                    player1.play()
                else:
                    gameEnds()
            elif(card['Height'] < card2['Height']):
                player2.score = player2.score+1
                print (player2.playerName + "Wins!!  Score : ", player2.score)
                if(len(player2.cardDeck) > 0 and len(player1.cardDeck) > 0):
                    player2.play()
                else:
                    gameEnds()
        else:
            print("Invalid choice--->")
            self.playCard()

    def play(self):
        # if(self.Name=="CPU"):
        #     print("Going for cpu game play")
        #     self.cpuPlay()
        print(self.Name + " please choose")
        print("Press 1---->For playing your card")
        print("Press 2---->For using God Spell")
        print("Press 3---->For using Resurrection Spell")
        choice = input("Your choice :")
        if(choice == 1):
            self.playCard()
        elif(choice == 2):
            print("XX no conditio for god spell")
            if(self.spellGod):
                self.spellGod=False
                self.godSpell()
            else:
                print("God spell can only be used once in an entire game")
                self.play()
        elif(choice == 3):
            print("yyy no condition for resurrection spell")
            if(self.spellRes==False):
                print("You can only play a spell once")
                self.play()
                return
            self.resurrectionSpell()
            
        else:
            print("Invalid choice")
            self.play()
    # def cpuPlay(self):
    #     print("inside cpu player conditions ")
        # choice1=
    def godSpell(self):
        # global discardedDeck
        deck=[]
        if(self.playerNumber==1):
            deck=player2.cardDeck
        else:
            deck=player1.cardDeck
        print("Inside gods spell",deck)
        if(len(discardedDeck)>=0):
            print(self.Name + " Please choose a card for 2nd player")
            print("choose number between "+ " 1 "+" and "+ str(len(deck)))
            ch=int(input("Enter : "))-1
            if(ch<0 or ch>=len(deck)):
                print("Invalid Choice")
                self.godSpell()
            else:
                self.afterGod(ch)
        else:
            print("No card in the discarde cards..Try later")
            self.spellGod=True
            self.play()
    def afterGod(self,ch):
        # name=""
        obj=player1
        if(self.playerNumber==1):
            card=player2.cardDeck[ch]
            # name=player2.playerName
            obj=player2
            player2.cardDeck.remove(card)
            player2.cardDeck.insert(0,card)
        elif(self.playerNumber==2):
            card=player1.cardDeck[ch]
            # name=player1.Name
            obj=player1
            player1.cardDeck.remove(card)
            player1.cardDeck.insert(0,card)
        print(obj.playerName+" Please choose between continue play or resurrection spell")
        print("Press 1-->for continue play and Press 2-->for resurrection spell")
        # if(name=="CPU"):
        #     print("Check for cpu")
        gameMode=input()
        if(gameMode==1):
            self.play()
        elif(gameMode==2):
            obj.resAfterGod()
        else:
            print("Pllease enter a valid choice-->")
            self.afterGod(ch)

    def resurrectionSpell(self):
        global discardedDeck
        random.shuffle(discardedDeck)
        # print("Res---Spell discarded card-->",discardedDeck)
        if len(discardedDeck)>0:
            self.spellRes=False
            # print("Please choose card number for reserection--->",)
            ch=random.randrange(0,len(discardedDeck)-1)
            # print("Random card choosen for ",self.Name, " is ",discardedDeck[ch])
            print("Card choosen for->",self.Name)
            self.cardDeck.insert(0,discardedDeck[ch])
            discardedDeck.remove(discardedDeck[ch])

        else: 
            print("Empty discarded card deck please choose the spell later")
            self.spellRes=True
        self.play()
    def resAfterGod(self):
        global discardedDeck
        random.shuffle(discardedDeck)
        

        ch=random.randrange(0,len(discardedDeck)-1)
        # name=""
        obj=player1
        # code repeat
        if(self.playerNumber==1):
            # name=player2.playerName
            obj=player2
        else:
            # name=player1.playerName
            obj=player1
        if(self.spellRes==False):
            print("Reserection spell can only be used once by a player")
            print(obj.playerName," please make next move")
            obj.play()
        print(obj.Name," Please press 1 to allow the other player to play with new card and 2 to not allow")
        action=input("Please provide Input ")
        if(action==1):
            if(self.playerNumber==1):
                player2.cardDeck.insert(0,discardedDeck[ch])
                
            else:
                player1.cardDeck.insert(0,discardedDeck[ch])
                
            obj.play()
        elif(action==2):
            if(self.playerNumber==1):
                player2.cardDeck.insert(1,discarderdDeck[ch])
                
            else:
                player1.cardDeck.insert(1,discardedDeck[ch])
                
            discardedDeck.remove(discardedDeck[ch])
            obj.play()
        else:
            print("Invalid choice")
            obj.play()# check for invalid entry
def gameEnds():
    name=player1
    global discardedDeck
    discardedDeck=[]
    score=0
    if(player1.score > player2.score):
        name = player1
        score = player1.score
    elif(player1.score == player2.score):
        print("<---Its a Draw--->")
    else:
        name = player2
        # score = player2.score
    print(name.playerName," wins !!!")
    print("Score : ",name.score)
    pageLoad()

def getCard(player):
    # print("DEbufgger>>>",player)
    if(player == 2):
        # print("Removed from player 2....>>1",player2.cardDeck)
        a= player2.cardDeck.pop(0)
        # print("Removed from player 2",player2.cardDeck)
        return(a)
    else:
        # print("Removed from player 1....>>1",player1.cardDeck)
        a= player1.cardDeck.pop(0)
        # print("Removed from player 1....>>2",player1.cardDeck)
        return(a)
    # print()
#toss winner starts the game
def chance():
    # print("player1")
    
    # print("player1>>>>>>>",player1.chance,player2.chance )
    if(player1.chance):
        player1.chance = False
        player2.chance = True
        player1.play()
    elif(player2.chance):
        player2.chance = False
        player1.chance = True
        player2.play()

def shuffelCards():
    random.shuffle(list1)
#toss gamestart
def gamePlay():
    
    while(True):
        choice = input("Enter 1 to begin: ")
        if(choice != 1):
            print("Invalid choice")
        else:
            print("Game begins.....rolling dice for player one")
            break
    while(True):
        rand1 = random.randrange(1, 6)
        print("Dice roll---->", rand1)
        rand2 = random.randrange(1, 6)
        print("Player2 Dice Roll---->", rand2)
        if(rand1 > rand2):
            print("Player One wins...!!")
            player2.chance = False
            player1.chance = True
            break
        elif(rand2 > rand1):
            print("Player Two wins...!!")
            player2.chance = True
            player1.chance = False
            break
        else:
            print("Its a draw")

def cardCreation():
        c1 = {'Name': 'Kane', 'Rank': 7,'Height': '6.10', 'Weight': '410 pounds'}
        c2 = {'Name': 'BigShow', 'Rank': 3,'Height': '7.0', 'Weight': '500 pounds'}
        c3 = {'Name': 'Lita', 'Rank': 8,'Height': '5.11', 'Weight': '250 pounds'}
        c4 = {'Name': 'Tori', 'Rank': 6, 'Height': '5.9', 'Weight': '230 pounds'}
        c5 = {'Name': 'Stephni', 'Rank': 5,'Height': '5.4', 'Weight': '210 pounds'}
        c6 = {'Name': 'Stone Cold', 'Rank': 4,'Height': '6.10', 'Weight': '350 pounds'}
        c7 = {'Name': 'Rock', 'Rank': 1, 'Height': '6.2', 'Weight': '360 pounds'}
        c8 = {'Name': 'Mike', 'Rank': 2, 'Height': '6.4', 'Weight': '365 pounds'}
        # print("Sample test 1", c1)
    # Inserting card in a list
        global list1
        list1 = [c1, c2, c3, c4, c5, c6, c7, c8]
def pageLoad():
    global player1
    global player2
    player1 = Game()# object of class
    player2 = Game()
    cardCreation() #Creating deck of card
    shuffelCards() #Shuffelling card
    player1.playerName() #Screen to take player name
    player2.playerName() #same as above
    player1.deal() #deal cards for player 1
    player2.deal() #deal cards for player 2
    gamePlay() #toss 
    chance() #Toss winner starts the game

pageLoad()