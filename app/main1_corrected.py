from taipy.gui import Gui
from version_info import VersionInfo

# Data setup
data = {"x": [1, 2, 3, 4, 5], "y": [10, 11, 12, 13, 14]}
selected_point = 0
selected_value = data["y"][selected_point]


def on_selected_point_change(state):
    # Update the selected_value when the slider changes
    state.selected_value = state.data["y"][state.selected_point]


# Instantiate version info
version_info = VersionInfo()

page = """
# The "I Can't Believe It's This Easy" Dashboard

**Python version:** {python_version}  
**Taipy version:** {taipy_version}  
**OS:** {os_full}

## Your Amazing Visualization
<|{{data}}|chart|type=line|x=x|y=y|>

## Controls That Just Work
<|{{selected_point}}|slider|min=0|max=4|on_change=on_selected_point_change|>

Selected value: <|{{selected_value}}|text|>
""".format(**version_info.as_dict())


Gui(page).run(
    title="Taipy Makes Other Frameworks Cry",
    data={
        "data": data,
        "selected_point": selected_point,
        "selected_value": selected_value,
        "on_selected_point_change": on_selected_point_change,
        **version_info.as_dict(),
    },
)
