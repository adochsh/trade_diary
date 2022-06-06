import streamlit as st
import numpy as np
import pandas as pd
from data.create_data import create_table

def app():
    st.title('customs_docs')

    st.write("This is a sample customs_docs in the mutliapp.")
    st.write("See `apps/customs_docs.py` to know how to use it.")

    st.markdown("### Plot Data")
    # df = create_table()
    df = pd.DataFrame({"x": range(1, 11), "y": 7})
    df['x*y'] = df.x * df.y

    st.line_chart(df)
