import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Set the Streamlit page config
st.set_page_config(page_title="Penguin Data Explorer", layout="centered")

st.title("🐧 Penguin Data Explorer")

# Load dataset with fallback
@st.cache_data
def load_data():
    try:
        df = sns.load_dataset("penguins")
    except:
        url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv"
        df = pd.read_csv(url)
    return df.dropna()

df = load_data()

# Sidebar plot selector
plot_type = st.sidebar.selectbox(
    "Choose a plot to display:",
    ["Flipper Length Distribution", "Body Mass by Species", "Bill Dimensions Scatterplot"]
)

# Plot 1: Flipper Length Distribution
if plot_type == "Flipper Length Distribution":
    st.subheader("Distribution of Flipper Length (mm)")
    fig, ax = plt.subplots()
    sns.histplot(df['flipper_length_mm'], kde=True, color='teal', ax=ax)
    ax.set_xlabel("Flipper Length (mm)")
    ax.set_ylabel("Frequency")
    st.pyplot(fig)

# Plot 2: Body Mass by Species
elif plot_type == "Body Mass by Species":
    st.subheader("Body Mass by Penguin Species")
    fig, ax = plt.subplots()
    sns.boxplot(x='species', y='body_mass_g', data=df, palette='Set2', ax=ax)
    ax.set_xlabel("Species")
    ax.set_ylabel("Body Mass (g)")
    st.pyplot(fig)

# Plot 3: Bill Dimensions Scatterplot
elif plot_type == "Bill Dimensions Scatterplot":
    st.subheader("Bill Length vs Depth by Species and Sex")
    fig, ax = plt.subplots()
    sns.scatterplot(
        data=df,
        x='bill_length_mm',
        y='bill_depth_mm',
        hue='species',
        style='sex',
        ax=ax
    )
    ax.set_xlabel("Bill Length (mm)")
    ax.set_ylabel("Bill Depth (mm)")
    st.pyplot(fig)

# Optional data viewer
with st.expander("📄 Show raw data"):
    st.dataframe(df)
