"""Part 1, Chapter 01 - Guard Clauses"""

import hypothesis
import hypothesis.strategies as st

Input = str | int | float | None
Output = str | None


@hypothesis.given(st.text() | st.integers() | st.floats() | st.none())
def run(raw: Input) -> None:
    assert before(raw) == after(raw)


def before(raw: Input) -> Output:
    """Parses some raw data"""
    if raw is not None:
        if isinstance(raw, (int, float)):
            parsed = str(raw)
        else:
            parsed = raw.strip()
    else:
        parsed = None
    return parsed


def after(raw: Input) -> Output:
    """Parses some raw data"""
    if raw is None:
        return None
    if isinstance(raw, (int, float)):
        return str(raw)
    return raw.strip()


if __name__ == "__main__":
    run()
