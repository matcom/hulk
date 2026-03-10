---
name: tesserax
description: Specialized in generating charts, diagrams, and technical visualizations using the tesserax Python library. Use when the user asks to "draw", "visualize", "chart", or "diagram" something, especially for architectural, hierarchical, or statistical data.
---

# Tesserax Visualization Guide

Tesserax is a declarative Python library for creating SVG-based diagrams and charts. Use it for generating high-quality, programmatic visualizations.

## Core Workflow

1.  **Initialize Canvas:** Always use the `Canvas` context manager.
2.  **Define Shapes/Data:** Use geometric primitives (`Square`, `Circle`, `Text`) or `Chart` for data.
3.  **Layout semantic elements:** Use `RowLayout`, `ColumnLayout`, `GridLayout`, `Tree`, or `Force-Directed` layouts.
4.  **Connect with Anchors:** Use semantic anchors (`top`, `bottom`, `left`, `right`, `center`) for connections.
5.  **Export/Display:** Use `.fit().display()` to finalize.

## Code Patterns

### Basic Diagram
```python
from tesserax import Canvas, Square, Text, RowLayout, Polyline

with Canvas() as canvas:
    a = Square(size=2) + Text("A")
    b = Square(size=2) + Text("B")
    layout = RowLayout(children=[a, b], gap=2)
    p = Polyline(points=[a.anchor("right"), b.anchor("left")])

canvas.fit().display()
```

### Statistical Chart
```python
from tesserax import Canvas, Chart

data = [{"x": 1, "y": 10}, {"x": 2, "y": 20}]
with Canvas() as canvas:
    chart = Chart(data).mark_bar().encode(x="x", y="y")

canvas.fit().display()
```

## Strategy for "Drawing" Requests
When the user asks to "draw" something:
1.  Analyze the data or structure to be visualized.
2.  Write a Python script using `tesserax`.
3.  **Quarto Integration:** If working inside a `.qmd` file (the primary format for this project), use a standard `{python}` code block.
    - End the block with `canvas.fit().display()`.
    - Quarto will automatically capture the SVG output and render it in the document.
    - No manual file saving or export commands are needed.
4.  **Standalone Execution:** For non-Quarto contexts, execute the script and capture the SVG output to a file (e.g., `diagram.svg`).
5.  **Environment Check:** Ensure `uv add tesserax` is run if the library is not available in the current environment.
