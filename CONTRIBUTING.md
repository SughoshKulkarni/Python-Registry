# Contributing to Python Registry Pattern

Thank you for your interest in contributing to the Python Registry Pattern project! This document provides guidelines and instructions for contributing.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Project Structure](#project-structure)
- [Making Changes](#making-changes)
- [Code Style Guidelines](#code-style-guidelines)
- [Adding New Features](#adding-new-features)
- [Submitting Changes](#submitting-changes)

## Code of Conduct

Please be respectful and constructive in all interactions with the project and its community.

## Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/Python-Registry.git
   cd Python-Registry
   ```
3. **Add the upstream repository** as a remote:
   ```bash
   git remote add upstream https://github.com/SughoshKulkarni/Python-Registry.git
   ```

## Development Setup

### Prerequisites

- Python 3.13 or higher
- [uv](https://github.com/astral-sh/uv) (recommended) or pip

### Installation

Using uv (recommended):
```bash
uv sync
```

Using pip:
```bash
pip install -e .
```

### Running Examples

Test your setup by running the examples:

```bash
# Before pattern (anti-pattern)
python before_registry.py

# After pattern (basic)
python after_registry_basic.py

# After pattern (advanced with plugins)
python after_registry/main.py
```

### Code Quality Tools

This project uses [Ruff](https://docs.astral.sh/ruff/) for linting and formatting:

```bash
# Install ruff (if not already installed)
pip install ruff

# Check for linting issues
ruff check .

# Auto-fix linting issues
ruff check . --fix

# Format code
ruff format .
```

Run these commands before committing to ensure code quality.

## Project Structure

```
Python-Registry/
├── before_registry.py              # Anti-pattern example
├── after_registry_basic.py         # Basic registry pattern
├── after_registry/                 # Advanced plugin architecture
│   ├── main.py                    # Main entry point
│   ├── utils/                     # Core utilities
│   │   ├── registry.py           # Registry implementation
│   │   └── plugin_loader.py      # Plugin discovery
│   └── plugins/                   # Exporter plugins
│       ├── csv/
│       ├── json/
│       └── pdf/
```

## Making Changes

### Creating a Branch

Always create a new branch for your changes:

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

### Branch Naming Conventions

- `feature/` - for new features
- `fix/` - for bug fixes
- `docs/` - for documentation changes
- `refactor/` - for code refactoring

## Code Style Guidelines

### Python Style

This project follows PEP 8 style guidelines. Key points:

- Use 4 spaces for indentation (no tabs)
- Maximum line length: 88 characters (ruff formatter standard)
- Use type hints for function signatures
- Write docstrings for all modules, classes, and functions

### Docstring Format

Use Google-style docstrings:

```python
def function_name(arg1: str, arg2: int) -> bool:
    """Brief description of the function.
    
    More detailed description if needed.
    
    Args:
        arg1: Description of arg1.
        arg2: Description of arg2.
        
    Returns:
        Description of return value.
        
    Raises:
        ValueError: Description of when this is raised.
    """
    pass
```

### Type Hints

Always use type hints:

```python
from typing import Any, Callable

type Data = dict[str, Any]
type ExportFn = Callable[[Data], None]

def export_data(data: Data, format: str) -> None:
    """Export data in the specified format."""
    pass
```

## Adding New Features

### Adding a New Exporter Plugin

To add a new exporter format:

1. Create a new directory under `after_registry/plugins/` named `your_format`

2. Create an empty `__init__.py` file in `after_registry/plugins/your_format/`

3. Add a docstring to `__init__.py`:
   ```python
   """Your format plugin package for exporting data."""
   ```

3. Create the exporter module:
   ```python
   # after_registry/plugins/your_format/export_your_format.py
   """Your format exporter plugin.
   
   This module provides export functionality for your_format using the registry pattern.
   """
   
   from utils.registry import Data, register_exporter
   
   
   @register_exporter("your_format")
   def export_your_format(data: Data) -> None:
       """Export data in your_format format.
       
       Args:
           data: Dictionary containing the data to export.
       """
       print(f"Exporting data to your_format: {data}")
   ```

4. Test your plugin:
   ```python
   python after_registry/main.py
   ```

### Adding Documentation

- Update README.md for significant changes
- Add docstrings to all new code
- Include usage examples where appropriate

## Submitting Changes

### Before Submitting

1. **Test your changes**: Run all examples to ensure they work
2. **Lint and format code**: Run `ruff check . --fix && ruff format .`
3. **Check code style**: Ensure your code follows the style guidelines
4. **Update documentation**: Update README.md if needed
5. **Commit your changes**:
   ```bash
   git add .
   git commit -m "Brief description of changes"
   ```

### Commit Message Guidelines

Write clear, concise commit messages:

- Use the imperative mood ("Add feature" not "Added feature")
- First line should be 50 characters or less
- Add a blank line followed by a more detailed explanation if needed

Example:
```
Add XML exporter plugin

Implements XML export functionality using the registry pattern.
The exporter is automatically discovered via the plugin loader.
```

### Creating a Pull Request

1. **Push your changes** to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

2. **Open a Pull Request** on GitHub:
   - Go to the original repository
   - Click "New Pull Request"
   - Select your fork and branch
   - Fill in the PR template with details about your changes

3. **Respond to feedback**: Address any comments or requested changes
