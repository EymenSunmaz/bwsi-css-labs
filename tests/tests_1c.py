import pytest
from labs.lab_1.lab_1c import max_subarray_sum
def tests():
    assert max_subarray_sum([2,2,2,2]) == 2
    assert max_subarray_sum([0,1,0,1,0,1]) == 1
    assert max_subarray_sum([-1,-2,-3,-4,-3,-6]) == -1