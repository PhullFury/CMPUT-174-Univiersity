from yahtzee1 import sum_of_given_number, fill_upper_section

def test_sum_of_given_number_all_different():
    roll = (1,2,3,4,5)
    assert sum_of_given_number(roll, 1) ==  1
    assert sum_of_given_number(roll, 2) ==  2
    assert sum_of_given_number(roll, 3) ==  3
    assert sum_of_given_number(roll, 4) ==  4
    assert sum_of_given_number(roll, 5) ==  5
    assert sum_of_given_number(roll, 6) ==  0

def test_sum_of_given_number_all_same():
    roll = (1, 1, 1, 1, 1)
    assert sum_of_given_number(roll, 1) == 5
    assert sum_of_given_number(roll, 2) == 0
    assert sum_of_given_number(roll, 3) == 0
    assert sum_of_given_number(roll, 4) == 0
    assert sum_of_given_number(roll, 5) == 0
    assert sum_of_given_number(roll, 6) == 0

def test_sum_of_given_number_some_different():
    roll = (1, 2, 1, 2, 3)
    assert sum_of_given_number(roll, 1) == 2
    assert sum_of_given_number(roll, 2) == 4
    assert sum_of_given_number(roll, 3) == 3
    assert sum_of_given_number(roll, 4) == 0
    assert sum_of_given_number(roll, 5) == 0
    assert sum_of_given_number(roll, 6) == 0

def test_fill_upper_section():
    roll = (6, 2, 1, 5, 1)
    assert fill_upper_section(roll) == [2, 2, 0, 0, 5, 6]
