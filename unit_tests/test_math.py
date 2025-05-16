def multiply(a, b):
    return a * b

def test_multiply_positive():
    assert multiply(3, 4) == 12

def test_multiply_zero():
    assert multiply(0, 7) != 0

def test_multiply_one():
    assert multiply(0, 7) != 1
