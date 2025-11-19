from functools import wraps
from typing import Any, Callable


type Data = dict[str, Any]  # Data is a dictionary with string keys and any type values
type ExportFn = Callable[[Data], None]  # Function that takes Data and returns None

# The registry: maps format name to export function
EXPORTERS: dict[str, ExportFn] = {}


def register_exporter(name: str):
    def decorator(func: ExportFn):
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            return func(*args, **kwargs)

        EXPORTERS[name] = wrapper
        return wrapper

    return decorator
