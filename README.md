# Python Registry Pattern

This repository contains examples demonstrating the Registry Pattern in Python, as featured in the [ArjanCodes video](#arjancodes-video). This design pattern is used to replace complex, hard-coded if/else chains with a flexible, decoupled system that allows for dynamic behavior selection and easy extensibility.

The pattern helps resolve the [Open/Closed principle](#open-closed-principle) of the SOLID principles by allowing new functionality to be added without modifying existing code.

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

1. Clone the repository
2. Install dependencies

    ```python
    uv sync
    ```

### Before registry pattern

```python
python before_registry.py
```

### After registry pattern

To run the basic after registry example:

```python
python after_registry_basic.py
```

The above script is basic only in the sense that all exporters are defined in a single file. To see a more advanced example with dynamic plugin loading, run:

```python
python after_registry/main.py
```

The above script demonstrates loading exporter functions from separate modules in a `plugins` directory.

## Resources

- <a id="arjancodes-video"></a>[YouTube: I Hate Long If-Elif Chains: This Design Pattern Solved It Once and For All](https://youtu.be/g7EGMWvJ1fI?si=5WVwtWvKiH-O90Qg)
- <a id="open-closed-principle"></a>[Python Tutorial: Python Open–closed principle](https://www.pythontutorial.net/python-oop/python-open-closed-principle/)
- [GitHub Repository: ArjanCodes/examples/2025/registry](https://github.com/ArjanCodes/examples/tree/ef76bfa8e2cb1a83651e85ca8cbf192cb504533b/2025/registry)
