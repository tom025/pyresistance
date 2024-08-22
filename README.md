 # PyResistance #

A FastAPI application following this [blog post](https://blog.jonrshar.pe/2024/Aug/17/python-tdd-ohm.html) from @textbook.

## Package management ##

This project uses [uv](https://docs.astral.sh/uv/) as a package manager. To install follow the [instructions](https://docs.astral.sh/uv/getting-started/installation/).

To synchronize dependencies run

```shell
uv sync
```

This will create an isolated virtual environment under `.venv` and install all the required production and dev packages.

## Development ##

To ensure commands/scripts run in the virtual environment, either activate it

```shell
source .venv/bin/activate
```

or prefix the command/script with `uv run`. For example

```shell
uv run pytest
```

### Install git hooks ###

Git hook integration is done using [pre-commit](https://pre-commit.com).

```shell
pre-commit install
```

will install git hooks to `.git/hooks`.

### Run tests ###

```shell
pytest
```

will run all tests.

### Format code ###

```shell
ruff format
```

will fix any code formatting issues

### Lint code ###

```shell
ruff lint
```