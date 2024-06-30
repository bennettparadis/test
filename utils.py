def inject_custom_css():
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
    st.markdown(custom_css, unsafe_allow_html=True)
