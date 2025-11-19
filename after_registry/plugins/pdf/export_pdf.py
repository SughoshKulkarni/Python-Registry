"""PDF exporter plugin.

This module provides PDF export functionality using the registry pattern.
The export_pdf function is automatically registered when this module is imported.
"""

from utils.registry import Data, register_exporter


@register_exporter("pdf")
def export_pdf(data: Data) -> None:
    """Export data in PDF format.
    
    Args:
        data: Dictionary containing the data to export.
    """
    print(f"Exporting data to PDF: {data}")
