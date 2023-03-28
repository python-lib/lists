from sum_of_all import sums
from product_of_all import products
from number_of_letters import words
from common_data import common_data
from removal_of_indexes import nfl_teams
from only_odds import only_odds
from three_random_numbers import three_random_numbers

if __name__ == '__main__':
    print(sums([1, -9, 2, 4, 10, -23]))
    print(products([1, -9, 2, 4, 10, -23]))
    print(words(4, "The cat is always in the hat in doctor sues"))
    print(common_data([1, 2, 3, 4, 5], [1, 3, 5, 6, 7]))
    print(nfl_teams())
    print(only_odds())
