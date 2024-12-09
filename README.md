# tidying-first-in-python

Python implementations of the "tidyings" from Kent Beck's
[_Tidy First?_](https://www.oreilly.com/library/view/tidy-first/9781098151232/)

Uses [hypothesis](https://hypothesis.readthedocs.io/en/latest/) to assert
behaviour is unchanged before and after each tidying.

## Installation

Assuming you have git & [uv](https://docs.astral.sh/uv/getting-started/installation/)
installed, run:

```bash
git clone git@github.com:pattersam/tidying-first-in-python.git
cd tidying-first-in-python
uv sync
```

## Usage

Run all of the tidyings with:

```bash
uv run run_tidyings
```

Or run a single tidying with:

```bash
uv run src/tidy_first/tidyings/guard_clauses.py
```

## Contribution

Want to add a tidying?

Add a new module under `scr/tidy_first/tidyings/` and implement a `run`
function, wrapped with hypothesis `@given` decorator and parameter strategies,
that asserts the before & after behaviour is unchanged.

Have a look at other tidyings as a guide for how to do this.
