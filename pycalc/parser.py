from .exceptions import CalculatorError
from . import operations as ops

DISPATCH = {
    "add": ops.add,
    "sub": ops.sub,
    "mul": ops.mul,
    "div": ops.div,
}

def parse_operation(op_str: str):
    key = (op_str or "").strip().lower()
    if key in ("help", "quit"):
        return key
    try:
        return DISPATCH[key]
    except KeyError as e:
        raise CalculatorError(
            f"Unknown operation: '{op_str}'. Try: add, sub, mul, div, help, quit."
        ) from e

def parse_numbers(s: str):
    if s is None:
        raise CalculatorError("Expected numbers, got nothing.")
    parts = [p for p in s.strip().split() if p]
    if not parts:
        raise CalculatorError("Please enter one or more numbers separated by spaces.")
    values = []
    for p in parts:
        try:
            values.append(float(p))
        except ValueError as e:
            raise CalculatorError(f"Invalid number: '{p}'") from e
    return values
