import streamlit as st
import pandas as pd

st.set_page_config(page_title= 'Home', layout= 'wide')

st.image('images.jpeg')

html ="""
    <div style="text-align: center; color: #FF4B4B; font-size: 30px; font-weight: bold;">
        Epsilon Amr Ecommerce Mid project
    </div>
    """
st.markdown(html, unsafe_allow_html= True)

# Load Data
df = pd.read_parquet('cleaned_data.parquet')

# Show sample of data
st.subheader('Data Overview')
st.dataframe(df)


