import streamlit as st
import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.image import imread

import itertools
import random

def leaves_visualiser_body():
    st.write("### Leaves visualiser")
    st.info(
        f"The client would is interested to have a study to visually\n"
        f"differentiate a cherry leaf infected with powdery mildew or not."
    )

    version = "v1"
    if st.checkbox("Difference between average and variability image"):

        avg_powdery_mildew = plt.imread(f"outputs/{version}/avg_var_powdery_mildew.png")
        avg_healthy = plt.imread(f"outputs/{version}/avg_var_healthy.png")

        st.warning(
            f"A small difference in color pigment was observed between healthy and powdery mildew infected leaves"
        )

        st.image(avg_powdery_mildew, caption="Powdery mildew leaves - Average and Variability")
        st.image(avg_healthy, caption="Healthy leaves - Average and Variability")
        st.write("---")

    
    if st.checkbox("Differences between average powdery mildew and healthy leaves"):
        diff_bet_avgs = plt.imread(f"outputs/{version}/avg_diff.png")

        st.warning(
            'We observed a slight difference between the average images of powdery mildew and healthy leaves'
        )

        st.image(diff_bet_avgs, caption="Difference between average images")

    if st.checkbox("Image montage"):
        st.write("* To refresh the montage, click on the 'Create Montage' button")
        data_dir = 'inputs/cherry_leaves_dataset/cherry-leaves'
        labels = os.listdir(data_dir+'/validation')
        label_to_display = st.selectbox(label="Select label", options=labels, index=0)
        if st.button("Create Montage"):
            image_montage(data_dir+'/validation', presented_label=label_to_display, num_rows=8, num_cols=3, figsize=(10,25))
            st.write("---")

def image_montage(dir_path, presented_label, num_rows, num_cols, figsize=(15,10)):

    """
    Check if label exists in specified directory
    Check if size of montage exceeds the subset size
    Generate a list of axes indices based on subset size
    Loop through images and plot them 
    Limit the number of images plotted by predefined size of figure
    """
    
    fig_grid = num_rows * num_cols
    labels = os.listdir(dir_path)

    if presented_label in labels:
        img_lst = os.listdir(dir_path + '/' + presented_label)
         
        if fig_grid < len(img_lst):
            # select random image
            img_idx = np.random.choice(img_lst, num_rows * num_cols)
            
        else:
            print(f'There are {len(img_lst)} in your subset..\n'
                  f'but you requested a montage with {nrows * ncols} spaces. \n'
                  f'Decrease your number of cols or number of rows in your requested montage')
            return
        
        # create list of axes indices based on num_rows and num_cols
        lst_rows = range(0, num_rows)
        lst_cols = range(0, num_cols)
        plot_idx = list(itertools.product(lst_rows,lst_cols))

        # create plot and display images
        fig, axes = plt.subplots(nrows=num_rows, ncols=num_cols, figsize=figsize)
    
        for x in range(0, fig_grid):
            img = imread(dir_path + '/' + presented_label + '/' + img_idx[x])
            img_shape = img.shape
            axes[plot_idx[x][0], plot_idx[x][1]].imshow(img)
            axes[plot_idx[x][0], plot_idx[x][1]].set_title(f"Width {img_shape[1]}px x Height {img_shape[0]}px")
            axes[plot_idx[x][0], plot_idx[x][1]].set_xticks([])
            axes[plot_idx[x][0], plot_idx[x][1]].set_yticks([])
        plt.tight_layout()
        st.pyplot(fig=fig)
        # plt.show()

    else:
        print("The label you selected doesn't exist")
        print(f"Label options are: {labels}")
        return
