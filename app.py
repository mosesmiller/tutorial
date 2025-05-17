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

# Sidebar button navigation
st.sidebar.title("Select a Plot")
plot_selected = None

if st.sidebar.button("📊 Flipper Length Distribution"):
    plot_selected = "flipper"
elif st.sidebar.button("📦 Body Mass by Species"):
    plot_selected = "body_mass"
elif st.sidebar.button("📐 Bill Dimensions Scatterplot"):
    plot_selected = "bill_dims"

# Plot 1: Flipper Length Distribution
if plot_selected == "flipper":
    st.subheader("Distribution of Flipper Length (mm)")
    st.markdown("This plot shows the distribution of penguin flipper lengths. It helps us understand the common sizes and variability within the species.")
    fig, ax = plt.subplots()
    sns.histplot(df['flipper_length_mm'], kde=True, color='teal', ax=ax)
    ax.set_xlabel("Flipper Length (mm)")
    ax.set_ylabel("Frequency")
    st.pyplot(fig)

# Plot 2: Body Mass by Species
elif plot_selected == "body_mass":
    st.subheader("Body Mass by Penguin Species")
    st.markdown("This boxplot displays the spread and central tendency of body mass across different penguin species. Useful for comparing typical sizes.")
    fig, ax = plt.subplots()
    sns.boxplot(x='species', y='body_mass_g', data=df, palette='Set2', ax=ax)
    ax.set_xlabel("Species")
    ax.set_ylabel("Body Mass (g)")
    st.pyplot(fig)

# Plot 3: Bill Dimensions Scatterplot
elif plot_selected == "bill_dims":
    st.subheader("Bill Length vs Depth by Species and Sex")
    st.markdown("This scatterplot explores the relationship between bill length and depth, color-coded by species and shaped by sex.")
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

# Default message if no plot selected yet
if plot_selected is None:
    st.info("👈 Use the buttons on the left to select a plot to display.")

# Optional data viewer
with st.expander("📄 Show raw data"):
    st.dataframe(df)
