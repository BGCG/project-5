import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from src.data_management import download_dataframe_as_csv
from src.machine_learning.predictive_analysis import (
    load_model_and_predict,
    resize_input_image,
    plot_prediction_probabilities
)


def page_powdery_mildew_predictor():

    st.info(
        f"* The client is interested in determining whether a given leaf is "
        f"infected with Powdery Mildew or not."
    )

    st.write(
        f"You can download a set of healthy and powdery mildew infected "
        f"leaf images for live predictions from here"
    )

    st.write("---")

    images_buffer = st.file_uploader('Upload your cherry leaf imagges here (multiple image uploads allowed)',
                                     type="jpg", accept_multiple_files=True)

    if images_buffer is not None:
        columns = ["Name", "Result"]
        df_report = pd.DataFrame(columns=columns)
        df = []
        for image in images_buffer:

            img_pil = (Image.open(image))
            st.info(f"Cherry leaf sample: {image.name}")
            img_array = np.array(img_pil)
            st.image(img_pil, caption=f"Image size: {img_array.shape[1]}px width x {img_array.shape[0]}px height")

            version = "v1"
            resized_image = resize_input_image(img=img_pil, version=version)
            pred_proba, predicted_class = load_model_and_predict(resized_image, version=version)
            plot_prediction_probabilities(pred_proba, predicted_class)

            new_data = {"Name":image.name, "Result": predicted_class}

            df_report.loc[0] = new_data

            if not df_report.empty:
                st.success("Analysis report")
                st.table(df_report)
                st.markdown(download_dataframe_as_csv(df_report), unsafe_allow_html=True)