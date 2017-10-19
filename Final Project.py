######################################################################
# Author: Abdirahman Mohamed
# Username: mohameda
# Assignment: P0: Final Project
# Credits: Dr. Scott Heggen and Vincent Davis
# Purpose: Synthesize element of learning from the entire course into a single, final project
# Game Name: Ya Tseeb o Tkheeb
# The game is basically a cards game where two people play against each other and who ever has two kings will win the game.
# Instructions:
#step 1: The program will assign you four random cards
#step 2: The player will discard a card of his/her choosing, then the program will replace it with a random card
#step 3: The other player will be going through step 1 and will do step 2.
#step 4: Continue playing until a winner is determined

#####################################################################
import random  # importing the random module
suits = ["Clubs", "Diamonds", "Hearts", "Spades"]  # card suits
ranks = ["Ace", "2", "3", "4", "5", "6", "7",
             "8", "9", "10", "Jack", "Queen", "King"] # card ranks

class Card:
    """This class called cards. Returnes the cards which are made of suits and ranks"""
    def __init__(self, suit=0, rank=0): # insitilize the class
        self.suit = suit
        self.rank = rank

    def __str__(self):
        # returnes suit and rank
        return (self.ranks[self.rank] + " of " + self.suits[self.suit])


class Deck:
    """This is the deck class. It returnes the card's deck,shuffle it for players and remove it from the deck"""
    def __init__(self):

        self.cards = []
        for suit in suits:
            for rank in ranks:

                    self.cards.append(Card(suit, rank)) # list of cards
    def __str__(self):
        s = ""
        for i in range(7):
            s = s + " " * i + str(self.cards[i]) + "\n"
        return s

    def shuffle(self,deck):
        for i in range(7):
            j = i
            (self.cards[i], self.cards[j]) = (self.cards[j], self.cards[i])

    def remove(self, card):
        if card in self.cards:
            index = self.cards.index(card) # an element of the list of cards
            del self.cards[index] # deletes the element from the list of cards


class Player:
    """This is the player's class. This class initialises the player's hands which draws and removes cards"""
    def __init__(self,deck=None):

        self.hand = [] # A player's hand
    def __str__(self):
        s = []
        for card in self.hand:
            s.append(str(card.rank))
        return str(s)  # returnes hands with cards

    def draw (self, deck):
        self.hand.append(deck.cards.pop(random.randint(0,len(deck.cards)-1)))


    def win(self):
        king_count = 0
        for card in self.hand:
            if card.rank=="King": #The condition of winning
                king_count += 1

        if king_count > 1:
            return True # if a player had two kings, he will win
        else:
            return False

    def remove(self):
        print(self)
        card = ""
        while card not in self.hand:
            picked_card = input("Which card would you like to remove? ")

            for card in self.hand:
                if card.rank == picked_card:
                    index = self.hand.index(card)

                    del self.hand[index] # deletes the card the player have removed
                    break
            return self.hand


class Game:
    """Initialises two players in the game"""
    def __init__(self):
        # create a deck of cards
        self.deck = Deck()
        # create two players
        self.p1 = Player(self.deck)
        self.p2 = Player(self.deck)

def main():
    """The Tseeb o Tkheeb game. Each player will draw 4 cards, discard one if they dont have two kings, if they do have two kings, they will win"""
    # initializes game
    game = Game()
    # game starts
    for i in range(4):
        game.p1.draw(game.deck) # player one has 4 cards
    for i in range(4):
        game.p2.draw(game.deck) # player two has 4 cards
    while not game.p1.win() and not game.p2.win() and len(game.deck.cards) > 0:
        if game.p1.win()!=True:
            game.p1.remove() # player one removes a card from hand
            game.p1.draw(game.deck) # player one draws a card from the deck
        else:
            break
        if game.p2.win()!=True:
            game.p2.remove() # player two removes a card from hand
            game.p2.draw(game.deck) # player two draws a card from the deck
        else:
            break

    if game.p1.win() and game.p2.win():
        print("Tie!") # it will print a tie if both have won
    else:
        if game.p1.win(): # if player one wins
            print("Player 1 wins")
        else: # player two would be the winner
            print("Player 2 wins")




if __name__ == '__main__':
    main() #Call the main function


