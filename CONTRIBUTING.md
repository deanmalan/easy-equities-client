# Contributing

## Installation

System dependencies:
- Python 3.13+
- [uv](https://docs.astral.sh/uv/)

1. Install Python 3.13: `uv python install 3.13`.
2. `uv sync` to install packages.

## Tests

Running the tests:

```
uv run pytest
```

Running the tests with code coverage:

```
uv run pytest --cov=easy_equities_client tests/
```

## Linting

With pre-commit:

- Install [pre-commit](pre-commit.com/).
- Run `pre-commit install`.
- Stage files.
- When you create a commit, pre-commit will automatically lint and check your staged files.
- Stage the files that were modified again.
- Repeat until no more pre-commit errors are raised.

Manually:

```
uv run ruff format
```

## Type-checking

We use [MyPy](https://mypy.readthedocs.io/en/latest/index.html) for static type-checking. You can run it with:

```
uv run mypy src tests
```

## Releasing a new version

1. Update [CHANGELOG.md](./CHANGELOG.md) following the [Keep a changelog](https://keepachangelog.com/en/1.0.0/) format.

2. Bump the version number (following [semantic versioning](https://semver.org/)).
