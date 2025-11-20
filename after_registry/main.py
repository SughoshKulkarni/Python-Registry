"""Main module demonstrating the registry pattern with dynamic plugin loading.

This example shows how to use the registry pattern with automatic plugin discovery.
All exporter plugins are dynamically loaded from the plugins directory, and their
decorated functions are automatically registered in the exporters registry.
"""

from utils.plugin_loader import load_plugins
from utils.registry import Data, exporters


def export_data(data: Data, format: str) -> None:
    """Export data using the specified format.

    Looks up the appropriate exporter function from the registry and calls it
    with the provided data.

    Args:
        data: Dictionary containing the data to export.
        format: String identifier for the export format (e.g., "pdf", "csv", "json").

    Raises:
        ValueError: If no exporter is registered for the specified format.
    """
    exporter = exporters.get(format)
    if exporter is None:
        raise ValueError(f"No exporter found for format: {format}")
    exporter(data)


def main() -> None:
    """Main entry point demonstrating the registry pattern with plugins."""
    load_plugins()  # Ensure all plugins are loaded

    # Example usage
    sample_data = {"name": "Alice", "age": 30}

    # These will work because the exporters are registered via plugins
    export_data(sample_data, "pdf")
    export_data(sample_data, "csv")
    export_data(sample_data, "json")

    # This would raise an error because "xlsx" exporter is not registered
    try:
        export_data(sample_data, "xlsx")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
