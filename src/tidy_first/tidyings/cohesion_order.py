"""Part 1, Chapter 06 - Cohesion Order"""

import typing as t

import hypothesis
import hypothesis.strategies as st

Input = int
Output = t.Callable[[Input], int]


@hypothesis.given(st.integers())
def run(arg: Input) -> None:
    assert before()(arg) == after()(arg)


def before() -> Output:
    """A module with coupled functions scattered across it"""

    def double_then_add_one(arg: int) -> int:
        return add_one(multiply_by_two(arg))

    def subtract_one(arg: int) -> int:
        return arg - 1

    def special_square(arg: int) -> int:
        return multiply_by_two(arg) * arg

    def add_one(arg: int) -> int:
        return arg + 1

    def module_entry_point(arg: int) -> int:
        for func in [
            double_then_add_one,
            special_square,
            add_one,
            subtract_three,
            subtract_one,
        ]:
            arg = func(arg)
        return arg

    def subtract_three(arg: int) -> int:
        return arg - 3

    def multiply_by_two(arg: int) -> int:
        return arg * 2

    return module_entry_point


def after() -> Output:
    """The module refactored to have coupled functions adjacent to one another"""

    def module_entry_point(arg: int) -> int:
        for func in [
            double_then_add_one,
            special_square,
            add_one,
            subtract_three,
            subtract_one,
        ]:
            arg = func(arg)
        return arg

    def add_one(arg: int) -> int:
        return arg + 1

    def subtract_one(arg: int) -> int:
        return arg - 1

    def subtract_three(arg: int) -> int:
        return arg - 3

    def multiply_by_two(arg: int) -> int:
        return arg * 2

    def special_square(arg: int) -> int:
        return multiply_by_two(arg) * arg

    def double_then_add_one(arg: int) -> int:
        return add_one(multiply_by_two(arg))

    return module_entry_point


if __name__ == "__main__":
    run()
