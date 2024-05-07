# Mölkky score card

import sys

class Game:
    def __init__(self):
        self.players = []
        self.run()
    
    def list_players(self):
        while True:
            num = int(input("How many players? "))
            if num <= 0: print("You need to have at least 1 player.")
            else:
                for i in range(num):
                    self.players.append(Player(input(f"Enter name for player {i+1}: ")))
                break
    
    def run(self):
        self.list_players()
        playersout = []
        while True:
            for player in self.players:
                if player.isout:
                    continue
                elif len(playersout) == len(self.players) - 1:
                        print(f"{player.name}, you're the only one left, you won.")
                        sys.exit(0)
                else:None
                        
                print(f"\nPlayer {player.name}'s turn.")
                
                while True:
                    try:
                        newpts = input("How many points did you get? ")
                        if newpts == "ex":
                            print("Exiting.")
                            sys.exit(0)
                        else:
                            newpts = int(newpts)

                        if 0 <= newpts <= 12:
                            break
                        else:
                            print("Incorrect value. Try again.")
                    except ValueError:
                        print("Not an integer. Try again.")
                        continue
                    
                player.throws.append(newpts) 
                if len(player.throws) > 3:
                    player.throws.pop(0)

                if player.throws == [0, 0, 0]:
                    print("Three strikes and you're out!")
                    player.isout = True
                    playersout.append(player)

                player.points += newpts
                if player.points < 50 and not player.isout:
                    print(f"Current points: {player.points}")
                    continue
                elif player.points > 50:
                    print("50p exceeded. Continue from 25.")
                    player.points = 25
                    continue
                elif player.points == 50:
                    print("You got to 50 points first. You win the game.")
                    sys.exit(0)

class Player:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.throws = []
        self.isout = False

def main():
    Game()

if __name__ == "__main__":
    main()