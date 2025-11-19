"""Plugin loader module for dynamic discovery and loading of exporters.

This module provides functionality to automatically discover and import all plugin
modules from the plugins directory. This ensures that all exporter functions
decorated with @register_exporter are registered when load_plugins() is called.
"""

import importlib
import pkgutil
from pathlib import Path


def load_plugins() -> None:
    """Dynamically load all plugins from the plugins directory.

    This function walks through the plugins directory and imports all Python modules
    it finds. This triggers the decorator registration for any functions decorated
    with @register_exporter, making them available in the exporters registry.

    The function uses pkgutil.walk_packages to recursively discover all modules
    in the plugins directory and its subdirectories.

    Note:
        Ensure __init__.py exists in the utils directory for proper module imports.
    """
    plugins_dir = (
        Path(__file__).parent.parent / "plugins"
    )  # Path to plugins directory relative to this file
    package_name = "plugins"  # Base package name for plugins

    # Walk through all modules in the plugins directory and import them
    for module_info in pkgutil.walk_packages([str(plugins_dir)], f"{package_name}."):
        importlib.import_module(module_info.name)
