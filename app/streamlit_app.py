import streamlit as st;

"""
# My first app
Here's our first attempt at using data to create a table:
change
"""


import numpy as np

dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)