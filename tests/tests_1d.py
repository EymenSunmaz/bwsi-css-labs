import pytest
from labs.lab_1.lab_1d import two_sum
def tests():
    assert two_sum([2,2,2,2],9) == [] #Non reply
    assert two_sum([1,2,4,4],8) == [2,3] # 
    assert two_sum([2,5,8,6],6) == [] #Same number
    assert two_sum([1,2,2,1],3) == [0,1]
def test_len():
    assert two_sum([1,2],3)==[0,1]
    assert two_sum([1],2) == []
