import numpy as np
import pandas as pd
import bokeh
from bokeh.io import curdoc, output_notebook, show, reset_output
from bokeh.layouts import column, layout, widgetbox, row
from datetime import date
from bokeh.models.widgets import DateSlider, RadioGroup
from bokeh.tile_providers import get_provider, Vendors
from bokeh.models import WMTSTileSource, ColumnDataSource, CustomJS, Slider, Select, Button
from bokeh.plotting import figure, output_file, show
# output_notebook()

url = 'http://a.basemaps.cartocdn.com/rastertiles/voyager/{Z}/{X}/{Y}.png'

x_range,y_range = ((-13884029,-7453304), (2698291,6455972))

# Read Data
df1 = pd.read_csv('time_series_covid19_confirmed_global.csv')
df2 = pd.read_csv('time_series_covid19_deaths_global.csv')
df3 = pd.read_csv('time_series_covid19_recovered_global.csv')

#Data Confirmed
df1['Province/State'].fillna('',inplace=True)
df1['Country/Region'] = df1['Country/Region'] + '-' + df1['Province/State']
df1.rename(columns = {'Country/Region':'Region'}, inplace = True)

#Data Deaths
df2['Province/State'].fillna('',inplace=True)
df2['Country/Region'] = df2['Country/Region'] + df2['Province/State']
df2.rename(columns = {'Country/Region':'Region'}, inplace = True)

#Data Recovered
df3['Province/State'].fillna('',inplace=True)
df3['Country/Region'] = df3['Country/Region'] + df3['Province/State']
df3.rename(columns = {'Country/Region':'Region'}, inplace = True)

def create_coordinates(df, lon="Long", lat="Lat"):
    # Converts decimal longitude/latitude to Web Mercator format
    k = 6378137
    df["x"] = df[lon] * (k * np.pi/180.0)
    df["y"] = np.log(np.tan((90 + df[lat]) * np.pi/360.0)) * k
    return df

#Data confirmed
df1 = pd.DataFrame(dict(df1))
create_coordinates(df1)
dtf1 = df1.iloc[:, 4:100]
df1['Jumlah'] = dtf1.sum(axis=1)

#Data deaths
df2 = pd.DataFrame(dict(df2))
create_coordinates(df2)
dtf2 = df2.iloc[:, 4:100]
df2['Jumlah'] = dtf2.sum(axis=1)

#Data recovered
df3 = pd.DataFrame(dict(df3))
create_coordinates(df3)
dtf3 = df3.iloc[:, 4:100]
df3['Jumlah'] = dtf3.sum(axis=1)


reg = Select(title="Region", options=list(df1['Region']), value="All")
# tgl = DateSlider(title="Tanggal", start=date(2020, 1, 22), end=date(2020, 4, 25), value=date(2020, 3, 20), step=1)
jml = Slider(title='Jumlah Kasus Min', start=0, end=100000, step=1000, value=100)
radio = RadioGroup(labels=["Data1", "Data2", "Data3"], active=0)

source1 = ColumnDataSource(data=dict(x=[], y=[], jum=[]))
source2 = ColumnDataSource(data=dict(x=[], y=[], jum=[]))
source3 = ColumnDataSource(data=dict(x=[], y=[], jum=[]))

TOOLTIPS=[
    ("Region", "@region"),
    ("Jumlah", "@jumlah")
]

p = figure(plot_height=400, plot_width=600, toolbar_location=None, 
           tooltips=TOOLTIPS, x_range=x_range, 
           y_range=y_range, x_axis_type='mercator', 
           y_axis_type='mercator')
p.add_tile(WMTSTileSource(url=url))
p1 = p.circle(x="x", y="y", source=source1, size=7, color="red")
p2 = p.circle(x="x", y="y", source=source2, size=7, color="blue")
p3 = p.circle(x="x", y="y", source=source3, size=7, color="green")

radiohandler = CustomJS(args=dict(plot1=p1, plot2=p2, plot3=p3), code="""   
    while (var bool=True) {
        if (cb_obj.active == 0) {
            plot1.visible = true;
            plot2.visible = false;
            plot3.visible = false;
            bool=False;
        } else if (cb_obj.active == 1) {
            plot2.visible = true;
            plot1.visible = false;
            plot3.visible = false;
            bool=False;
        } else if(cb_obj.active == 2) {
            plot3.visible = true;
            plot2.visible = false;
            plot1.visible = false;
            bool=False;
        }
    }
    
    source.change.emit()
""")

def btnhandler():
    rad_select = radio.active
    if rad_select == 0:
        p1(visible=True)
        p2(visible=False)
        p3(visible=False)
    elif rad_select == 2:
        p1(visible=False)
        p2(visible=True)
        p3(visible=False)
    elif rad_select == 2:
        p1(visible=False)
        p2(visible=False)
        p3(visible=True)

def select_data():
    rad_select = radio.active
    reg_val = reg.value
    if rad_select == 0:
        selected = df1[(df1.Jumlah >= jml.value)]
    elif rad_select == 1:
        selected = df2[(df2.Jumlah >= jml.value)]
    elif rad_select == 2:
        selected = df3[(df3.Jumlah >= jml.value)]
        
    if (reg_val != "All"):
        selected = selected[selected.Region.str.contains(reg_val)==True]
    
    return selected

def update_data():
    df_new = select_data()
    rad_select = radio.active
    if rad_select == 0:
        source1.data = dict(
        x = df_new['x'],
        y = df_new['y'],
        region = df_new['Region'],
        jumlah = df_new['Jumlah']
    )
    elif rad_select == 1:
        source2.data = dict(
        x = df_new['x'],
        y = df_new['y'],
        region = df_new['Region'],
        jumlah = df_new['Jumlah']
    )
    elif rad_select == 2:
        source3.data = dict(
        x = df_new['x'],
        y = df_new['y'],
        region = df_new['Region'],
        jumlah = df_new['Jumlah']
    )       
    
btn = Button(label="Click")

controls = [reg, jml]
for control in controls:
    control.on_change('value', lambda attr, old, new: update_data())
    radio.js_on_event('active', radiohandler)
    btn.on_click(btnhandler)

inputs = column(*controls, width=200, height=100)
inputs.sizing_mode = "fixed"
l = layout(column(row(radio, inputs, width=200, height=100), btn, p))

update_data()  # initial load of the data

curdoc().add_root(l)
curdoc().title = "Covid19"
