import pandas as pd
import streamlit as st


#################### START ############################################################################################
def app():
    st.title("📉 Let's analyse your deals history!")

    st.markdown("### Plot Data")
    # df = create_table()
    df = pd.DataFrame({"x": range(1, 11), "y": 7})
    df['x*y'] = df.x * df.y
    st.line_chart(df)
    
    #### See all records from google sheet
    expander = st.expander("See")
    with expander:
        st.line_chart(df)
