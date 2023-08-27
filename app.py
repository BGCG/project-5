import streamlit as st
from app_pages.multipage import Multipage

# load scripts
from app_pages.page_summary import page_summary
from app_pages.leaves_visualiser_page import leaves_visualiser_body
from app_pages.project_hypothesis_page import page_project_hypothesis_body
from app_pages.ml_performance_page import page_ml_performance_metrics
from app_pages.live_predictor import page_powdery_mildew_predictor

# Create instance of the app
app = Multipage(app_name="Powdery mildew predictor")

# Add your app pages below using add_page()
app.add_page("Project summary", page_summary)
app.add_page("Leaf visualiser", leaves_visualiser_body)
app.add_page("Project hypothesis", page_project_hypothesis_body)
app.add_page("ML performance", page_ml_performance_metrics)
app.add_page("Live powdery mildew predictor", page_powdery_mildew_predictor)

# run app
app.run()
