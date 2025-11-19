import importlib
import pkgutil
from pathlib import Path

# NOTE: Ensure __init__.py exists in the utils directory
# Dynamically load all plugins from the plugins directory, including subfolders
def load_plugins():
    plugins_dir = (
        Path(__file__).parent.parent / "plugins"
    )  # Adjusted path to plugins directory
    package_name = "plugins"  # Base package name for plugins

    for module_info in pkgutil.walk_packages([str(plugins_dir)], f"{package_name}."):
        importlib.import_module(module_info.name)
