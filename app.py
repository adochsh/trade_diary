import streamlit as st
from multiapp import MultiApp
# import your app modules here
from apps import main, analysis

st.set_page_config(page_title="Trade diary", page_icon="📉", layout="centered")

app = MultiApp()
# Add all your application here
app.add_app("Main Page", main.app)
app.add_app("Analysis", analysis.app)





# The main app
app.run()
