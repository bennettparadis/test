import streamlit as st
import pandas as pd
import plotly.express as px

#Label/units variable
oysters_per_sq_meter = "oysters/m²"

#Density calculations
def density_calc(df_selection):
        st.subheader("Density Metrics")
        
        if df_selection["total"].isnull().all():
            st.markdown('<p style="font-size:20px; font-family: Arial, sans-serif;">Total Density: Data not available for this site during this year.</p>', unsafe_allow_html=True)
        else:
            total_density = int(df_selection["total"].mean())
            st.markdown(f'<p style="font-size:20px; font-family: Arial, sans-serif;">Total Density: {total_density:,} {oysters_per_sq_meter}</p>', unsafe_allow_html=True)
        
        if df_selection["legal"].isnull().all():
            st.markdown('<p style="font-size:20px; font-family: Arial, sans-serif;">Legal Density: Data not available for this site during this year.</p>', unsafe_allow_html=True)
        else:
            legal_density = int(df_selection["legal"].mean())
            st.markdown(f'<p style="font-size:20px; font-family: Arial, sans-serif;">Legal Density: {legal_density:,} {oysters_per_sq_meter}</p>', unsafe_allow_html=True)
        
        if df_selection["sublegal"].isnull().all():
            st.markdown('<p style="font-size:20px; font-family: Arial, sans-serif;">Sublegal Density: Data not available for this site during this year.</p>', unsafe_allow_html=True)
        else:
            sublegal_density = int(df_selection["sublegal"].mean())
            st.markdown(f'<p style="font-size:20px; font-family: Arial, sans-serif;">Sublegal Density: {sublegal_density:,} {oysters_per_sq_meter}</p>', unsafe_allow_html=True)

        if df_selection["spat"].isnull().all():
            st.markdown('<p style="font-size:20px; font-family: Arial, sans-serif;">Spat Density: Data not available for this site during this year.</p>', unsafe_allow_html=True)
        else:
            spat_density = int(df_selection["spat"].mean())
            st.markdown(f'<p style="font-size:20px; font-family: Arial, sans-serif;">Spat Density: {spat_density:,} {oysters_per_sq_meter}</p>', unsafe_allow_html=True)

def make_histogram(data_selection, histogram_df, max_y):
    if histogram_df is None or histogram_df.empty:
        st.warning("No population data available.")
        return
    st.subheader("Population Structure")

    if not data_selection.empty:
        hist_plot = px.bar(
            histogram_df, 
            x= 'Level Valve Length (mm)', 
            y='Frequency (oysters/m²)', 
            color_discrete_sequence=['orange'],
            width=600,
            height=500)
        
        hist_plot.update_traces(
            marker=dict(line=dict(color= 'black', width=1)), 
            selector=dict(type='bar'),
            hoverlabel=dict(bgcolor='white', font=dict(color='black', size =16))
        )
        
        hist_plot.update_layout(
            paper_bgcolor = '#D6F2F4', 
            plot_bgcolor='#D6F2F4',
            bargap=0, 
            yaxis_range=[0,max_y],
            font=dict(color='black'),
            xaxis=dict(
                title=dict(text='Level Valve Length (mm)', font=dict(color='black', size =22)),
                tickfont=dict(color='black')
            ),
            yaxis=dict(
                title=dict(text='Frequency (oysters/m²)', font=dict(color='black', size =22)),
                tickfont=dict(color='black')
            )
        )

        hist_plot.add_vline(x=4.5, line=dict(color='red', width=3, dash='dash'))
        hist_plot.add_vline(x=14.5, line=dict(color='red', width=3, dash='dash'))

        hist_plot.add_annotation(
            x = 2,
            y=max_y,
            text="Spat",
            showarrow=False,
            font=dict(color='black', size=14),
            xref="x",
            yref="y"
        )

        hist_plot.add_annotation(
            x = 9,
            y=max_y,
            text="Sublegal",
            showarrow=False,
            font=dict(color='black', size=14),
            xref="x",
            yref="y"
        )

        hist_plot.add_annotation(
            x = 19.5,
            y=max_y,
            text="Legal",
            showarrow=False,
            font=dict(color='black', size=14),
            xref="x",
            yref="y"
        )

        st.plotly_chart(hist_plot, use_container_width=False)
    
    else:
        st.warning("No population data available.")