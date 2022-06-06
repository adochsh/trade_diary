import streamlit as st
from multiapp import MultiApp
# import your app modules here
from apps import main, analysis, smain
app = MultiApp()
st.set_page_config(layout="wide")

# Add all your application here
app.add_app("Main Page", main.app)
app.add_app("Analysis", analysis.app)
app.add_app("bugreport", smain.app)

# The main app
app.run()
