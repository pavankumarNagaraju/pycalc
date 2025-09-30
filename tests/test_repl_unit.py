from pycalc.repl import run_repl

class InputFeeder:
    def __init__(self, items):
        self._it = iter(items)
    def __call__(self, prompt=""):
        return next(self._it)

def test_repl_happy_path_and_error():
    inputs = [
        "pow", "2 3",          # -> Result: 8   (left-to-right: 2**3)
        "add", "1 2",          # -> Result: 3   (int formatting)
        "mul", "0.5 0.25",     # -> Result: 0.125 (float formatting)
        "div", "10 0",         # -> Error: Division by zero...
        "quit"                 # -> Goodbye!
    ]
    feeder = InputFeeder(inputs)
    out = []
    run_repl(input_fn=feeder, print_fn=out.append)

    text = "\n".join(out)
    assert "CLI Calculator" in text
    assert "Result: 8" in text
    assert "Result: 3" in text
    assert "Result: 0.125" in text
    assert "Error: Division by zero is not allowed." in text
    assert "Goodbye!" in text

def test_repl_eof_exit():
    def raising_input(_prompt=""):
        raise EOFError
    out = []
    run_repl(input_fn=raising_input, print_fn=out.append)
    assert any("Goodbye!" in line for line in out)
