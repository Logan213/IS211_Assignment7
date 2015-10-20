#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 7 Assignment - Pig Game"""


import random


class Die(object):
    """A dice class.

    Generates a random number from 1 to 6.

    Args:
        None.

    Attribues:
        None
    """

    random.seed(0)

    def __init__(self):
        """Constructor for the Die() class.

        Args:
            None.

        Attributes:
            None.

        Returns:
            None.
        """"
        self.rolled = 0

    def roll(self):
        """Returns a randomly generated number between 1 and 6 to be used in
        a turn of the game Pig.
        """
        self.rolled = random.randint(1, 6)
        return self.rolled


class Player(object):
    """A pig game player class."""
    def __init__(self, name):
        self.name = name
        self.totscore = 0
        self.turnscore = 0
        self.turn_status = 0
        print self.name

    def turn_choice(self):
        """Pig player game turn decision. Asks a player if they would like to
        hold or roll the dice to keep points, or roll again to risk losing or
        add more, respectively.
        """
        choice = raw_input('{}, Hold or Roll?'.format(self.name))
        choice = str(choice[0]).lower()
        if choice == 'h':
            self.totscore += self.turnscore
            if self.totscore >= 100:
                print ('{} wins with '
                       'a score of {}.').format(self.name, self.totscore)
                # Need End Game Function.
            else:
                self.turnscore = 0
                print ('{}\'s score is {}.'
                       ' Pass die to next'
                       'player.').format(self.name, self.totscore)
                Game.next_player(Game)
        elif choice == 'r':
            Game.turn(self.name)


class Game(object):
    """A game rules class."""
    def __init__(self, player1, player2):
        """Constructor Docstring."""
        self.player1 = Player(player1)
        self.player2 = Player(player2)
        self.die = Die()
        self.turn(self.player1)


    def turn(self, player):
        """The initial turn function for the Pig game."""
        player.turn_status = 1
        while player.turn_status == 1 and player.totscore < 100:
            roll = self.die.roll()
            if roll == 1:
                print ('{}, You rolled a 1 and forfeit all '
                       'points this turn. Pass die '
                       'to next player.').format(player)
                player.turnscore = 0
                self.next_player()
            else:
                print 'You rolled a {}.'.format(roll)
                player.turnscore += roll
                print ('Your current total '
                       'for this turn is {}.').format(player.turnscore)
                player.turn_choice()


    def next_player(self):
        """Swithces to the next player in the game."""
        if self.player1.turn_status == 1:
            self.player1.turn_status = 0
            self.turn(self.player2)
        else:
            self.player2.turn_status = 0
            self.turn(self.player1)
