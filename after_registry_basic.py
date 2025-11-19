"""Basic example of the registry pattern with decorator-based registration.

This module demonstrates the registry pattern using a decorator to allow functions
to self-register. This eliminates the need for manual if/elif chains and makes it
easy to add new export formats without modifying the core export_data function.

Key improvements over the if/else approach:
- Functions self-register using decorators
- No need to modify export_data when adding new formats
- Follows the Open/Closed Principle (open for extension, closed for modification)
- More maintainable and scalable

This is a basic example where all exporters are defined in a single file.
See after_registry/main.py for a more advanced example with plugin loading.
"""

import json
from collections.abc import Callable
from functools import wraps
from typing import Any

type Data = dict[str, Any]
type ExportFn = Callable[[Data], None]

# The registry: maps format name to export function
exporters: dict[str, ExportFn] = {}


def register_exporter(name: str):
    """Decorator to register an exporter function in the registry.

    Args:
        name: The format name/key under which to register the exporter function.

    Returns:
        A decorator function that registers the exporter.
    """

    def decorator(func: ExportFn):
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            return func(*args, **kwargs)

        exporters[name] = wrapper
        return wrapper

    return decorator


@register_exporter("pdf")
def export_pdf(data: Data) -> None:
    """Export data in PDF format (placeholder implementation).

    This function is automatically registered under the "pdf" key.

    Args:
        data: Dictionary containing the data to export.
    """
    print(f"Exporting data to PDF: {data}")


@register_exporter("csv")
def export_csv(data: Data) -> None:
    """Export data in CSV format (placeholder implementation).

    This function is automatically registered under the "csv" key.

    Args:
        data: Dictionary containing the data to export.
    """
    print(f"Exporting data to CSV: {data}")


@register_exporter("json")
def export_json(data: Data) -> None:
    """Export data in JSON format.

    This function is automatically registered under the "json" key.

    Args:
        data: Dictionary containing the data to export.
    """
    print("Exporting data to JSON:")
    print(json.dumps(data, indent=2))


def export_data(data: Data, format: str) -> None:
    """Export data using the specified format from the registry.

    Looks up the exporter function in the registry and calls it.
    No modification needed when new exporters are added!

    Args:
        data: Dictionary containing the data to export.
        format: String identifier for the export format.

    Raises:
        ValueError: If no exporter is registered for the specified format.
    """
    exporter = exporters.get(format)
    if exporter is None:
        raise ValueError(f"❌ No exporter found for format: {format}")
    exporter(data)


def main() -> None:
    """Demonstrate the registry pattern with self-registering functions."""
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
