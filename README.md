# Python FastAPI Base

Minimal template for starting a Python REST API with FastAPI. It includes a small in-memory CRUD example, Pydantic models, pytest tests, Ruff checks, dependency updates with Dependabot, and GitHub Actions CI.

## Requirements

- Python 3.10+
- pip
- FastAPI
- Pydantic

The development toolchain uses pytest for tests and Ruff for linting and formatting checks.

## Use this template

Create a repository from this GitHub template, clone it, and create a virtual environment:

```sh
python -m venv .venv
source .venv/bin/activate
```

On Windows PowerShell, activate it with:

```powershell
.venv\Scripts\Activate.ps1
```

Install the pinned runtime dependencies:

```sh
pip install -r requirements.txt
```

Run the development server:

```sh
fastapi dev main.py
```

The API is available at `http://127.0.0.1:8000` and the interactive documentation at `http://127.0.0.1:8000/docs`.

## Development checks

Install the development dependencies and run the same checks used by CI:

```sh
pip install -r requirements-dev.txt
ruff check .
ruff format --check .
python -m pytest -q
python -m compileall -q main.py models services
```
