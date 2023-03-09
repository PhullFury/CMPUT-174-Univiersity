'''
This program tests whether the file yahtzee2 works or not
Name: Harmanpreet Singh Phull
Date: 8th March 2023
'''

from yahtzee2 import num_of_a_kind, yahtzee

def test_three_of_a_kind_found():
    roll = (1,1,1,2,2)
    assert num_of_a_kind(roll, 3) == 7

def test_three_of_a_kind_not_found():
    roll = (1,1,2,2,3)
    assert num_of_a_kind(roll, 3) == 0

def test_four_of_a_kind_found():
    roll = (1,1,1,1,2)
    assert num_of_a_kind(roll, 4) == 6

def test_four_of_a_kind_not_found():
    roll = (1,1,2,2,3)
    assert num_of_a_kind(roll, 4) == 0

def test_yahtzee_found():
    roll = (1,1,1,1,1)
    assert yahtzee(roll) == 50

def test_yahtzee_not_found():
    roll = (1, 1, 1, 1, 2)
    assert yahtzee(roll) == 0