"""
Matthew Garchik
Computer Programming II Final

What is the relationship between a state's population, population density, urban index, income
"""


import os

import pandas as pd
import folium

url = 'https://raw.githubusercontent.com/python-visualization/folium/master/examples/data'
state_geo = f'{url}/us-states.json'

state_data = pd.read_csv("/Users/garch/PycharmProjects/P2_SP20/Final Project/Population - Sheet1 (1).csv")
state_data["Population"] = state_data["Population"].astype('float')
"""
m = folium.Map(location=[48, -102], zoom_start=3)

folium.Choropleth(
    geo_data=state_geo,
    name='choropleth',
    data=state_data,
    columns=['State', 'Population'],
    key_on='feature.properties.name',
    fill_color='YlGn',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='USA State Population'
).add_to(m)

folium.LayerControl().add_to(m)
m.save('USA_Population_Choropleth.html')

m2 = folium.Map(location=[48, -102], zoom_start=3)

folium.Choropleth(
    geo_data=state_geo,
    name='choropleth',
    data=state_data,
    columns=['State', 'Density'],
    key_on='feature.properties.name',
    fill_color='YlGn',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='USA State Population Density'
).add_to(m2)

folium.LayerControl().add_to(m2)
m2.save('USA_Population_Density_Choropleth.html')

m3 = folium.Map(location=[48, -102], zoom_start=3)

folium.Choropleth(
    geo_data=state_geo,
    name='choropleth',
    data=state_data,
    columns=['State', 'Unemployment'],
    key_on='feature.properties.name',
    fill_color='YlGn',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='USA State Unemployment (%)'
).add_to(m3)

folium.LayerControl().add_to(m3)
m3.save('USA_Unemployment_Choropleth.html')


m4 = folium.Map(location=[48, -102], zoom_start=3)

folium.Choropleth(
    geo_data=state_geo,
    name='choropleth',
    data=state_data,
    columns=['State', 'Mean_Income'],
    key_on='feature.properties.name',
    fill_color='YlGn',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='USA State Mean Income'
).add_to(m4)

folium.LayerControl().add_to(m4)
m4.save('USA_Mean_Income_Choropleth.html')

m5 = folium.Map(location=[48, -102], zoom_start=3)

folium.Choropleth(
    geo_data=state_geo,
    name='choropleth',
    data=state_data,
    columns=['State', 'Median_Income'],
    key_on='feature.properties.name',
    fill_color='YlGn',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='USA State Median Income'
).add_to(m5)

folium.LayerControl().add_to(m5)
m5.save('USA_Median_Income_Choropleth.html')

m6 = folium.Map(location=[48, -102], zoom_start=3)

folium.Choropleth(
    geo_data=state_geo,
    name='choropleth',
    data=state_data,
    columns=['State', 'Urbanity'],
    key_on='feature.properties.name',
    fill_color='YlGn',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='USA State Urbanity'
).add_to(m6)

folium.LayerControl().add_to(m6)
m6.save('USA_Urbanity_Choropleth.html')
/usr/local/bin/python3.8 "/Applications/PyCharm CE.app/Contents/helpers/pydev/pydevconsole.py" --mode=client --port=50225
import sys; print('Python %s on %s' % (sys.version, sys.platform))
sys.path.extend(['/Users/garch/PycharmProjects/P2_SP20'])
Python 3.8.1 (v3.8.1:1b293b6006, Dec 18 2019, 14:08:53) 
Type 'copyright', 'credits' or 'license' for more information
IPython 7.14.0 -- An enhanced Interactive Python. Type '?' for help.
PyDev console: using IPython 7.14.0
Python 3.8.1 (v3.8.1:1b293b6006, Dec 18 2019, 14:08:53) 
[Clang 6.0 (clang-600.0.57)] on darwin
import pandas as pd
df = pd.read_csv('/Users/garch/PycharmProjects/P2_SP20/Final Project/Population - Sheet1 (1).csv')
pd.plotting.scatter_matrix(df)
Backend MacOSX is interactive backend. Turning interactive mode on.
Out[4]: 
array([[<matplotlib.axes._subplots.AxesSubplot object at 0x10ede9d00>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x10eecfb50>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x115c4f340>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x115c78b80>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x115cae400>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x115cd5c70>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x115ce1b80>],
       [<matplotlib.axes._subplots.AxesSubplot object at 0x115d19460>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x115d6a5b0>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x115d92df0>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x115dc76a0>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x115df0ee0>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x115e24760>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x115e4ffa0>],
       [<matplotlib.axes._subplots.AxesSubplot object at 0x115e81820>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x115ebae80>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x115ee0940>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x115f17f70>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x115f3ea00>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x115f76280>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x115f9eac0>],
       [<matplotlib.axes._subplots.AxesSubplot object at 0x115fd33a0>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x115ffdbe0>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x116030460>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x11605bd00>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x11608e580>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x1160b9dc0>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x1160ee640>],
       [<matplotlib.axes._subplots.AxesSubplot object at 0x116117e80>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x11614a760>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x116173fa0>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x1161a8820>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x1161dee80>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x116207910>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x11623ff40>],
       [<matplotlib.axes._subplots.AxesSubplot object at 0x1162669d0>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x11629c2b0>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x1162c4af0>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x1162f9370>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x116323bb0>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x116355430>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x116381c70>],
       [<matplotlib.axes._subplots.AxesSubplot object at 0x1163b54f0>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x1163dfd30>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x1164145b0>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x11643ddf0>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x116472670>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x11649beb0>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x1164d0730>]],
      dtype=object)
df.plot(y='Unemployment', x='Mean_Income', kind='scatter')
Out[5]: <matplotlib.axes._subplots.AxesSubplot at 0x1178792b0>
df.plot(y='Unemployment', x='Median_Income', kind='scatter')
Out[6]: <matplotlib.axes._subplots.AxesSubplot at 0x1178917c0>
df.plot(y='Unemployment', x='Urbanity', kind='scatter')
Out[7]: <matplotlib.axes._subplots.AxesSubplot at 0x1150d36d0>
pd.plotting.scatter_matrix(df)
Out[8]: 
array([[<matplotlib.axes._subplots.AxesSubplot object at 0x115135160>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x1154a9c70>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x1154db520>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x115506d60>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x11553b5e0>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x115567e20>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x115573d30>],
       [<matplotlib.axes._subplots.AxesSubplot object at 0x1155a5670>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x1155f77c0>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x11562fdf0>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x115657880>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x11568ceb0>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x1156b6a00>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x1156ed280>],
       [<matplotlib.axes._subplots.AxesSubplot object at 0x115717ac0>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x11574c340>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x117982b80>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x1179b8400>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x1179e1c40>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x117a164c0>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x117a40d00>],
       [<matplotlib.axes._subplots.AxesSubplot object at 0x117a75580>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x117a9e700>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x117ca7f40>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x117cd07c0>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x117cfddf0>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x117d1c880>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x117d4eeb0>],
       [<matplotlib.axes._subplots.AxesSubplot object at 0x117d76940>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x117dacf70>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x117dd6a00>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x117e0d280>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x11a69cac0>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x11a6d1340>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x11cb01b80>],
       [<matplotlib.axes._subplots.AxesSubplot object at 0x11cb37400>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x11cb5ec40>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x11cb954c0>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x11cbbfd00>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x11cbf3580>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x11cc1fdc0>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x11cc54640>],
       [<matplotlib.axes._subplots.AxesSubplot object at 0x11cc7fe80>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x11ccb3730>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x11ccdefa0>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x11cd13820>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x11cd4ae50>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x11cd728e0>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x11cda9f10>]],
      dtype=object)
df.plot(y='Mean_Income', x='Urbanity', kind='scatter')
Out[9]: <matplotlib.axes._subplots.AxesSubplot at 0x11d06cb80>
df.plot(y='Median_Income', x='Urbanity', kind='scatter')
Out[10]: <matplotlib.axes._subplots.AxesSubplot at 0x11d5ed220>
pd.plotting.scatter_matrix(df)
Out[11]: 
array([[<matplotlib.axes._subplots.AxesSubplot object at 0x11d5f3ee0>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x11d6288b0>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x11d659f10>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x11d6839a0>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x11d6b9fd0>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x11d6e1a60>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x11d6ee970>],
       [<matplotlib.axes._subplots.AxesSubplot object at 0x11d725250>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x11d7763a0>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x11d7a0be0>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x11d7d6460>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x11d800ca0>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x11d835520>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x11d85fd60>],
       [<matplotlib.axes._subplots.AxesSubplot object at 0x11d8955e0>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x11d8c0e20>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x11d8f26a0>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x11d91fee0>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x11d953760>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x11d97dfa0>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x11d9b1820>],
       [<matplotlib.axes._subplots.AxesSubplot object at 0x11d9e8e50>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x11e9428e0>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x11e978f10>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x11e9a29a0>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x11e9d9fd0>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x11ea02a60>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x11ea382e0>],
       [<matplotlib.axes._subplots.AxesSubplot object at 0x11ea63b20>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x11ea983a0>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x11eac2be0>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x11eaf8460>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x11eb22ca0>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x11eb57520>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x11eb7fd60>],
       [<matplotlib.axes._subplots.AxesSubplot object at 0x11ebb75e0>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x11ebe0e20>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x11ec146a0>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x11ec40ee0>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x11ec73760>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x11ec9efa0>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x11ecd1820>],
       [<matplotlib.axes._subplots.AxesSubplot object at 0x11ed0ae50>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x11ed338e0>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x11ed6bf10>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x11ed949a0>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x11edcafd0>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x11edf3a60>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x11ee282e0>]],
      dtype=object)
df.plot(y='Urbanity', x='Density', kind='scatter')
Out[12]: <matplotlib.axes._subplots.AxesSubplot at 0x11f0e06d0>
df.plot(x='Urbanity', y='Density', kind='scatter')
Out[13]: <matplotlib.axes._subplots.AxesSubplot at 0x11f0e8040>
df.plot(y='Median_Income', x='Urbanity', kind='scatter')
Out[14]: <matplotlib.axes._subplots.AxesSubplot at 0x11fb12af0>
df.plot(y='Mean_Income', x='Urbanity', kind='scatter')
Out[15]: <matplotlib.axes._subplots.AxesSubplot at 0x120038520>
df.plot(y='Mean_Income', x='Median_Income', kind='scatter')
Out[16]: <matplotlib.axes._subplots.AxesSubplot 
"""
