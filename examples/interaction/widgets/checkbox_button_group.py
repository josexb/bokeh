from bokeh.io import show
from bokeh.models import CheckboxButtonGroup, CustomJS

LABELS = ["Option 1", "Option 2", "Option 3"]

checkbox_button_group = CheckboxButtonGroup(labels=LABELS, active=[0, 1])
checkbox_button_group.js_on_event("button_click", CustomJS(args=dict(btn=checkbox_button_group), code="""
    console.log('checkbox_button_group: active=' + btn.active, this.toString())
"""))

show(checkbox_button_group)
