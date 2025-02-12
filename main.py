import streamlit as st
import pandas as pd
import numpy as np


dataUrl = 'dataset\\placement.csv'

# st.title('Placement Insights: Factors Influencing Recruitment')
# st.sidebar.title("Placement Insights")

# st.markdown("This application is a streamlit dashboard to provide insights on the factors influencing recruitment in a college campus placement drive.")


def load_data():
    data = pd.read_csv(dataUrl)
    return data

data = load_data()


