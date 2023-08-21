import streamlit as st
import matplotlib.pyplot as plt


def page_summary():

    """
    Render text describing project summary to provide information to the user about the
    purpose of the page
    """

    st.write("### Project summary")

    st.info(
        f"***Background information:***\n"
        f"Powdery mildew is a fungal infection that affects a wide range of plants, including the cherry plant. \n"
        f"Infection with powdery mildew can cause a white or grayish coating on the leaves of infected plants and sometimes the fruit. \n"
        f"The fungus spreads through airborne spores and thrives in humid conditions. Infection of plants with powdery mildew can negatively affect\n"
        f" the overall functioning of the plant, including disrupting photosynthesis. This can result in stunting of growth of the plant as well as overall\n"
        f" quality and yield of the fruit.\n"
        f" Powdery mildew can spread easily between infected plants via physical contact with infected plants or fungal airborne spores. Therefore, early detection\n"
        f" of powdery mildew infection is vital to preserve the overall quality of the crop. \n" 
        f"Our client, a cherry farmer, is interested in creating a tool to accurately detect whether a cherry leaf is infected with powdery mildew or not, \n"
        f"in order to allow effective infection monitoring of their crops."
    )

    st.info(
        f"***Project dataset:***\n"
        f"The dataset was composed of 2104 images of healthy leaves and 2104 images of cherry leaves infected with powdery mildew.\n"
    )

    st.success(
        f"The project has 2 buisness requirements:\n"
        f"* 1 - The client would is interested to have a study to visually differentiate a cherry leaf infected with powdery mildew or not.\n"
        f"* 2 - An machine learning model to predict whether a partiuclar leaf is infected by powdery mildew or not.\n"
    )

    st.write(
        f"For additional information, please read this projects readme file\n"
        f"[Project README file](https://github.com/BGCG/project-5/tree/main)\n"
    )