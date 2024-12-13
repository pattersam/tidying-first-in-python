"""Part 1, Chapter 04 - New Interface, Old Implementation"""

import typing as t

import hypothesis
import hypothesis.strategies as st

Input = list[str | int | None]
Output = set[str | int]

NewInterface = t.Callable[[Input], Output]


@hypothesis.given(st.lists(st.text() | st.integers() | st.none()))
def run(values: Input) -> None:
    assert before(values) == after(values)


def before(values: Input) -> Output:
    """Find the difference between two transformations"""

    return set(
        old_implementation(
            values,
            filter_negatives=True,
            convert_to_upper=False,
            double_numbers=False,
            ignore_strings=False,
        )
    ).symmetric_difference(
        set(
            old_implementation(
                values,
                filter_negatives=False,
                convert_to_upper=False,
                double_numbers=False,
                ignore_strings=False,
            )
        )
    )


def after(values: Input) -> Output:
    """Find the difference between two transformations"""

    return set(new_interface(values, filter_negatives=True)).symmetric_difference(
        set(new_interface(values))
    )


def new_interface(values: Input, filter_negatives: bool = False) -> list[str | int]:
    return old_implementation(
        values,
        filter_negatives=filter_negatives,
        convert_to_upper=False,
        double_numbers=False,
        ignore_strings=False,
    )


def old_implementation(
    values: Input,
    filter_negatives: bool,
    convert_to_upper: bool,
    double_numbers: bool,
    ignore_strings: bool,
) -> list[str | int]:
    """Transforms a list with a number of options"""
    result: list[str | int] = []

    for value in values:
        if value is None:
            continue
        if isinstance(value, int):
            if filter_negatives and value < 0:
                continue
            if double_numbers:
                result.append(value * 2)
            else:
                result.append(value)
        elif isinstance(value, str):
            if ignore_strings:
                continue
            if convert_to_upper:
                result.append(value.upper())

    return result


if __name__ == "__main__":
    run()
