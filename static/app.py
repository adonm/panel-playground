import panel as pn
import pandas as pd

pn.extension(sizing_mode="stretch_width")

slider = pn.widgets.FloatSlider(start=0, end=10, name='Amplitude')

def callback(new):
    return f'Amplitude is: {new}'

pn.Row(slider, pn.bind(callback, slider)).servable(target='simple_app');

csv_file = 'https://raw.githubusercontent.com/holoviz/panel/master/examples/assets/occupancy.csv'
data = pd.read_csv(csv_file, parse_dates=['date'], index_col='date')

pn.pane.DataFrame(data.tail()).servable(target="df")