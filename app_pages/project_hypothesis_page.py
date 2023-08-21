import streamlit as st
import matplotlib.pyplot as plt


def page_project_hypothesis_body():

    """
    Render text describing project hypothesis to provide information to the user about the
    purpose of the page
    """

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

    st.info(
        f"As the visualisation of the cherry leaves suggested there was no prominent discernable"
        f" features that could tell if a cherry leaf was infected with powdery mildew or not, "
        f"we decided that a classification tool would be the best route forward to fulfill the client's request."
        f"Since the prediction outcome would fall into one of two categories (healthy or powdery mildew infection), "
        f"we decided creation of a binary classification algorithm would be the best approach to build our prediction tool."
    )
