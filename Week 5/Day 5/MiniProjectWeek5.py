import random
class RockPaperScissors(): 
    def __init__(self): 
        self.wins = 0 
        self.losses = 0 
        self.draws = 0

    def rock(self):  
        rand = random.choice(["r", "p", "s"])  
        if rand == "r": 
            print("Its a draw!") 
            self.draws += 1 
            mainmenu()
        elif rand == "p": 
            print("Computer chose Paper. You lost")
            self.losses += 1
            mainmenu()
        else: 
            print("The computer chose Scissors, You win!") 
            self.wins += 1
            mainmenu()

    def paper(self):  
        rand = random.choice(["r", "p", "s"])  
        if rand == "r": 
            print("Computer chose Rock, You Win") 
            self.wins += 1 
            mainmenu()
        elif rand == "p": 
            print("Its a Draw!")
            self.draws += 1 
            mainmenu()
        else: 
            print("The computer chose Scissors, You Lost!") 
            self.losses += 1
            mainmenu()

    def scissors(self):  
        rand = random.choice(["r", "p", "s"])  
        if rand == "r": 
            print("Computer chose Rock, You Lost") 
            self.losses += 1 
            mainmenu()
        elif rand == "p": 
            print("Computer chose Paper, you Win!")
            self.wins += 1 
            mainmenu()
        else: 
            print("Its a Draw!") 
            self.draws += 1
            mainmenu()

    
    
    def showresults(self):
        print("    Game Results:")
        print(f"    You Won {self.wins} times!") 
        print(f"    You Lost {self.losses} times!")
        print(f"    You Drew {self.draws} times!") 
        print("                                 ")
        print("                                 ")
        print("    Thank you for Playing!")





game = RockPaperScissors()

def playgame(): 
    move = input("Select (r)ock, (p)aper, or (s)cissors:   ") 
    if move == "r": 
        game.rock() 
    elif move == "p": 
        game.paper()
    elif move == "s": 
        game.scissors() 
    else: 
        print("Error") 
        playgame()

def mainmenu():
    print("   Menu")
    choose = input("   (g) Play a new Game\n   (x) Show scores and exit\n           :  ")  
    if choose == "g": 
        playgame() 
    elif choose == "x": 
        game.showresults()



mainmenu()
