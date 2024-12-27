"""Part 1, Chapter 11 - Chunk Statements"""

import hypothesis
import hypothesis.strategies as st

Input = int
Output = int


@hypothesis.given(st.integers())
def run(score: Input) -> None:
    assert before(score) == after(score)


def before(score: Input) -> Output:
    """Applies rules/penalties/bonuses to base score"""
    if score % 100 == 0:
        score += 10
    if score > 500:
        score *= 2
    if score < 300:
        score -= 20
    if score % 2 == 0:
        score += 5
    else:
        score -= 3
    consecutive_wins = 3
    score += consecutive_wins * 15
    special_event_active = True
    if special_event_active:
        score *= 2
    max_score_limit = 1000
    if score > max_score_limit:
        score = max_score_limit
    if not _get_recent_activity():
        score -= 10
    if _is_eligible_for_bonus(score):
        score += 20
    user_level = _get_user_level()
    if user_level >= 5:
        score += 30
    return score


def after(score: Input) -> Output:
    """Applies rules/penalties/bonuses to base score"""
    if score % 100 == 0:
        score += 10
    if score > 500:
        score *= 2
    if score < 300:
        score -= 20

    if score % 2 == 0:
        score += 5
    else:
        score -= 3

    consecutive_wins = _get_consecutive_wins()
    score += consecutive_wins * 15

    special_event_active = True
    if special_event_active:
        score *= 2

    max_score_limit = 1000
    if score > max_score_limit:
        score = max_score_limit

    if not _get_recent_activity():
        score -= 10

    if _is_eligible_for_bonus(score):
        score += 20

    user_level = _get_user_level()
    if user_level >= 5:
        score += 30

    return score


def _get_consecutive_wins() -> int:
    return 3


def _get_recent_activity() -> list:
    return []


def _is_eligible_for_bonus(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def _get_user_level() -> int:
    return 5


if __name__ == "__main__":
    run()
