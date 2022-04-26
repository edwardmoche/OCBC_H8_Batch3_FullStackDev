from unittest import result
from my_sum import sum
 
def test_my_sum():
    input = [-1, 0, 8, 2]
    # result = my_sum([-1, 0, 8, 2])
    result = sum(input)
    assert result == 9, "Should be 9"


def test_my_sum_float():
    input = [3.2, 1.1, 0.8]
    # result = my_sum([-1, 0, 8, 2])
    result = sum(input)
    assert result == 5.1, "Should be 5.1"