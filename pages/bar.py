import streamlit as st
import pandas as pd
import altair as alt
import seaborn as sns
import matplotlib.pyplot as plt

@st.cache_data  
def load_data(csv):
    df = pd.read_csv(csv)
    return df

media = load_data("data/social_media.csv")

fig = plt.figure(figsize=(10, 4))
sns.countplot(x="platform", hue="gender", data=media)

st.pyplot(fig)

sns.countplot(media, x="platform", hue="gender")
plt.show()
