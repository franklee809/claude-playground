import csv
from pathlib import Path


def load_members(filepath: str | Path) -> list[dict[str, str]]:
    """Read members from a CSV file and return them as a list of dicts.

    The CSV must have at minimum ``first_name`` and ``last_name`` columns.
    Any additional columns are included in the returned dicts.

    Args:
        filepath: Path to the CSV file.

    Returns:
        List of dicts, one per row, keyed by column header.

    Raises:
        FileNotFoundError: If the CSV file does not exist.
        KeyError: If ``first_name`` or ``last_name`` columns are missing.
    """
    path = Path(filepath)
    if not path.exists():
        raise FileNotFoundError(f"CSV file not found: {path}")

    with path.open(newline="") as f:
        rows = list(csv.DictReader(f))

    if rows and not {"first_name", "last_name"}.issubset(rows[0].keys()):
        raise KeyError("CSV must contain 'first_name' and 'last_name' columns")

    return rows


def display_members(filepath: str | Path) -> None:
    """Print the full name of each member in the CSV file.

    Args:
        filepath: Path to the CSV file.
    """
    for member in load_members(filepath):
        print(member["first_name"], member["last_name"])
