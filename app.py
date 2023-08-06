import streamlit as st
from app_pages.multipage import Multipage

# load scripts
from app_pages.page_summary import page_summary


app = Multipage(app_name="Cherry leaves predictor") # Create instance of the app

# Add your app pages below using add_page()
app.add_page("Project summary", page_summary)

app.run() # run app