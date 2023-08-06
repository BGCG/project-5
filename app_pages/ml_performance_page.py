import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.image import imread


def page_ml_performance_metrics():
    version = 'v1'

    st.write("Train, Validation and Test set: Label frequencies")

    labels_distribution = plt.imread(f"outputs/{version}/labels_distribution.png")
    st.image(labels_distribution, caption='Labels distrubution on Train, Valdation and Test sets')
    st.write("---")

    col1, col2 = st.beta_columns(2)
    with col1:
        model_acc = plt.imread(f"outputs/{version}/model_training_acc.png")
        st.image(model_acc, caption='Model Training accuracy')
    with col2:
        model_loss = plt.imread(f"outputs/{version}/model_training_acc.png")
        st.image(model_loss, caption="Model Training losses")
    st.write("---")

    st.write("### Performance on Test Set")
    st.dataframe(pd.DataFrame(load_test_evaluation(version), index=['Loss', 'Accuracy']))