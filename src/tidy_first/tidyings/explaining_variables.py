"""Part 1, Chapter 08 - Explaining Variables"""

import dataclasses
import math

import hypothesis
import hypothesis.strategies as st

Input = tuple[int | None, int, int]


@dataclasses.dataclass
class Output:
    x: int
    y: int


@hypothesis.given(st.tuples(st.integers() | st.none(), st.integers(), st.integers()))
def run(args: Input) -> None:
    assert before(*args) == after(*args)


def before(a: int | None, b: int, c: int) -> Output:
    """Transform `a`, `b`, `c` into `x` & `y`"""
    return Output(
        x=(a if a is not None else 1) + b - c + 42 + c**2,
        y=c * 2 + 15 - math.floor(99_000_000 / 180) + (a if a is not None else 1),
    )


def after(a: int | None, b: int, c: int) -> Output:
    """Transform `a`, `b`, `c` into `x` & `y`"""
    normalised_a = a if a is not None else 1
    heuristic_for_x = normalised_a + b - c + 42 + c**2
    flower_projection_of_y = c * 2 + 15 - math.floor(99_000_000 / 180) + normalised_a
    return Output(x=heuristic_for_x, y=flower_projection_of_y)


if __name__ == "__main__":
    run()
