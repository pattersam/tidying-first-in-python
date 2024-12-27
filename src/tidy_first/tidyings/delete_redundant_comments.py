"""Part 1, Chapter 15 - Delete Redundant Comments"""

import dataclasses

import hypothesis
import hypothesis.strategies as st

Input = str | tuple | dict | None


@dataclasses.dataclass
class Output:
    field1: str
    field2: str


@hypothesis.given(
    st.text()
    | st.tuples()
    | st.dictionaries(keys=st.text(), values=st.text())
    | st.none()
)
def run(data: Input) -> None:
    assert before(data) == after(data)


def before(data: Input) -> Output | None:
    """Parses some raw data ... shout out to ChatGPT for the redundant comments ;)"""
    if data is None:
        # Return `None` if data is `None`
        return None
    if isinstance(data, str):
        # If input is a string, split it into two parts
        parts = data.split(",")
        if len(parts) > 2:
            # Return `None` if there are not exactly 2 parts
            return None
        # otherwise and unpack into the two fields
        field1 = (
            parts[0].strip() if len(parts) > 0 else "default"
        )  # set to `"default"` when not given
        field2 = (
            parts[1].strip() if len(parts) > 1 else "default"
        )  # set to `"default"` when not given
    elif isinstance(data, tuple):
        # If input is a tuple, check if it has two parts
        if len(data) > 2:
            # return None if there are more than 2 parts
            return None
        # otherwise unpack it into the two fields
        field1 = (
            data[0] if len(data) > 0 else "default"
        )  # set to `"default"` when not given
        field2 = (
            data[1] if len(data) > 1 else "default"
        )  # set to `"default"` when not given
    elif isinstance(data, dict):
        # If input is a dictionary, extract values by keys
        field1 = data.get("field1", "default")  # set to `"default"` when not given
        field2 = data.get("field2", "default")  # set to `"default"` when not given
    else:
        # return `None` when any other type is given
        return None

    return Output(field1=field1, field2=field2)


def after(data: Input) -> Output | None:
    """Parses some raw data"""
    if data is None:
        return None
    if isinstance(data, str):
        parts = data.split(",")
        if len(parts) > 2:
            return None
        field1 = parts[0].strip() if len(parts) > 0 else "default"
        field2 = parts[1].strip() if len(parts) > 1 else "default"
    elif isinstance(data, tuple):
        if len(data) > 2:
            return None
        field1 = data[0] if len(data) > 0 else "default"
        field2 = data[1] if len(data) > 1 else "default"
    elif isinstance(data, dict):
        field1 = data.get("field1", "default")
        field2 = data.get("field2", "default")
    else:
        return None

    return Output(field1=field1, field2=field2)


if __name__ == "__main__":
    run()
