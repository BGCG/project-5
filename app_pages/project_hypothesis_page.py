import streamlit as st
import matplotlib.pyplot as plt


def page_project_hypothesis_body():

    """
    Render text describing project hypothesis to provide information to the user about the purpose of the page
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

    st.success(
        f"We hypothesised usage of the adam optimiser in our model along with performing regularisation techniques such as"
        f"image augmentation and internal dropout layers in our model, to improve the models ability to generalise, would result"
        f" in the model to meet the clients perfromance goal of 97% accuracy. Our hypothesis was validated as evaluation of the model "
        f"with the test set yeilded a 99.2% accuracy, which met our clients goals."
        f"Therefore, in conclusion we were sucessful in the creation of a machine learning model to predict whether a "
        f" cherry leaf is infected with powdery mildew or not. Further details about the model can be found on the ML "
        f"perfromance page of this dashboard."
    )
