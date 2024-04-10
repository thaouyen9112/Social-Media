import streamlit as st
import pandas as pd
import altair as alt

@st.cache_data  # 👈 Add the caching decorator
def load_data(csv):
    df = pd.read_csv(csv)
    return df

media = load_data("data/social_media.csv")

st.write(media)