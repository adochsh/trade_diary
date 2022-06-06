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

# Create a connection object.
conn = connect()

# Perform SQL query on the Google Sheet.
# Uses st.cache to only rerun when the query changes or after 10 min.
@st.cache(ttl=600)
def run_query(query):
    rows = conn.execute(query, headers=1)
    rows = rows.fetchall()
    return rows

sheet_url = st.secrets["public_gsheets_url"]
# Print results.
for row in rows:
    st.write(f"{row.name} has a :{row.pet}:")
