from .parser import parse_operation, parse_numbers
from .exceptions import CalculatorError

HELP = """
Welcome to the CLI Calculator!
Operations: add, sub, mul, div
Commands:   help, quit
Usage:
  1) Enter an operation name.
  2) Enter numbers separated by spaces (e.g., '3 4 5').
""".strip()

def run_repl(input_fn=input, print_fn=print):
    print_fn("CLI Calculator. Type 'help' for instructions. Type 'quit' to exit.")
    while True:
        try:
            op_in = input_fn("> Operation [add|sub|mul|div|help|quit]: ").strip()
            op = parse_operation(op_in)
            if op == "help":
                print_fn(HELP)
                continue
            if op == "quit":
                print_fn("Goodbye!")
                break

            nums_in = input_fn("> Enter numbers (space separated): ")
            values = parse_numbers(nums_in)

            result = op(values)  # op is a function
            if float(result).is_integer():
                print_fn(f"Result: {int(result)}")
            else:
                print_fn(f"Result: {result}")
        except CalculatorError as ce:
            print_fn(f"Error: {ce}")
        except EOFError:
            print_fn("\nGoodbye!")
            break
