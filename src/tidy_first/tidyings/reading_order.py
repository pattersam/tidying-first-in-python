"""Part 1, Chapter 05 - Reading Order"""

from __future__ import annotations

import dataclasses
import math
import logging
import typing as t

import hypothesis
import hypothesis.strategies as st

Input = tuple[str, int, float]
Output = t.Callable[[Input], bool]


@hypothesis.given(st.tuples(st.text(), st.integers(), st.floats()))
def run(args: Input) -> None:
    assert before()(args) == after()(args)


def before() -> Output:
    """A module with the important business rules at the bottom."""

    @dataclasses.dataclass
    class Arguments:
        a: str = "default"
        i: int = 1
        x: float = 0.5

    def _validate_args(args: Arguments) -> list[str] | None:
        validation_errors: list[str] = []
        if not args.a:
            validation_errors.append(
                f"Argument {args.a=} must not be None or an empty string"
            )
        if args.i > 100:
            validation_errors.append(
                f"Chosen value for {args.i=} is higher than 100..."
            )
        if args.x % 1 == 0:
            validation_errors.append(f"{args.x=} should have a remainder.")
        return validation_errors if validation_errors else None

    def _parse_args(raw_args: Input) -> Arguments | None:
        assert len(raw_args) == 3
        a, i, x = raw_args
        parsed_args = Arguments(a=a, i=i, x=x)
        if (validation_errors := _validate_args(parsed_args)) is not None:
            msg = f"{parsed_args=} has the {validation_errors=}."
            logging.info(msg)
            return None
        return parsed_args

    def module_entry_point(args: Input) -> bool:
        parsed_args = _parse_args(args)
        if parsed_args is None:
            return False
        return _run(parsed_args)

    def _run(args: Arguments) -> bool:
        return all([_process_a(args.a), _process_i(args.i), _process_x(args.x)])

    def _process_a(a: str) -> bool:
        return any(banned_word in a for banned_word in ["banned", "words"])

    def _process_i(i: int) -> bool:
        if i < 0 or i > 10:
            return False
        return True

    def _process_x(x: float) -> bool:
        try:
            floored = math.floor(x)
        except (ValueError, OverflowError):
            return False
        if (diff := x - floored) > 0.5:
            logging.info("this is close to the limit")
        return diff > 0.6

    return module_entry_point


def after() -> Output:
    """The module refactored to have the important business rules at the top."""

    def _run_command(args: Arguments) -> bool:
        return all([_process_a(args.a), _process_i(args.i), _process_x(args.x)])

    def _process_a(a: str) -> bool:
        return any(banned_word in a for banned_word in ["banned", "words"])

    def _process_i(i: int) -> bool:
        if i < 0 or i > 10:
            return False
        return True

    def _process_x(x: float) -> bool:
        try:
            floored = math.floor(x)
        except (ValueError, OverflowError):
            return False
        if (diff := x - floored) > 0.5:
            logging.info("this is close to the limit")
        return diff > 0.6

    def module_entry_point(args: Input) -> bool:
        parsed_args = _parse_args(args)
        if parsed_args is None:
            return False
        return _run_command(parsed_args)

    @dataclasses.dataclass
    class Arguments:
        a: str = "default"
        i: int = 1
        x: float = 0.5

    def _validate_args(args: Arguments) -> list[str] | None:
        validation_errors: list[str] = []
        if not args.a:
            validation_errors.append(
                f"Argument {args.a=} must not be None or an empty string"
            )
        if args.i > 100:
            validation_errors.append(
                f"Chosen value for {args.i=} is higher than 100..."
            )
        if args.x % 1 == 0:
            validation_errors.append(f"{args.x=} should have a remainder.")
        return validation_errors if validation_errors else None

    def _parse_args(raw_args: Input) -> Arguments | None:
        assert len(raw_args) == 3
        a, i, x = raw_args
        parsed_args = Arguments(a=a, i=i, x=x)
        if (validation_errors := _validate_args(parsed_args)) is not None:
            msg = f"{parsed_args=} has the {validation_errors=}."
            logging.info(msg)
            return None
        return parsed_args

    return module_entry_point


if __name__ == "__main__":
    run()
