# """This program plays a game of Rock, Paper, Scissors between two Players,
# and reports both Player's scores each round."""
# """The Player class is the parent class for all of the Players"""

import random

moves = ['rock', 'paper', 'scissors']


# Parent class
class Player:
    def move(self):
        return RandomPlayer.random_move(self)

    # Learn function to memorize opponent's move and return the same
    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move
        return self.their_move


# Human class which allows the users to play the game
class HumanPlayer(Player):
    def move(self):
        return input("rock, paper, scissors ? > ").lower()


# Reflect class which mimics the opponent's move in the next round
class ReflectPlayer(Player):
    def __init__(self):
        self.round = 0

    def move(self):
        # Since it cannot mimic opponent's move in the first Round
        # It returns a random move from the moves list
        while self.round == 0:
            self.round += 1
            return RandomPlayer.random_move(self)
        # returns the opponent's move from the previous round
        return self.their_move


# CyclePlayer class which cycles its own moves from the 'moves' list
class CyclePlayer(Player):
    def __init__(self):
        self.round = 0

    def move(self):
        # Round 1 returns a random move
        while self.round == 0:
            self.round += 1
            return RandomPlayer.random_move(self)
        # Round 2 returns the adjacent/next item from the 'moves' list
        try:
            return moves[moves.index(self.my_move) + 1]
        # If index exceeds the length of the list,
        # It circles back to its fist item
        except IndexError:
            return moves[0]


# RandomPlayer class which returns a random move from the 'moves' list
class RandomPlayer():
    def random_move(self):
        return random.choice(["rock", "paper", "scissors"])


# Constant player class which returns a constant - 'rock'
class ConstantPlayer():
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


# beats function which returns a boollean vaule of game rule
def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


# Game class which decides the length of the game, announce winner
# and condition to terminate the game
class Game():
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1.win = 0
        self.p2.win = 0
        self.round = 0
        self.game = "initialized"

    # function to announce the winner scenario
    def announce_winner(self):
        print(f"\nTotal Score : "
              f"Opponent Wins - {self.p1.win}, Your Wins - {self.p2.win}")
        if self.p1.win > self.p2.win:
            print("Game Result : ** Opponent wins the Game **")
        elif self.p1.win < self.p2.win:
            print("Game Result : ** You win the Game **")
        else:
            print("Game Result : ** The Game is a Tie **")

    def play_round(self):
        # calls the player1 move
        move1 = self.p1.move()
        # calls the player2 move
        move2 = self.p2.move()
        # In case user injects a unrecognized input, it loops itself
        while move2 not in moves:
            move2 = self.p2.move()
        print(f"You Played\t: {move2}  \nOpponent Played : {move1}")
        # Learn opponent's move
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        # condition to determine Player1 victory scenario
        if beats(move1, move2):
            self.p1.win += 1
            print("Round Result\t: ** Opponent Wins **")
        # condition to determine game tie scenario
        elif move1 == move2:
            print("Round Result\t: ** Game Tie **")
        # condition to determine Player2 victory scenario
        else:
            self.p2.win += 1
            print("Round Result\t: ** You Win **")
        # statement to display total score every round
        print(f"Score until now : Opponent "
              f"- {self.p1.win}, You - {self.p2.win}")

    # Game method to play a match of several rounds
    def play_game(self):
        print("Game start!")
        # Case: player does not want to quit / play game again
        while self.game != "quit" and self.game != "no":
            self.round += 1
            print(f"\n[Round {self.round}]")
            self.play_round()
            self.game = input("\nPlay again? Type 'quit' to Quit > ").lower()
            # Condition to handle unrecognized input on 'self.game'
            while (self.game != "play again" and self.game != "yes") and \
                  (self.game != "quit" and self.game != "no"):
                self.game = input("Play again? Type 'quit' to Quit > ").lower()
        # function method to announce winner
        self.announce_winner()
        print("Game over!")

    # Game method to play a single round
    def play_game_once(self):
        print("Game Start!")
        self.play_round()
        print("Game over!")


# Case: Only if Game executed directly
if __name__ == '__main__':
    # Case1: For Game between 'Computer - (random move)' and User -
    # uncomment below line and comment out 'line 164' 'line 167' and 'line 170'
    game = Game(Player(), HumanPlayer())
    # Case2: For Game between 'Computer - (Reflect User Moves)' and 'User' -
    # uncomment below line and comment out 'line 161' 'line 167' and 'line 170'
    # game = Game(ReflectPlayer(), HumanPlayer())
    # Case3: For Game between 'Computer - (Cycle Moves)' and 'User' -
    # uncomment below line and comment out 'line 161' 'line 164' and 'line 170'
    # game = Game(CyclePlayer(), HumanPlayer())
    # Case4: For Game between 'Contant move - (rock)' and 'User' -
    # uncomment below line and comment out 'line 161' 'line 164' and 'line 167'
    # game = Game(ConstantPlayer(), HumanPlayer())

    # Game method to play a match of several rounds -
    # uncomment below line and comment out 'line 177'
    game.play_game()
    # Game method to play a single round -
    # uncomment below line and comment out 'line 174'
    # game.play_game_once()
