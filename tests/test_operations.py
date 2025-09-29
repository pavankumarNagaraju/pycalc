import pytest
from pycalc.operations import add, sub, mul, div
from pycalc.exceptions import CalculatorError

@pytest.mark.parametrize("values, expected", [
    ([1, 2], 3.0),
    ([1, 2, 3, 4], 10.0),
    ([-1, 1], 0.0),
    ([0.5, 0.25], 0.75),
])
def test_add(values, expected):
    assert add(values) == pytest.approx(expected)

@pytest.mark.parametrize("values, expected", [
    ([5, 2], 3.0),
    ([10, 3, 2], 5.0),
    ([-1, -1], 0.0),
])
def test_sub(values, expected):
    assert sub(values) == pytest.approx(expected)

@pytest.mark.parametrize("values, expected", [
    ([2, 3], 6.0),
    ([2, 3, 4], 24.0),
    ([-2, 3], -6.0),
    ([0.5, 0.5], 0.25),
])
def test_mul(values, expected):
    assert mul(values) == pytest.approx(expected)

@pytest.mark.parametrize("values, expected", [
    ([8, 2], 4.0),
    ([100, 5, 2], 10.0),
    ([-9, 3], -3.0),
])
def test_div(values, expected):
    assert div(values) == pytest.approx(expected)

@pytest.mark.parametrize("func", [add, sub, mul, div])
def test_all_ops_require_two_or_more(func):
    with pytest.raises(CalculatorError):
        func([1])
def test_div_by_zero_raises():
    from pycalc.operations import div
    from pycalc.exceptions import CalculatorError
    import pytest
    with pytest.raises(CalculatorError):
        div([10, 0])
