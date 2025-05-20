from taipy.gui import Gui
from utils import TaipyTemplateHelper, VersionInfo

data = {"x": [1, 2, 3, 4, 5], "y": [10, 11, 12, 13, 14]}
selected_point = 0
selected_value = data["y"][selected_point]


def on_selected_point_change(state):
    state.selected_value = state.data["y"][state.selected_point]


version_info = VersionInfo()

print(version_info.as_dict())

# Load the template (cached after first load)
page = TaipyTemplateHelper.load("dashboard2_tpl.md", base_dir="app/ui")

print(page)

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
