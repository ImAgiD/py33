import pytest
from contextlib import nullcontext as does_not_raise
from src.main import *


# def test_plus():
#     x = 10
#     y = 20
#     assert plus_(x, y) == 30 

# def minus():
#     x = 10
#     y = 20
#     assert minus_(x, y) == -10 
    
# def minus():
#     x = 10
#     y = 20
#     assert minus_(x, y) == -10 
    
@pytest.mark.parametrize(
        'x, y, res, expectation',
        [
            (10, 2, 5, does_not_raise()),
            (-100, '2', -50, pytest.raises(TypeError)),  
            (100, 0, 100, pytest.raises(ZeroDivisionError))
        ]
        )

# def test_div(x, y, res):
#     assert div_(x, y) == res
    
# def test_div(x, y, res, expectation):
#     with expectation:
#         assert div_(x, y) == res

