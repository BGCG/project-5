import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.image import imread
from src.machine_learning.evaluate_clf import load_test_evaluation


def page_ml_performance_metrics():
    version = 'v1'

    st.write("Train, Validation and Test set: Label frequencies")

    labels_distribution = plt.imread(f"outputs/{version}/labels_distribution.png")
    st.image(labels_distribution, caption='Labels distrubution on Train, Valdation and Test sets')
    st.write("---")

    model_acc = plt.imread(f"outputs/{version}/model_training_acc.png")
    st.image(model_acc, caption='Model Training accuracy')

    model_loss = plt.imread(f"outputs/{version}/model_training_loss.png")
    st.image(model_loss, caption="Model Training losses")

    conf_matrix = plt.imread(f"outputs/{version}/conf_matrix.png")
    st.image(conf_matrix, caption="Confusion matrix")

    roc_plot = plt.imread(f"outputs/{version}/roc_plot.png")
    st.image(roc_plot, caption="ROC plot")

    prec_recall_plot = plt.imread(f"outputs/{version}/precision_recall_plot.png")
    st.image(prec_recall_plot, caption="Precision-recall plot")

    
    st.write("---")

    st.write("### Performance on Test Set")
    st.dataframe(pd.DataFrame(load_test_evaluation(version), index=['Loss', 'Accuracy']))

    st.write(
        f"For additional information, please read this projects readme file\n"
        f"[Project README file](https://github.com/BGCG/project-5/tree/main)\n"
    )