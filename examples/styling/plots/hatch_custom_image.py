from bokeh.models import ImageURLTexture
from bokeh.plotting import figure, show

clips = [
    'https://static.bokeh.org/clipart/clipart-colorful-circles-64x64.png',
    'https://static.bokeh.org/clipart/clipart-celtic-repeating-64x64.png',
    'https://static.bokeh.org/clipart/clipart-tie-dye-64x64.png',
    'https://static.bokeh.org/clipart/clipart-ferns-64x64.png',
    'https://static.bokeh.org/clipart/clipart-diamond-tiles-64x64.png',
    'https://static.bokeh.org/clipart/clipart-abstract-squares-64x64.png',
    'https://static.bokeh.org/clipart/clipart-interlaced-pattern-64x64.png',
    'https://static.bokeh.org/clipart/clipart-mosaic-64x64.png',
    'https://static.bokeh.org/clipart/clipart-gold-stars-64x64.png',
    'https://static.bokeh.org/clipart/clipart-voronoi-2d-64x64.png',
    'https://static.bokeh.org/clipart/clipart-victorian-background-64x64.png',
    'https://static.bokeh.org/clipart/clipart-wallpaper-circles-64x64.png',
    'https://static.bokeh.org/clipart/clipart-beads-64x64.png',
]

p = figure(width=900, height=450, toolbar_location=None, tools="")
p.x_range.range_padding = p.y_range.range_padding = 0

for i, url in enumerate(clips):
    p.vbar(x=i+0.5, top=5, width=0.9, fill_color=None, line_color="black",
           hatch_pattern=dict(value='image'), hatch_extra={"image": ImageURLTexture(url=url)})

show(p)
