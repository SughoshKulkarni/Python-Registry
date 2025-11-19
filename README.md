# Python Registry Pattern

This repository contains examples demonstrating the **Registry Pattern** in Python, as featured in the [ArjanCodes video](#arjancodes-video). This design pattern is used to replace complex, hard-coded if/else chains with a flexible, decoupled system that allows for dynamic behavior selection and easy extensibility.

The pattern helps resolve the [Open/Closed Principle](#open-closed-principle) of the SOLID principles by allowing new functionality to be added without modifying existing code.

## Table of Contents

- [The Problem: The "If/Else" Hot Mess](#the-problem-the-ifelse-hot-mess)
- [The Solution: The Registry Pattern](#the-solution-the-registry-pattern)
- [Pros & Cons](#pros--cons)
- [How to Use](#how-to-use)
- [Project Structure](#project-structure)
- [Resources](#resources)

## The Problem: The "If/Else" Hot Mess

When building systems that require selecting behavior based on input (e.g., choosing a file export format), developers often resort to long chains of conditional statements.

Why this fails:

Hard to maintain: Adding a new format requires modifying the core function.

Violation of [Open/Closed principle](#open-closed-principle): You have to modify existing code to add new functionality.

Readability: The function grows indefinitely as options are added.

```python
# The Anti-Pattern
def export_data(data, format):
    if format == "pdf":
        return export_pdf(data)
    elif format == "csv":
        return export_csv(data)
    # ... logic continues endlessly
```

## The Solution: The Registry Pattern

The Registry Pattern decouples the selection of logic from the implementation of logic. It acts as a central directory (usually a Python dictionary) where functions or classes are stored using a unique key.

### Level 1: Basic Dictionary Registry

Instead of conditions, use a dictionary to map keys (strings/enums) to callables.

```python
# The Registry Approach
EXPORTERS = {
    "pdf": export_pdf,
    "csv": export_csv,
}

def export_data(data, format):
    # Look up the function and call it immediately
    exporter = EXPORTERS.get(format)
    if not exporter:
        raise ValueError(f"Unknown format: {format}")
    return exporter(data)
```

### Level 2: Self-Registering with Decorators

To avoid manually updating a central dictionary every time a new function is written, we use Python decorators. The function registers itself simply by being defined.

```python
EXPORTERS = {}

def register_exporter(format_name):
    def decorator(func):
        EXPORTERS[format_name] = func
        return func
    return decorator

@register_exporter("pdf")
def export_pdf(data):
    print("Exporting to PDF...")
```

## Pros & Cons

| **Pros**                          | **Cons**                                      |
| :--- | :--- |
| **Decoupled**: Core logic doesn't change when adding features. | **Hidden Logic**: Registration happens implicitly, which can be confusing to debug. |
| **Scalable**: Easy to manage dozens of options without massive functions. | **Import Order**: Modules must be imported for the registration decorator to run. |
| **Testable**: Registry items are isolated functions. | **Overhead**: May be overkill for very simple scripts. |

## How to Use

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/SughoshKulkarni/Python-Registry.git
   cd Python-Registry
   ```

2. **Install dependencies** (using [uv](https://github.com/astral-sh/uv))
   ```bash
   uv sync
   ```

   Or using pip:
   ```bash
   pip install -r requirements.txt  # If available
   ```

### Running the Examples

#### 1. Before Registry Pattern (Anti-Pattern)

This example demonstrates the problem with if/else chains:

```bash
python before_registry.py
```

**Output:**
```
Exporting data to PDF: {'name': 'Alice', 'age': 30}
Exporting data to CSV: {'name': 'Alice', 'age': 30}
Exporting data to JSON:
{
  "name": "Alice",
  "age": 30
}
❌ No exporter found for format: xlsx
```

#### 2. After Registry Pattern - Basic Example

This example shows the registry pattern with decorator-based self-registration:

```bash
python after_registry_basic.py
```

All exporters are defined in a single file, making it easy to see how the pattern works.

#### 3. After Registry Pattern - Advanced with Plugin Loading

This example demonstrates dynamic plugin loading from separate modules:

```bash
python after_registry/main.py
```

The script automatically discovers and loads exporter functions from the `plugins` directory, demonstrating a production-ready plugin architecture.

## Project Structure

```
Python-Registry/
├── before_registry.py              # Anti-pattern: if/else chain example
├── after_registry_basic.py         # Basic registry pattern in single file
├── after_registry/                 # Advanced example with plugin architecture
│   ├── main.py                    # Main entry point with plugin loading
│   ├── utils/                     # Core registry utilities
│   │   ├── registry.py           # Registry and decorator implementation
│   │   └── plugin_loader.py      # Dynamic plugin discovery
│   └── plugins/                   # Exporter plugins
│       ├── csv/
│       │   └── export_csv.py     # CSV exporter plugin
│       ├── json/
│       │   └── export_json.py    # JSON exporter plugin
│       └── pdf/
│           └── export_pdf.py     # PDF exporter plugin
├── README.md                       # This file
└── pyproject.toml                 # Project configuration
```

## Adding a New Exporter Plugin

To add a new export format (e.g., XML):

1. Create a new directory under `after_registry/plugins/`:
   ```bash
   mkdir after_registry/plugins/xml
   touch after_registry/plugins/xml/__init__.py
   ```

2. Create the exporter module:
   ```python
   # after_registry/plugins/xml/export_xml.py
   """XML exporter plugin."""
   
   from utils.registry import Data, register_exporter
   
   @register_exporter("xml")
   def export_xml(data: Data) -> None:
       """Export data in XML format."""
       print(f"Exporting data to XML: {data}")
   ```

3. That's it! The plugin will be automatically discovered and registered.

## Resources

- <a id="arjancodes-video"></a>[YouTube: I Hate Long If-Elif Chains: This Design Pattern Solved It Once and For All](https://youtu.be/g7EGMWvJ1fI?si=5WVwtWvKiH-O90Qg)
- <a id="open-closed-principle"></a>[Python Tutorial: Python Open–closed principle](https://www.pythontutorial.net/python-oop/python-open-closed-principle/)
- [GitHub Repository: ArjanCodes/examples/2025/registry](https://github.com/ArjanCodes/examples/tree/ef76bfa8e2cb1a83651e85ca8cbf192cb504533b/2025/registry)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

See [CONTRIBUTING.md](CONTRIBUTING.md) for more details.
