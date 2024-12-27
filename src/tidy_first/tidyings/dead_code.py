"""Part 1, Chapter 02 - Dead Code"""

import hypothesis
import hypothesis.strategies as st

Input = list[int]
Output = float | None


@hypothesis.given(st.lists(st.integers()))
def run(scores: Input) -> None:
    assert before(scores) == after(scores)


def before(scores: Input) -> Output:
    """Calculate the average of integer scores"""
    if not scores:
        return None

    cleaned_scores = [score for score in scores if score >= 0]

    if not cleaned_scores:
        return None

    total = sum(cleaned_scores)
    count = len(cleaned_scores)
    average = total / count

    if average < 0:
        raise ValueError("Unexpected negative average")

    return average


def after(scores: Input) -> Output:
    """Calculate the average of integer scores"""
    cleaned_scores = [score for score in scores if score >= 0]

    if not cleaned_scores:
        return None

    total = sum(cleaned_scores)
    count = len(cleaned_scores)
    average = total / count

    return average


if __name__ == "__main__":
    run()
