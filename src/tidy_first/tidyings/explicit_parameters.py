"""Part 1, Chapter 10 - Explicit Parameters"""

import os
import typing as t

import hypothesis
import hypothesis.strategies as st

Input = tuple[int, int, int]
Output = t.Callable[[int, int, int], bool]
os.environ["HIDDEN_PARAMETER"] = "abc,ijk,xyz"


@hypothesis.given(st.tuples(st.integers(), st.integers(), st.integers()))
def run(args: Input) -> None:
    assert before()(*args) == after()(*args)


def before() -> Output:
    """A module with functions that have implicit parameters."""

    def func_1(params: dict) -> int:
        return params["a"] + params["b"]

    def func_2(params: dict) -> int:
        return params["c"] + _sub_func_1(params)

    def func_3(params: dict) -> int:
        return params["a"] + _sub_func_2(params)

    def _sub_func_1(params: dict) -> int:
        return params["a"] + 1

    def _sub_func_2(params: dict) -> int:
        special_keys = os.getenv("HIDDEN_PARAMETER", "")
        for key in params.keys():
            if key in special_keys.split(","):
                return 1
        return params.get("a", 1)

    def module_entry_point(a, b, c) -> bool:
        params = {"a": a, "b": b, "c": c}
        return (func_1(params) + func_2(params) + func_3(params)) > 10

    return module_entry_point


def after() -> Output:
    """A refactored module functions that have explicit parameters."""

    def func_1(a: int, b: int) -> int:
        return a + b

    def func_2(a: int, c: int) -> int:
        return c + _sub_func_1(a)

    def func_3(a: int, known_params: list[str], special_keys: str) -> int:
        return a + _sub_func_2(known_params, special_keys, a)

    def _sub_func_1(a: int) -> int:
        return a + 1

    def _sub_func_2(known_params: list[str], special_keys: str, a: int | None) -> int:
        if a is None:
            return 1
        for key in known_params:
            if key in special_keys.split(","):
                return 1
        return a

    def module_entry_point(a, b, c) -> bool:
        special_keys = os.getenv("HIDDEN_PARAMETER", "")
        return (
            func_1(a, b) + func_2(a=a, c=c) + func_3(a, ["a", "b", "c"], special_keys)
        ) > 10

    return module_entry_point


if __name__ == "__main__":
    run()
