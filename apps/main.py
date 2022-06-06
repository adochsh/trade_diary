import streamlit as st
import numpy as np
import pandas as pd
import datetime
from gsheetsdb import connect

#@st.cache(suppress_st_warning=True)

def app():
    st.header('Main !Page')


st.sidebar.header("Filters:")
# Identifier
with st.sidebar.expander("Identifier", expanded=False):
    # articles = {"LM code , ADEO code , EAN"}
    articles_join = []
    articles = st.multiselect("heyo", articles_join)
