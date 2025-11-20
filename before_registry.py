"""Example demonstrating the problem with if/else chains (anti-pattern).

This module shows the traditional approach of using if/elif/else chains to select
behavior based on input. This approach becomes hard to maintain as more options
are added, violates the Open/Closed Principle, and leads to a "hot mess" of
conditional logic.

This is the "before" example that the registry pattern aims to improve.
"""

import json
from collections.abc import Callable
from typing import Any, TypeAlias

Data: TypeAlias = dict[str, Any]
ExportFn: TypeAlias = Callable[[Data], None]


def export_pdf(data: Data) -> None:
    """Export data in PDF format (placeholder implementation).

    Args:
        data: Dictionary containing the data to export.
    """
    print(f"Exporting data to PDF: {data}")


def export_csv(data: Data) -> None:
    """Export data in CSV format (placeholder implementation).

    Args:
        data: Dictionary containing the data to export.
    """
    print(f"Exporting data to CSV: {data}")


def export_json(data: Data) -> None:
    """Export data in JSON format.

    Args:
        data: Dictionary containing the data to export.
    """
    print("Exporting data to JSON:")
    print(json.dumps(data, indent=2))


def export_data(data: Data, format: str) -> None:
    """Export data using the specified format via if/else chain (anti-pattern).

    This function demonstrates the problem: every time a new export format is added,
    this function must be modified, violating the Open/Closed Principle.

    Args:
        data: Dictionary containing the data to export.
        format: String identifier for the export format.

    Raises:
        ValueError: If the format is not supported.
    """
    if format == "pdf":
        export_pdf(data)
    elif format == "csv":
        export_csv(data)
    elif format == "json":
        export_json(data)
    else:
        raise ValueError(f"No exporter found for format: {format}")


def main() -> None:
    """Demonstrate the if/else chain approach with various formats."""
    sample_data: Data = {"name": "Alice", "age": 30}

    # Try exporting in different formats
    export_data(sample_data, "pdf")
    export_data(sample_data, "csv")
    export_data(sample_data, "json")

    # This would raise an error:
    try:
        export_data(sample_data, "xlsx")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
