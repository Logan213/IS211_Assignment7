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
        """The dice roll function for the Die() class.

        Attributes:
            Die (class): Calls the Die() class.

        Returns:
            (Int) An integer to be used as the rolled die value in the pig game.
        """
        self.rolled = random.randint(1, 6)
        return self.rolled


class Player(object):
    """A game participant class.

    Stores the player names to be used in the pig game.

    Args:
        name (string): The name of the player.

    Attributes:
        name (string): The name of the player.
    """
    def __init__(self, name):
        """Constructor for the Player() class.

        Args:
            name (string): The name of the player.

        Attributes:
            Player() (class): Calls the Player() class.
            name (string): The name of the player.
        """
        self.name = name
        self.totscore = 0
        self.turnscore = 0
        self.turn_status = 0
        print 'Welcome to the game of pig, {}.'.format(self.name)


class Game(object):
    """A pig game class.

    Stores the player names by calling the Player() class and calls the Die
    class to use in the game.

    Args:
        player1 (string): the name of player 1.
        player2 (string): the name of player 2.

    Attirbutes:
        player1 (string): the name of player 1.
        player2 (string): the name of player 2.
    """
    def __init__(self, player1, player2):
        """Constructor for the Game() class.

        Args:
            player1 (string): the name of player 1.
            player2 (string): the name of player 2.

        Attributes:
            Game (class): Call the Game() class.
            Player (class): Calls the Player() class.
            player1 (string): the name of player 1.
            player2 (string): the name of player 2.
        """
        self.player1 = Player(player1)
        self.player2 = Player(player2)
        self.die = Die()
        self.turn(self.player1)

    def turn(self, player):
        """The initial turn function for the Pig game."""
        player.turn_status = 1
        print 'It is {}\'s turn.'.format(player.name)
        while player.turn_status == 1 and player.totscore < 100:
            roll = self.die.roll()
            if roll == 1:
                print ('Sorry {}! You rolled a 1 and forfeit all '
                       'points this turn. Your total score is {}. Pass die '
                       'to next player.').format(player.name, player.totscore)
                player.turnscore = 0
                self.next_player()
            else:
                print '{} rolled a {}.'.format(player.name, roll)
                player.turnscore += roll
                print ('Your current point total '
                       'for this turn is {}. Your total '
                       'score is {}').format(player.turnscore, player.totscore)
                self.turn_choice(player)
        print ('{} score is {} and'
               'has won the game!').format(player.name, player.totscore)

    def turn_choice(self, player):
        """Pig game turn decision. Asks a player if they would like to
        hold or roll the dice to keep points, or roll again to risk losing all
        points that turn, or add more to the turn total.

        Args:
            player (string): the name of the player whose turn it currently is.

        Returns:
            String: Depending on the choice entered, a message stating the
            points added to the turn score, the total score, or the winner
            of the pig game.
        """
        choice = raw_input('{}, Hold or Roll?'.format(player.name))
        choice = (choice[0])
        if choice.lower() == 'h':
            player.totscore += player.turnscore
            print ('{} points have been '
                   'added to {}\'s total '
                   'score.').format(player.turnscore, player.name)
            if player.totscore >= 100:
                print ('{} wins with '
                       'a score of {}.').format(player.name, player.totscore)
                raise SystemExit
            else:
                player.turnscore = 0
                print ('{}\'s score is now {}.'
                       ' Please pass die to next'
                       'player.').format(player.name, player.totscore)
                self.next_player()
        elif choice.lower() == 'r':
            self.turn(player)
        else:
            print '***Type Hold (H/h) or Roll (R/r) only, please.***'
            self.turn_choice(player)

    def next_player(self):
        """Swithces to the next player in the game.

        Attributes:
            Game (class): Calls the Game() class.
        """
        if self.player1.turn_status == 1:
            self.player1.turn_status = 0
            self.turn(self.player2)
        else:
            self.player2.turn_status = 0
            self.turn(self.player1)
