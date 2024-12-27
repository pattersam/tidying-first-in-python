"""Part 1, Chapter 12 - Extract Helper"""

import logging

import hypothesis
import hypothesis.strategies as st

Input = str | None
Output = str


@hypothesis.given(st.text() | st.none())
def run(raw: Input) -> None:
    assert before(raw) == after(raw)


def before(raw: Input) -> Output:
    """Validate some raw data"""
    if raw is None or raw == "None":
        raw = "default value"
    result = raw
    if any(bad_word in result for bad_word in ["bad", "words"]):
        logging.debug("bad word detected in %s", result)
        result = f"[EXPLICIT CONTENT WARNING] {result}"
    result = result.replace("\n", " ")
    result = result.strip()
    num_words = len(result.split(" "))
    result = f'{{"content_length": {len(result)}, "num_words": {num_words}}} {result}'
    return result


def after(raw: Input) -> Output:
    """Validate some raw data"""
    result = _coerce_input(raw)
    result = _tag_bad_words(result)
    result = _remove_whitespace(result)
    result = _add_metadata(result)
    return result


def _coerce_input(value: str | None) -> str:
    if value is None or value == "None":
        value = "default value"
    return value


def _tag_bad_words(value: str) -> str:
    if any(bad_word in value for bad_word in ["bad", "words"]):
        logging.debug("bad word detected in %s", value)
        return f"[EXPLICIT CONTENT WARNING] {value}"
    return value


def _remove_whitespace(value: str) -> str:
    return value.replace("\n", " ").strip()


def _add_metadata(value: str) -> str:
    return f'{{"content_length": {len(value)}, "num_words": { len(value.split(" "))}}} {value}'


if __name__ == "__main__":
    run()
