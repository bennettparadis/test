import streamlit as st
import plotly.express as px
import numpy as np
import pandas as pd
import geopandas as gpd
import warnings
import maps

# Suppress warnings
warnings.filterwarnings('ignore')

# Tab display 
st.set_page_config(page_title="NC Oyster Sanctuary Data", page_icon=":oyster:", layout="wide")

#IMPORT OS DATA (densities and extraction samples)
OSMaterial = gpd.read_file("data/OS_material_storymap.shp")
df = pd.read_csv("data/2019-2023_oyster_densities.csv")

# --- HEADER & INFO TEXT ---
st.markdown(
    f"""
    <div style="text-align: center;">
        <p style="font-size:50px; font-weight: bold;">🦪View Oyster Sanctuary Maps</p>
    </div>
    """, 
    unsafe_allow_html=True
)

st.markdown(
    f"""
    <div style="text-align: center;">
        <p style="font-size:20px;">Noth Carolina's oyster sanctuaries are large-scale restoration sites ranging from 4 to 80. Each sanctuary has been built with a variety of materials such as crushed aggregate rock (marl limestone, granite, concrete, basalt), reef balls, concrete pipe, and recycled shell. Here you can view the material blueprint and additional information for each sanctuary. </p>
    </div>
    """, 
    unsafe_allow_html=True
)

st.info(
    """
    **Select an oyster sanctuary from the dropdown menu on the left to see the site information and map. Click, drag, and zoom in and on the material blueprint. Hover your cursor over the different polygons to get information on the material type, coordinates, deployment date, and area. This geospatial data includes all materials deployed between 1996 and 2023.** 
"""
)

# ----- SIDE BAR -----
sanctuary_names = sorted(df["OS_Name"].unique())
default_sanctuary1 = "Neuse River"

default_sanctuary_index1 = list(df["OS_Name"].unique()).index(default_sanctuary1)


st.sidebar.subheader("Use the filters to explore the different material footprints at each Sanctuary!")
st.sidebar.header("Select Filters:")

sanctuary1 = st.sidebar.selectbox(
    "Select an Oyster Sanctuary:",
    sanctuary_names,
    index=default_sanctuary_index1,
    key=11
)

# Filter the GeoDataFrame based on the selected sanctuary
filtered_material1 = OSMaterial[OSMaterial['OS_Site'] == sanctuary1]

col1, col2 = st.columns([15,5])

with col1:
    #MAP
    maps.display_map(sanctuary1, filtered_material1, 900, 1200)

with col2:
    #SANCTUARY SITE INFORMATION
    maps.site_info(sanctuary1)

    st.info("""
    *Permit acreage is the boundary area delineated as protected habitat under NC law
    
    *Developed habitat is the area covered by material and the space between mounds/ridges  
""")