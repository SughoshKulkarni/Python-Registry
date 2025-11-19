"""CSV exporter plugin.

This module provides CSV export functionality using the registry pattern.
The export_csv function is automatically registered when this module is imported.
"""

from utils.registry import Data, register_exporter


@register_exporter("csv")
def export_csv(data: Data) -> None:
    """Export data in CSV format.

    Args:
        data: Dictionary containing the data to export.
    """
    print(f"Exporting data to CSV: {data}")
