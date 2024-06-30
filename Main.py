import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="NC Oyster Sanctuary Data", page_icon=":oyster:", layout="wide")

# Define the custom CSS
custom_css = """
<style>
    /* Change the color and font of the page titles in the sidebar */
    .eczjsme13 {
        color: #00647B !important; /* Replace with your desired color */
        font-weight: bold !important;
        font-size: 16px !important;
    }
</style>
"""

# Apply the custom CSS
st.markdown(custom_css, unsafe_allow_html=True)

# --- MAINPAGE ---

st.markdown('''
            <style>
            body {background-color: white;
            }
            <style>
            ''', unsafe_allow_html=True)

st.markdown(
    f"""
    <div style="text-align: center;">
        <p style="font-size:60px; font-weight: bold;">🦪 Oyster Sanctuary Data Dashboard 📊</p>
    </div>
    """, 
    unsafe_allow_html=True
)

st.info("**Hello and welcome to the Oyster Sanctuary Data Visualization Dashboard! The dataset featured here is part of ongoing oyster restoration and monitoring efforts in North Carolina. "
           f"If you would like to learn more about the importance of Oyster Sanctuaries and how they are built in North Carolina, please visit the [StoryMap](https://storymaps.arcgis.com/stories/d876f9b131174f859270c600ccf3545f)!**")

st.markdown(
    f"""
    <div style="text-align: left;">
        <p style="font-size:20px;">In 1996, the North Carolina Division of Marine Fisheries began building artificial reefs with the specific aim of creating protected habitat for subtidal oysters. These Oyster Sanctuaries are closed to harvest with the goal of creating a network of thriving and self-sustaining oyster reefs throughout Pamlico Sound. </p>
    <div style="text-align: left;">
        <p style="font-size:20px;">DMF's dive team conducts annual monitoring to gather data with the aim of quantifying the performance and longevity of the sanctuaries. This dashboard allows users to explore the dataset collected from these yearly SCUBA surveys. Here you can interact with the data by choosing filters in the sidebar.</p>
    </div>
    """, 
    unsafe_allow_html=True
)

st.sidebar.success("Choose how you want to explore the dataset!")

df = pd.read_csv('data/2019-2023_oyster_densities.csv')

year = st.sidebar.selectbox(
    "Select a Year:", 
    df["Year"].unique(),
    key=10
)

df_selection = df.query(
    "Year == @year"
)

col1, col2 = st.columns(2)
sampling_effort = {
    '2019': {
        'samples':'109',
        'oysters': '4,995'
    },
    '2020': {
        'samples':'123',
        'oysters': '17,898'
    },
    '2021': {
        'samples':'128',
        'oysters':'16,637'
    },
    '2022': {
        'samples':'146',
        'oysters':'18,255'
    },
    '2023': {
        'samples':'136',
        'oysters':'26,652'
    },
}

with col1:
    # Donut chart
    legal_sum = df_selection['legal'].sum()
    sublegal_sum = df_selection['sublegal'].sum()
    spat_sum = df_selection['spat'].sum()

    labels = ['Legal (>75mm)', 'Sublegal (26mm< x <76mm)', 'Spat (<26mm)']
    values = [legal_sum, sublegal_sum, spat_sum]
    fig = go.Figure(
        data=[go.Pie(labels=labels, values=values, hole=0.3)]
    )
    fig.update_traces(
        marker=dict(colors=['#636EFA', '#EF553B', '#00CC96'], line=dict(color='black', width=2)),
        hoverlabel=dict(bgcolor='white', font=dict(color='black', size=16))
    )
    fig.update_layout(
        title=f"Size Class Breakdown - Sampling {year}"
    )
    # Displaying the figure in Streamlit
    st.plotly_chart(fig)
    
with col2:

    st.info(""" 
        **Select a year in the sidebar on the left to change the graphic!** 
            
        **Move your cursor over the graphic to see more info.**   
            
        On the sidebar you can also choose the different tabs to dive deeper into North Carolina's Oyster Sanctuary dataset:
        - Learn about our methodology
        - Explore Pamlico Sound
        - View the blueprints for each sanctuary
        - Compare oyster populations
        - Analyze the performance of different materials used on the sanctuaries
        """)

