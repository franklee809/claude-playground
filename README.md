# members-reader

A lightweight Python library to load and display member names from a CSV file.

## Requirements

- Python 3.11+
- No external dependencies

## Installation

Install directly from GitHub:

```bash
pip install git+https://github.com/franklee809/claude-playground.git@freecodecamp
```

Or with `uv`:

```bash
uv add git+https://github.com/franklee809/claude-playground.git@freecodecamp
```

## CSV Format

Your CSV file must have at minimum these two columns (additional columns are allowed):

```csv
first_name,last_name
Alice,Johnson
Bob,Smith
```

## Usage

### Display names to stdout

```python
from members_reader import display_members

display_members("members.csv")
# Alice Johnson
# Bob Smith
```

### Load members as data

```python
from members_reader import load_members

members = load_members("members.csv")
# [{'first_name': 'Alice', 'last_name': 'Johnson'}, ...]

for m in members:
    print(f"Hello, {m['first_name']}!")
```

Any extra columns in the CSV are included in the returned dicts automatically:

```csv
first_name,last_name,email
Alice,Johnson,alice@example.com
```

```python
members = load_members("members.csv")
print(members[0]["email"])  # alice@example.com
```

## API Reference

### `load_members(filepath)`

Reads a CSV file and returns all rows as a list of dicts.

| Parameter  | Type              | Description           |
|------------|-------------------|-----------------------|
| `filepath` | `str` or `Path`   | Path to the CSV file  |

**Returns:** `list[dict[str, str]]`

**Raises:**
- `FileNotFoundError` — if the file does not exist
- `KeyError` — if `first_name` or `last_name` columns are missing

---

### `display_members(filepath)`

Prints `first_name last_name` for every row in the CSV.

| Parameter  | Type              | Description           |
|------------|-------------------|-----------------------|
| `filepath` | `str` or `Path`   | Path to the CSV file  |

**Returns:** `None`

## Local Development

```bash
git clone https://github.com/franklee809/claude-playground.git
cd claude-playground
git checkout freecodecamp
```

Run the demo script directly:

```bash
python3 read_members.py
```

## License

MIT
