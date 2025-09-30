from .exceptions import CalculatorError

def _require_at_least_two(values):
    if len(values) < 2:
        raise CalculatorError("Please provide at least two numbers.")
    return values

def add(values):
    _require_at_least_two(values)
    total = 0.0
    for v in values:
        total += v
    return total

def sub(values):
    _require_at_least_two(values)
    result = values[0]
    for v in values[1:]:
        result -= v
    return result

def mul(values):
    _require_at_least_two(values)
    result = 1.0
    for v in values:
        result *= v
    return result

def div(values):
    _require_at_least_two(values)
    result = values[0]
    for v in values[1:]:
        if v == 0:
            raise CalculatorError("Division by zero is not allowed.")
        result /= v
    return result

def pow(values):
    """Exponentiate left-to-right: (((a ** b) ** c) ** d) ..."""
    _require_at_least_two(values)
    result = values[0]
    for v in values[1:]:
        result = result ** v
    return result
