#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 7 Assignment - Pig Game"""


import random


class Die(object):
    """A dice class.

    Generates a random number from 1 to 6.
    """

    random.seed(0)

    def __init__(self):
        """Constructor for the Die() class."""
        self.rolled = 0

    def roll(self):
        self.rolled = random.randint(1, 6)
        return self.rolled


class Player(object):
    """docstring"""
    def __init__(self, name):
        self.name = name
        self.totscore = 0
        self.turnscore = 0
        self.turn_status = 0
        #print self.name


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
                print '{} rolled a {}.'.format(player.name, roll)
                player.turnscore += roll
                print ('Your current total '
                       'for this turn is {}.').format(player.turnscore)
                self.turn_choice(player)


    def turn_choice(self, player):
        """Pig player game turn decision. Asks a player if they would like to
        hold or roll the dice to keep points, or roll again to risk losing or
        add more, respectively.
        """
        choice = raw_input('{}, Hold or Roll?'.format(player.name))
        choice = (choice[0])
        if choice.lower() == 'h':
            player.totscore += player.turnscore
            if player.totscore >= 100:
                print ('{} wins with '
                       'a score of {}.').format(player.name, player.totscore)
                # Need End Game Function.
            else:
                player.turnscore = 0
                print ('{}\'s score is {}.'
                       ' Pass die to next'
                       'player.').format(player.name, player.totscore)
                self.next_player()
        elif choice.lower() == 'r':
            self.turn(player)
            if player.totscore >= 100:
                print ('{} wins with '
                       'a score of {}.').format(player.name, player.totscore)
                # Play again or exit?
        else:
            print '**Enter Hold or Roll, without quotes.**'
            # raise exception?


    def next_player(self):
        """Swithces to the next player in the game."""
        if self.player1.turn_status == 1:
            self.player1.turn_status = 0
            self.turn(self.player2)
        else:
            self.player2.turn_status = 0
            self.turn(self.player1)
