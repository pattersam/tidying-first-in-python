"""Part 1, Chapter 09 - Explaining Constants"""

import hypothesis
import hypothesis.strategies as st

Input = tuple[float, float]
Output = float


@hypothesis.given(
    st.tuples(
        st.floats(allow_infinity=False, allow_nan=False),
        st.floats(allow_infinity=False, allow_nan=False),
    )
)
def run(args: Input) -> None:
    assert before(*args) == after(*args)


def before(reading: float, error_correction: float) -> Output:
    """Correct & convert pressure reading."""
    return reading * 6.8947572932 + error_correction + 101.325


def after(reading: float, error_correction: float) -> Output:
    """Correct & convert pressure reading."""
    KPA_PER_PSI = 6.8947572932
    GAUGE_PRESSURE = 101.325
    return reading * KPA_PER_PSI + error_correction + GAUGE_PRESSURE


if __name__ == "__main__":
    run()
