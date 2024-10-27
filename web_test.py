from bokeh.io import export_svgs
from bokeh.plotting import curdoc, figure, show
import pandas as pd

data = pd.read_csv("year_data_flattened.csv")

p = figure(title="Year", 
           x_axis_label='Day', 
           y_axis_label='Demand', 
           x_range=(0, 365 * 24), 
           width=1000, 
           height=400, 
           output_backend="svg")

p.background_fill_color = None
p.border_fill_color = None
p.line(x=list(range(365 * 24)), y=data["0"], line_width=1)

p.xaxis.ticker = [24 * 7 * i for i in range((365 * 24) // (24 * 7) + 1)]
p.xaxis.major_label_overrides = {24 * 7 * i: f"Day {7 * i}" for i in range((365 * 24) // (24 * 7) + 1)}
p.xaxis.major_label_orientation = 3.14 / 2

p.title.text_color = "white"  
p.xaxis.axis_label_text_color = "white"  
p.yaxis.axis_label_text_color = "white"  
p.xaxis.major_label_text_color = "white"
p.yaxis.major_label_text_color = "white" 

export_svgs(p, filename="static/plot.svg")