"""Part 1, Chapter 03 - Normalise Symmetries"""

import typing as t

import hypothesis
import hypothesis.strategies as st

Input = str | None
Output = str


@hypothesis.given(st.text(min_size=1) | st.none())
def run(raw: Input) -> None:
    assert before(raw) == after(raw)


def before(maybe_foo: Input) -> Output:
    """Variants of optionally initialising `foo` from accross the codebase"""

    def variant_1(maybe_foo: Input) -> Output:
        if maybe_foo is None:
            return "bar"
        return maybe_foo

    def variant_2(maybe_foo: Input) -> Output:
        if maybe_foo is not None:
            return maybe_foo
        return "bar"

    def variant_3(maybe_foo: Input) -> Output:
        if maybe_foo is not None:
            foo = maybe_foo
        else:
            foo = "bar"
        return foo

    variant_4 = lambda mf: mf if mf else "bar"  # noqa

    def variant_5(maybe_foo: Input) -> Output:
        return maybe_foo or "bar"

    def variant_6(maybe_foo: Input) -> Output:
        if (foo := maybe_foo) is None:
            foo = "bar"
        return foo

    return _one_unique(
        v(maybe_foo) for v in (variant_1, variant_2, variant_3, variant_4, variant_5, variant_6)
    )


def after(maybe_foo: Input) -> Output:
    """Variants of optionally initialising `foo` from accross the codebase"""

    def variant_1(maybe_foo: Input) -> Output:
        if maybe_foo is None:
            return "bar"
        return maybe_foo

    def variant_2(maybe_foo: Input) -> Output:
        if maybe_foo is None:
            return "bar"
        return maybe_foo

    def variant_3(maybe_foo: Input) -> Output:
        if maybe_foo is None:
            return "bar"
        return maybe_foo

    variant_4 = lambda mf: "bar" if mf is None else mf  # noqa

    def variant_5(maybe_foo: Input) -> Output:
        return "bar" if maybe_foo is None else maybe_foo

    def variant_6(maybe_foo: Input) -> Output:
        if maybe_foo is None:
            return "bar"
        return maybe_foo

    return _one_unique(
        v(maybe_foo) for v in (variant_1, variant_2, variant_3, variant_4, variant_5, variant_6)
    )


def _one_unique[T](elements: t.Iterable[T]) -> T:
    unique_elements = set(elements)
    if len(unique_elements) != 1:
        raise ValueError(f"A single unique element can't be found in {list(elements)}")
    return next(iter(unique_elements))

if __name__ == "__main__":
    run()
