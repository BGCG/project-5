import streamlit as st
import matplotlib.pyplot as plt

def page_summary():

    st.write("### Project summary")

    st.info(
        f"Background information\n"
        f"Powdery mildew is a fungal infection which effects multiple different flower and fruit plants including the cherry plant\n"
    )

    st.success(
        f"The project has 2 buisness requirements\n"
        f"* 1 - The client would is interested to have a study to visually differentiate a cherry leaf infected with powdery mildew or not.\n"
        f"* 2 - An machine learning model to predict whether a partiuclar leaf is infected by powdery mildew or not.\n"
    )

    st.write(
        f"For additional information, please read this projects readme file\n"
        f"[Project README file](https://github.com/BGCG/project-5/tree/main)\n"
    )