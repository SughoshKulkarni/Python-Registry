"""JSON exporter plugin.

This module provides JSON export functionality using the registry pattern.
The export_json function is automatically registered when this module is imported.
"""

import json

from utils.registry import Data, register_exporter


@register_exporter("json")
def export_json(data: Data) -> None:
    """Export data in JSON format.
    
    Args:
        data: Dictionary containing the data to export.
    """
    print("Exporting data to JSON:")
    print(json.dumps(data, indent=2))
