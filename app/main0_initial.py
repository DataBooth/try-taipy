# Taipy: What dashboard development should have been all along

import taipy as tp
from taipy.gui import Gui

data = {"x": [1, 2, 3, 4, 5], "y": [10, 11, 12, 13, 14]}

page = """
# The "I Can't Believe It's This Easy" Dashboard

## Your Amazing Visualization
<|{data}|chart|type=line|x=x|y=y|>

## Controls That Just Work
<|{selected_point}|slider|min=0|max=4|>

Selected value: <|{data["y"][selected_point]}|text|>
"""

Gui(page).run(title="Taipy Makes Other Frameworks Cry")
