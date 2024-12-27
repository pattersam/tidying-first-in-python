"""Part 1, Chapter 07 - Move Declaration and Initialisation Together"""

import hypothesis
import hypothesis.strategies as st

Input = int | None
Output = str | None


@hypothesis.given(st.tuples(st.integers() | st.none(), st.integers() | st.none()))
def run(args: tuple[Input, Input]) -> None:
    assert before(*args) == after(*args)


def before(arg1: Input, arg2: Input) -> Output:
    """Parses some input arguments"""
    parsed_arg2 = str(arg2)
    a = _get_dep_a(arg1)
    if arg1 is None:
        arg1 = 5
    if not parsed_arg2:
        parsed_arg2 = "None"
    b: int = arg1 * 2
    if len(parsed_arg2) > 5:
        return None
    try:
        c = arg1 / b
        b_plus_c = str(b + c)
        c = str(c)
    except ZeroDivisionError:
        return None
    if a is None:
        return None
    return a + b_plus_c + parsed_arg2


def after(arg1: Input, arg2: Input) -> Output:
    """Parses some input arguments"""
    a = _get_dep_a(arg1)
    if a is None:
        return None

    if arg1 is None:
        arg1 = 5
    b: int = arg1 * 2
    try:
        c = arg1 / b
    except ZeroDivisionError:
        return None
    b_plus_c = str(b + c)
    c = str(c)

    parsed_arg2 = str(arg2)
    if not parsed_arg2:
        parsed_arg2 = "None"
    if len(parsed_arg2) > 5:
        return None

    return a + b_plus_c + parsed_arg2


def _get_dep_a(arg1: Input = None) -> str | None:
    if arg1 is None:
        return "default"
    return "special" if arg1 > 1 else None


if __name__ == "__main__":
    run()
