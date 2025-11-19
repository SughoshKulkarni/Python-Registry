from utils.plugin_loader import load_plugins
from utils.registry import Data, exporters


def export_data(data: Data, format: str) -> None:
    exporter = exporters.get(format)
    if exporter is None:
        raise ValueError(f"No exporter found for format: {format}")
    exporter(data)


if __name__ == "__main__":
    load_plugins()  # Ensure all plugins are loaded

    # Example usage
    sample_data = {"name": "Alice", "age": 30}

    # This will work because the exporters are registered via plugins
    export_data(sample_data, "pdf")
    export_data(sample_data, "csv")
    export_data(sample_data, "json")

    # This would raise an error because "xlsx" exporter is not registered
    export_data(sample_data, "xlsx")
