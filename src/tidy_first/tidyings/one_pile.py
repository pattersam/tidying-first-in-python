"""Part 1, Chapter 13 - One Pile"""

import typing as t

import hypothesis
import hypothesis.strategies as st

Input = list[int]
Output = t.Callable[[Input], Input]


@hypothesis.given(st.lists(st.integers()))
def run(numbers: Input) -> None:
    assert before()(numbers) == after()(numbers)


def before() -> Output:
    """A module that's been broken down into small pieces which are hard to understand."""

    def module_entry_point(numbers: Input) -> Input:
        numbers = transformation_1(numbers)
        numbers = transformation_2(numbers)
        numbers = transformation_3(numbers)
        numbers = transformation_4(numbers)
        numbers = transformation_5(numbers, transformation_1)
        numbers = apply_nested_transformations(numbers)
        return numbers

    def transformation_1(numbers) -> Input:
        return [x * 2 for x in numbers]

    def transformation_2(numbers) -> Input:
        return [x**2 for x in numbers]

    def transformation_3(numbers) -> Input:
        return [x for x in numbers if x % 2 == 0]

    def transformation_4(numbers) -> Input:
        cumulative_sum = 0
        result: list[int] = []
        for value in numbers:
            cumulative_sum += value
            result.append(value)
        return result

    def transformation_5(numbers, transform_func) -> Input:
        transformed_numbers = transform_func(numbers)
        return transformation_4(transformed_numbers)

    def apply_nested_transformations(input: Input) -> Input:
        input = transformation_1(input)
        input = transformation_3(input)
        input = transformation_2(input)
        return input

    return module_entry_point


def after() -> Output:
    """A refactor of the module where everything is inlined, preparing for a potential futher tidying"""

    def module_entry_point(numbers: Input) -> Input:
        numbers = [x * 2 for x in numbers]
        numbers = [x**2 for x in numbers]
        numbers = [x for x in numbers if x % 2 == 0]
        numbers = [x * 2 for x in numbers]
        cumulative_sum = 0
        result: list[int] = []
        for value in numbers:
            cumulative_sum += value
            result.append(value)
        numbers = result
        numbers = [x * 2 for x in numbers]
        numbers = [x for x in numbers if x % 2 == 0]
        numbers = [x**2 for x in numbers]
        return numbers

    return module_entry_point


if __name__ == "__main__":
    run()
