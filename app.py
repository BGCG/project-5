import streamlit as st
from app_pages.multipage import Multipage

# load scripts
from app_pages.page_summary import page_summary
from app_pages.leaves_visualiser_page import leaves_visualiser_body

app = Multipage(app_name="Cherry leaves predictor") # Create instance of the app

# Add your app pages below using add_page()
app.add_page("Project summary", page_summary)
app.add_page("Leaf visualiser", leaves_visualiser_body)

app.run() # run app