from unittest.mock import patch

import pytest

from src.pytemplate.entrypoints.cli.main import main


def run_main_with_inputs(inputs):
    with patch("builtins.input", side_effect=inputs):
        with patch("builtins.print") as mocked_print:
            main()
            return mocked_print


def test_main_add():
    inputs = ["45", "35", "add"]
    mocked_print = run_main_with_inputs(inputs)
    mocked_print.assert_called_with("The result is: 80")


def test_main_subtract():
    inputs = ["45", "35", "subtract"]
    mocked_print = run_main_with_inputs(inputs)
    mocked_print.assert_called_with("The result is: 10")


def test_main_multiply():
    inputs = ["45", "35", "multiply"]
    mocked_print = run_main_with_inputs(inputs)
    mocked_print.assert_called_with("The result is: 1575")


def test_main_divide():
    inputs = ["45", "15", "divide"]
    mocked_print = run_main_with_inputs(inputs)
    mocked_print.assert_called_with("The result is: 3")


def test_main_invalid_action():
    inputs = ["45", "35", "unknown"]
    mocked_print = run_main_with_inputs(inputs)
    mocked_print.assert_called_with("Invalid action")
