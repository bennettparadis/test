import streamlit as st
import pandas as pd
import pydeck as pdk
import geopandas as gpd

# Load data
df = pd.read_csv('data/2019-2023_oyster_densities.csv')
OSMaterial = gpd.read_file("data/OS_material_storymap.shp")
OSBoundaries = gpd.read_file("data/permit_boundaries.shp")

# Set up the Streamlit page
st.set_page_config(page_title="NC Oyster Sanctuary Data", page_icon=":oyster:", layout="wide")

st.markdown(
    f"""
    <div style="text-align: center;">
        <p style="font-size:50px; font-weight: bold;">🌍Explore Pamlico Sound</p>
    </div>
    """, 
    unsafe_allow_html=True
)

st.markdown(
    f"""
    <div style="text-align: center;">
        <p style="font-size:20px;">Welcome to North Carolina's Pamlico Sound -- home to 15 oyster sanctuaries spanning 563 acres of protected subtidal habitat. Every year NCDMF's Habitat & Enhancement dive team visits each sanctuary to collect oyster density estimates all around the reefs which are then used for further analysis and to quantify reef performance.</p>
    </div>
    """, 
    unsafe_allow_html=True
)

st.info("""
    **Explore the map to see how oyster densities differ across Pamlico Sound. Zoom in and you will see where our dive team has sampled along each sanctuary and the general layout of each site. Hold the right mouse button to rotate the map. Hover your cursor over the columns to see how many oysters were found at each point. Select a year from the drop down menu in the sidebar to see how densities change over time.** 
    
    *NOTE: Red columns indicate two or more samples were collected in close proximity to one another.
""")

st.sidebar.subheader("Use the dropdown to select a year and explore oyster densities across the Oyster Sanctuary Network")
default_year = 2023
default_year_index = list(df["Year"].unique()).index(default_year)

year = st.sidebar.selectbox(
    "Select a Year:", 
    df["Year"].unique(),
    index=default_year_index,
    key=30
)

df_selection = df.query("Year == @year")

# Remove rows with missing values in 'Latitude', 'Longitude', 'total'
df_selection = df_selection.dropna(subset=['Latitude', 'Longitude', 'total'])

# Extract centroids for each geometry in OSBoundaries
OSBoundaries['centroid'] = OSBoundaries.geometry.centroid
OSBoundaries['Latitude'] = OSBoundaries.centroid.y
OSBoundaries['Longitude'] = OSBoundaries.centroid.x

# Convert centroids to a DataFrame
boundary_centroid_data = OSBoundaries[['OS_Name', 'Latitude', 'Longitude']]

# Convert GeoDataFrame to GeoJSON dictionary
geojson_dict = OSMaterial.to_crs(epsg=4326).__geo_interface__

# Define layers
# TextLayer with positions of each geometry's centroid
text_layer = pdk.Layer(
    "TextLayer",
    data=boundary_centroid_data,
    get_position=["Longitude", "Latitude"],
    get_text="OS_Name",
    get_color=[0, 0, 0, 255],
    get_size=20,
    get_alignment_baseline="'top'",
)

# Material layer
material_layer = pdk.Layer(
    "GeoJsonLayer",
    data=geojson_dict,  
    get_fill_color=[255, 0, 0, 150],
    pickable=True,
)

max_total = df_selection['total'].max()

density_layer = pdk.Layer(
    "ColumnLayer",
    data=df_selection,
    get_position=["Longitude", "Latitude"],
    get_elevation="total",
    radius=8,
    elevation_scale=1,
    get_fill_color=[255, 0, 0, 150],
    pickable=True,
    auto_highlight=True,
)

tooltip = {
    "html": "<b>Oysters/m²:</b> {total}",
    "style": {
        "backgroundColor": "steelblue",
        "color": "white"
    }
}

# Display map
st.pydeck_chart(
    pdk.Deck(
        map_style="mapbox://styles/mapbox/outdoors-v9",
        initial_view_state={
            "latitude": 35.05,
            "longitude": -76.4,
            "zoom": 11.2,
            "pitch": 60,
        },
        layers=[text_layer, density_layer, material_layer],
        tooltip=tooltip  # Add the tooltip configuration
    )
)
