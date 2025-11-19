"""Registry module for the exporter pattern.

This module provides the core registry functionality for registering and managing
exporter functions. It uses a decorator pattern to allow functions to self-register.
"""

from functools import wraps
from typing import Any, Callable


type Data = dict[str, Any]  # Data is a dictionary with string keys and any type values
type ExportFn = Callable[[Data], None]  # Function that takes Data and returns None

# The registry: maps format name to export function
exporters: dict[str, ExportFn] = {}


def register_exporter(name: str):
    """Decorator to register an exporter function in the registry.
    
    This decorator allows functions to self-register by simply being decorated
    with @register_exporter("format_name"). The function is then available in
    the exporters dictionary under the specified name.
    
    Args:
        name: The format name/key under which to register the exporter function.
        
    Returns:
        A decorator function that registers the exporter and returns a wrapper.
        
    Example:
        @register_exporter("pdf")
        def export_pdf(data: Data) -> None:
            print(f"Exporting to PDF: {data}")
    """
    def decorator(func: ExportFn):
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            return func(*args, **kwargs)

        exporters[name] = wrapper
        return wrapper

    return decorator