st.markdown(custom_css, unsafe_allow_html=True)

# --- MAINPAGE ---

st.markdown('''
            <style>
            body {background-color: white;
            }
            <style>
            ''', unsafe_allow_html=True)

st.markdown(
    f"""
    <div style="text-align: center;">
        <p style="font-size:60px; font-weight: bold;">🦪 Oyster Sanctuary Data Dashboard 📊</p>
    </div>
    """, 
    unsafe_allow_html=True
)

st.info("**Hello and welcome to the Oyster Sanctuary Data Visualization Dashboard! The dataset featured here is part of ongoing oyster restoration and monitoring efforts in North Carolina. "
           f"If you would like to learn more about the importance of Oyster Sanctuaries and how they are built in North Carolina, please visit the [StoryMap](https://storymaps.arcgis.com/stories/d876f9b131174f859270c600ccf3545f)!**")

st.markdown(
    f"""
    <div style="text-align: left;">
        <p style="font-size:20px;">In 1996, the North Carolina Division of Marine Fisheries began building artificial reefs with the specific aim of creating protected habitat for subtidal oysters. These Oyster Sanctuaries are closed to harvest with the goal of creating a network of thriving and self-sustaining oyster reefs throughout Pamlico Sound. </p>
    <div style="text-align: left;">
        <p style="font-size:20px;">DMF's dive team conducts annual monitoring to gather data with the aim of quantifying the performance and longevity of the sanctuaries. This dashboard allows users to explore the dataset collected from these yearly SCUBA surveys. Here you can interact with the data by choosing filters in the sidebar.</p>
    </div>
    """, 
    unsafe_allow_html=True
)

st.sidebar.success("Choose how you want to explore the dataset!")

df = pd.read_csv('data/2019-2023_oyster_densities.csv')

year = st.sidebar.selectbox(
    "Select a Year:", 
    df["Year"].unique(),
    key=10
)

df_selection = df.query(
    "Year == @year"
)

col1, col2 = st.columns(2)
sampling_effort = {
    '2019': {
        'samples':'109',
        'oysters': '4,995'
    },
    '2020': {
        'samples':'123',
        'oysters': '17,898'
    },
    '2021': {
        'samples':'128',
        'oysters':'16,637'
    },
    '2022': {
        'samples':'146',
        'oysters':'18,255'
    },
    '2023': {
        'samples':'136',
        'oysters':'26,652'
    },
}

with col1:
    # Donut chart
    legal_sum = df_selection['legal'].sum()
    sublegal_sum = df_selection['sublegal'].sum()
    spat_sum = df_selection['spat'].sum()

    labels = ['Legal (>75mm)', 'Sublegal (26mm< x <76mm)', 'Spat (<26mm)']
    values = [legal_sum, sublegal_sum, spat_sum]
    fig = go.Figure(
        data=[go.Pie(labels=labels, values=values, hole=0.3)]
    )
    fig.update_traces(
        marker=dict(colors=['#636EFA', '#EF553B', '#00CC96'], line=dict(color='black', width=2)),
        hoverlabel=dict(bgcolor='white', font=dict(color='black', size=16))
    )
    fig.update_layout(
        title=f"Size Class Breakdown - Sampling {year}"
    )
    # Displaying the figure in Streamlit
    st.plotly_chart(fig)
    
with col2:

    st.info(""" 
        **Select a year in the sidebar on the left to change the graphic!** 
            
        **Move your cursor over the graphic to see more info.**   
            
        On the sidebar you can also choose the different tabs to dive deeper into North Carolina's Oyster Sanctuary dataset:
        - Learn about our methodology
        - Explore Pamlico Sound
        - View the blueprints for each sanctuary
        - Compare oyster populations
        - Analyze the performance of different materials used on the sanctuaries
        """)
