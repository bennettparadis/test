import streamlit as st
import plotly.express as px
import pandas as pd

df = pd.read_csv("data/2019-2023_oyster_densities.csv")

#Sanctuary dictionary with relevant information
OS_dict = {
    'Croatan Sound': {
        'permit': 7.7, 
        'developed':7.7,
        'aggregate': '2,093',
        'established':1996,
        'recent':2013,
        'materials': ['Marl', 'Reef Ball', 'Shell'],
        'zoom':17.0
    },
    'Deep Bay': {
        'permit': 17.2, 
        'developed':7.73,
        'aggregate': '1,749',
        'established':1996,
        'recent':2014,
        'materials':['Marl', 'Reef Ball', 'Shell'],
        'zoom':17.0
    },
    'West Bay': {
        'permit': 6.6, 
        'developed':6.6,
        'aggregate': '2,329',
        'established':1996,
        'recent':2014,
        'materials':['Marl', 'Reef Ball', 'Shell'],
        'zoom':17.5
    },
    'Crab Hole': {
        'permit': 30.5, 
        'developed':30.5,
        'aggregate': '36,489',
        'established':2003,
        'recent':2009,
        'materials':['Marl'],
        'zoom':16.0
    },
    'Middle Bay': {
        'permit': 4.6, 
        'developed':4.6,
        'aggregate': '900',
        'established':2004,
        'recent':2004,
        'materials':['Marl'],
        'zoom':18.6
    },
    'Neuse River': {
        'permit': 11.2, 
        'developed':11.2,
        'aggregate': '7,357',
        'established':2005,
        'recent':2008,
        'materials':['Marl'],
        'zoom':17.2
    },
    'West Bluff': {
        'permit': 29.42, 
        'developed':10.0,
        'aggregate': '10,162',
        'established':2005,
        'recent':2013,
        'materials':['Marl', 'Reef Ball'],
        'zoom':16.8
    },
    'Gibbs Shoal': {
        'permit': 54.7, 
        'developed':54.7,
        'aggregate': '22,447',
        'established':2009,
        'recent':2013,
        'materials':['Marl', 'Reef Ball'],
        'zoom':16.2
    },
    'Long Shoal': {
        'permit': 10.0, 
        'developed':6.8,
        'aggregate': 'N/A (1,035 Reef Balls)',
        'established':2013,
        'recent':2013,
        'materials':['Reef Ball'],
        'zoom':16.0
    },
    'Raccoon Island': {
        'permit': 10.0, 
        'developed':10.0,
        'aggregate': '1,824',
        'established':2013,
        'recent':2016,
        'materials':['Crushed Concrete', 'Consolidated Concrete', 'Reef Ball'],
        'zoom':17.0
    },
    'Pea Island': {
        'permit': 46.4, 
        'developed':33.9,
        'aggregate': '3,420',
        'established':2015,
        'recent':2015,
        'materials':['Crushed Concrete', 'Consolidated Concrete', 'Reef Ball'],
        'zoom':16.2
    },
    'Little Creek': {
        'permit': 20.7, 
        'developed':20.7,
        'aggregate': '5,700',
        'established':2016,
        'recent':2016,
        'materials':['Crushed Concrete', 'Consolidated Concrete', 'Reef Ball', 'Granite', 'Marl', 'Reef Ball'],
        'zoom':16.8
    },
    'Swan Island': {
        'permit': 80.3, 
        'developed':62.6,
        'aggregate': '55,000',
        'established':2017,
        'recent':2021,
        'materials':['Granite', 'Marl'],
        'zoom':15.5
    },
    'Cedar Island': {
        'permit': 75.0, 
        'developed':70.3,
        'aggregate': '51,800',
        'established':2021,
        'recent':2023,
        'materials':['Crushed Concrete', 'Marl'],
        'zoom':15.8
    }
}

# Define the color mapping dictionary
color_scale = px.colors.qualitative.G10
unique_materials = df['Material'].unique()
color_discrete_map = {material: color_scale[i % len(color_scale)] for i, material in enumerate(unique_materials)}
transparency_value = 0.7


def site_info(sanctuary_selection):
    st.subheader("Site Info")
    st.markdown(f'<p style="font-size:20px; font-family: Arial, sans-serif;">Permit Acreage: {OS_dict[sanctuary_selection]["permit"]} acres</p>', unsafe_allow_html=True)
    st.markdown(f'<p style="font-size:20px; font-family: Arial, sans-serif;">Developed Habitat: {OS_dict[sanctuary_selection]["developed"]} acres</p>', unsafe_allow_html=True)
    st.markdown(f'<p style="font-size:20px; font-family: Arial, sans-serif;">Year Established: {OS_dict[sanctuary_selection]["established"]}</p>', unsafe_allow_html=True)
    #st.markdown(f'<p style="font-size:20px; font-family: Arial, sans-serif;">Most Recent Addition: {OS_dict[sanctuary_selection]["recent"]}</p>', unsafe_allow_html=True)
    st.markdown(f'<p style="font-size:20px; font-family: Arial, sans-serif;">Total Aggregate Rock: {OS_dict[sanctuary_selection]["aggregate"]} tons</p>', unsafe_allow_html=True)


def display_map(sanctuary_selection, filtered_materials, height, width):
    st.subheader(f"Map of {sanctuary_selection}")

    if not filtered_materials.empty:
        # Reproject the GeoDataFrame to WGS84 (EPSG:4326) if necessary
        if filtered_materials.crs != 'EPSG:4326':
            filtered_materials = filtered_materials.to_crs(epsg=4326)

        # Convert GeoDataFrame to GeoJSON
        geojson1 = filtered_materials.__geo_interface__

        hover_columns = ["REEF_SITE", "OS_Site", "Material", "DeployYear", "DeployMont", "AREA_SQFT", "Latitude", "Longitude"]

        # Create a Plotly map
        fig = px.choropleth_mapbox(
            filtered_materials,
            geojson=geojson1,
            locations=filtered_materials.index,
            color="Material",
            color_discrete_map=color_discrete_map,
            mapbox_style="carto-positron",
            center={"lat": filtered_materials.geometry.centroid.y.mean(), "lon": filtered_materials.geometry.centroid.x.mean()},
            zoom=OS_dict[sanctuary_selection]["zoom"],
            opacity=transparency_value,
            height=height,#650,
            width=width, #650,
            hover_data=hover_columns
            #title=f"Map of {sanctuary}"
        )

        fig.update_layout(
            legend=dict(
                title= dict(
                    text='Material',
                    font= dict(color='black', size=16)
                ),
                font=dict(color='black', size=16)  # Update font size for legend text
            ),
            font=dict(color='black', size=16)
        )

        fig.update_traces(
            hoverlabel=dict(bgcolor='white', font=dict(color='black', size=14))
        )

        st.plotly_chart(fig)
    else:
        st.warning("No map data available for the selected sanctuary.")