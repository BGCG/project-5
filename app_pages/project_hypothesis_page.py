import streamlit as st

def page_project_hypothesis_body():
    st.write("### Project Hypothesis and validation")

    st.success(
        f"We suspect that cherry leaves infected with powdery mildew may have "
        f"discernible features that can tell them apart from cherry leaves that are "
        f"not infected. Image montage analysis showed that white blemishes were observed "
        f"on leaves infected with powdery mildew in comparison to those not infected. "
        f"Average Image, Variability image and Difference between images studies did not "
        f"show any explicit pattern that could be used to differentiate a leaf infected "
        f"with powdery mildew to one that is uninfected."

    )