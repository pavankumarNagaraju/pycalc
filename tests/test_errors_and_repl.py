import sys, subprocess
import pytest
from pycalc.parser import parse_operation, parse_numbers
from pycalc.exceptions import CalculatorError
from pycalc import operations as ops

def test_parse_operation_valid():
    assert parse_operation("add") is ops.add
    assert parse_operation("SUB") is ops.sub
    assert parse_operation("mul") is ops.mul
    assert parse_operation("div") is ops.div
    assert parse_operation("help") == "help"
    assert parse_operation("quit") == "quit"

def test_parse_operation_invalid():
    with pytest.raises(CalculatorError):
        parse_operation("pow")

def test_parse_numbers_valid():
    assert parse_numbers("1 2 3") == [1.0, 2.0, 3.0]
    assert parse_numbers("  -2.5   4 ") == [-2.5, 4.0]

@pytest.mark.parametrize("bad", ["", "   ", None])
def test_parse_numbers_missing(bad):
    with pytest.raises(CalculatorError):
        parse_numbers(bad)

def test_parse_numbers_invalid_token():
    with pytest.raises(CalculatorError):
        parse_numbers("1 two 3")

def test_run_as_module_shows_help_and_quits():
    cmd = [sys.executable, "-m", "pycalc"]
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    out, err = proc.communicate("help\nquit\n", timeout=10)
    assert proc.returncode == 0
    assert "CLI Calculator" in out
    assert "Operations: add, sub, mul, div" in out
    assert "Goodbye!" in out
    assert err == ""
