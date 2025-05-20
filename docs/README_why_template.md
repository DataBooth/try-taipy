# Taipy Dashboard Template Approach

## Why Use External Template Files for Taipy Dashboards?

This project adopts the **template approach** for defining Taipy dashboard pages. Instead of embedding the dashboard UI as a Python string in your code, the template is stored in a separate Markdown (`.md`) file and loaded at runtime.

---

## Rationale & Benefits

### 1. **Separation of Concerns**

- **Cleaner code:** Business logic (Python) and UI layout (Markdown/Template) are kept separate, making both easier to read and maintain.
- **Easier collaboration:** Developers can focus on Python logic, while designers or data analysts can edit the dashboard layout without touching the code.

### 2. **Maintainability**

- **Simpler updates:** UI changes can be made directly in the template file without modifying Python scripts.
- **Scalability:** As dashboards grow, managing them in external files prevents your Python code from becoming cluttered.

### 3. **Reusability**

- **Template sharing:** Common layouts can be reused across multiple apps or pages by simply loading different template files.
- **Version control:** Templates can be tracked and reviewed independently in version control systems (e.g., Git).

### 4. **Flexibility**

- **Rapid prototyping:** Quickly iterate on UI changes by editing the template file and reloading the app.
- **Multiple layouts:** Easily swap or extend dashboard layouts by loading different template files as needed.

### 5. **Tooling and Editor Support**

- **Markdown syntax highlighting:** Most editors provide excellent support for `.md` files, making it easier to visualise and edit dashboard layouts.
- **Preview:** Some editors can preview Markdown, aiding in design.

---

## How It Works

- The dashboard layout is defined in a Markdown file (e.g., `dashboard_tpl.md`) using Taipy’s augmented Markdown syntax.
- Variables (like `{data}`, `{selected_point}`) are referenced in the template and bound to Python variables via the `data` dictionary in `Gui.run`.
- The template file is loaded at runtime using a helper class or a simple file read.

---

## Example

**dashboard_tpl.md**
```markdown
# My Dashboard

**Python version:** {python_version}  
**Taipy version:** {taipy_version}



Selected value: 
```

**main.py**
```python
from taipy.gui import Gui
from pathlib import Path

data = {...}
selected_point = 0
selected_value = ...
def on_selected_point_change(state): ...

page = Path("dashboard_tpl.md").read_text(encoding="utf-8")

Gui(page).run(
    data={
        "data": data,
        "selected_point": selected_point,
        "selected_value": selected_value,
        "on_selected_point_change": on_selected_point_change,
        # ...other variables
    }
)
```

---

## When Should You Use This Approach?

- For any non-trivial dashboard or when working in a team.
- When you want to keep your codebase organised and maintainable.
- When you anticipate frequent UI changes or want to reuse layouts.

---

## Summary

**The template approach for Taipy dashboards leads to cleaner, more maintainable, and more collaborative projects.**  