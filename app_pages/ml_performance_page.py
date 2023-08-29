import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.image import imread
from src.machine_learning.evaluate_clf import load_test_evaluation


def page_ml_performance_metrics():
    """
    Render text going through the machine learning performance
    Render the plots describing the machine learning performance
    Load the evaluation pickle so user can see test set evaludaiton accuracy and loss scores
    """

    version = 'v1'

    st.write("Train, Validation and Test set: Label frequencies")

    labels_distribution = plt.imread(
        f"outputs/{version}/labels_distribution.png")
    st.image(labels_distribution,
             caption='Labels distrubution on Train, Valdation and Test sets')
    st.success("Plotting the number of Healthy and Powdery mildew images in train, test and validation sets "
               "showed that the dataset is balanced - with healthy and powdery mildew groups having identical "
               "sample numbers in test, validation and train sets.")
    st.write("---")

    model_acc = plt.imread(f"outputs/{version}/model_training_acc.png")
    st.image(model_acc, caption='Model Training accuracy')
    st.success("Plotting the accuracy during each successive iteration during model training showed that accuracy increased overall while training. "
               "This trend suggests that the model is fine-tuning it's parameters to fit the training data better. The validation results showed "
               "the validation result accuracy scores mirrored those of the training set, suggestive that the model is generalising well to "
               "unseen data and is capturing underlying patterns rather than just memorising the training examples.")

    model_loss = plt.imread(f"outputs/{version}/model_training_loss.png")
    st.image(model_loss, caption="Model Training losses")
    st.success("Plotting of loss during each successive iteration during model training showed that loss decreased over while training, "
               "suggestive that the model is adjusting it parameters to fit the training data and is improving it's ability to detect "
               "patterns in the train data and reduce errors. Additionally, the validation loss also decreasing in a similar "
               "fashion to that seen in the training data suggestive that the model is generalising well to unseen data.")

    conf_matrix = plt.imread(f"outputs/{version}/conf_matrix.png")
    st.image(conf_matrix, caption="Confusion matrix")
    st.success("The confusion matrix is used to determine the performance of a classification model, by plotting the actual class against the "
               "predicted class in a tabular format. In a confusion matrix, the predictions are categorised as follows: true positive, "
               "false positive, true negative, false negative. The confusion matrix of the test set results showed that there are minimal false positives "
               "and false negatives, suggestive of good overall model performance.")

    roc_plot = plt.imread(f"outputs/{version}/roc_plot.png")
    st.image(roc_plot, caption="ROC plot")
    st.success("The ROC plot is a plot to evaludation the models ability to accurately distinguish between classes by plotting the false positive"
               "rate by the true positive rate. Plotting the false positive rate by the true positive rate suggested the model is very good at "
               "predicting the positive class, as the false positive rate was consistently near 0 and the true positive rate consistently close to 1."
               " The AUC, which is used to summarise the overall perfromance, was 1.0 suggestive that the model is good a distinguishing between classes.")

    prec_recall_plot = plt.imread(
        f"outputs/{version}/precision_recall_plot.png")
    st.image(prec_recall_plot, caption="Precision-recall plot")
    st.success("The precision recall plot represents the ratio of true positive predictions over all positive predictions in the model versus the true positive predictions "
               "over all positive instances in the dataset. The plot shows that the model is good at predicting positive instances in the test set while also maintaining precision.")

    st.write("---")

    st.write("### Performance on Test Set")
    st.dataframe(pd.DataFrame(load_test_evaluation(
        version), index=['Loss', 'Accuracy']))
    st.success("The model evaluation on the test set showed that we have met our clients expectations - where we have achieved an accuracy score of 99.2%")

    st.write(
        f"For additional information, please read this projects readme file\n"
        f"[Project README file](https://github.com/BGCG/project-5/tree/main)\n"
    )
