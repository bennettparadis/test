import streamlit as st
import pandas as pd
import pydeck as pdk

# Load data
df = pd.read_csv('data/2019-2023_oyster_densities.csv')

default_year = 2023
default_year_index = list(df["Year"].unique()).index(default_year)

year = st.sidebar.selectbox(
    "Select a Year:", 
    df["Year"].unique(),
    index=default_year_index,
    key="year_selector"  # Use a string for the key to avoid conflicts
)

df_selection = df[df["Year"] == year]

max_total = df_selection['total'].max()

# Create a formatted tooltip column
df_selection['tooltip'] = df_selection['total'].apply(lambda x: f"Oysters/m²: {x}")

density_layer = pdk.Layer(
    "HexagonLayer",
    data=df_selection,
    get_position=["Longitude", "Latitude"],
    radius=200,  # Adjust radius as needed
    elevation_scale=50,  # Adjust elevation scale
    elevation_range=[0, 3000],
    extruded=True,
    pickable=True,
    get_elevation="total",
    auto_highlight=True,
    get_fill_color="[255, total * 5, total * 5]",  # Adjust color mapping
)

# Define the tooltip
tooltip = {
    "html": "<b>{tooltip}</b>",
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
        layers=[density_layer],
        tooltip=tooltip
    )
)
