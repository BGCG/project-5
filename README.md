### Powdery mildew predictor

#### Introduction

Powdery mildew is a fungal infection that affects a wide range of plants, including the cherry plant. Infection with powdery mildew can cause a white or grayish coating on the leaves of infected plants and sometimes the fruit. The fungus spreads through airborne spores and thrives in humid conditions.
Infection of plants with powdery mildew can negatively affect the overall functioning of the plant, including disrupting photosynthesis. This can result in stunting of growth of the plant as well as overall quality and yield of the fruit. 

Powdery mildew can spread easily between infected plants via physical contact with infected plants or fungal airborne spores. Therefore, early detection of powdery mildew infection is vital to preserve the overall quality of the crop.

Our client, a cherry farmer, is interested in creating a tool to accurately detect whether a cherry leaf is infected with powdery mildew or not in order to allow effective infection monitoring of their crops.

We have developed a machine learning tool to predict whether a cherry leaf is infected with powdery mildew or not. The tool has been deployed and can be accessed by following this [link](https://powdery-mildew-predictor-1becb7613bb9.herokuapp.com/).

We followed the Cross-industry Standard process for Data-Mining (CRISP-DM) structure frameworks to guide our steps involved in this machine learning project.

### Business case / understanding

Our client is a cherry farmer who has been having issues with their cherry crops being infected with the fungus, Powdery Mildew. Their farm employees spend approximately 30 minutes per cherry tree checking if the leaves show signs of infection. As this is a strain on the time resources of the employees and infection of the cherry tree with powdery mildew can impact the quality and yield of the product, the client would like to explore more time-effective methods to determine whether cherry leaves are infected with powdery mildew or not.

The business requirements are:
1. The client would like us to conduct a study to visually differentiate between a cherry plant infected with powdery mildew and one that is not.
2. The client would like to be able to detect whether a cherry leaf is infected with powdery mildew or not.

The business case can be broken down into the following user stories:
* As a client, I would like to see a study comparing the leaves infected with powdery mildew or not so I can see if there are any discriminatory features between the two groups.
* As a client, I would like to be able to evaluation the model performance by seeing a summary of the performance of the model on test set data so I can determine whether the study has met my business requirements
* As a client, I would like a tool to allow me to make live predictions on cherry leaf images so I can accurately detect whether they have powdery mildew or not
* As a client, I would like to be able to download a report so I can easily have a summary of the prediction probability result of each leaf so I can use this for the infection monitoring of my farm.

### Dataset composition 
The dataset consisted of 2104 images of cherry leaves that were infected with powdery mildew and 2104 images of cherry leaves that were healthy. The dataset was downloaded from [Kaggle](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves).

### Data preparation 
Non-image files from cherry leaves image dataset were removed and image files were split the images into train, validation and test in a 7:2:1 ratio.

### Modeling

#### Hypothesis and validation

###### Hypothesis 1: Cherry leaves infected with powdery mildew can be visually distinguished from those that are not infected

Validation: As per the clients requests, we carried our study to see if a cherry leaf was infected with powdery mildew and those that are not, to determine whether there are any visual differences between the two groups. Plotting of an image montage showed that cherry leaves infected with powdery mildew showed that those affected with powdery mildew had white blemishes in the middle of the leaf and the leaf had a shriveled appearance.

Analysis of the average images and variability images in powdery mildew and unaffected leaves showed again that powdery mildews had more white stripes in the middle and inside the leaf body.

However, the difference between the average infected leaf and noninfected leaf showed no clear differences between the two groups. This confirmed that this problem can’t be solved with data analytics alone and that we require a more complex tool to allow us to distinguish between a leaf infected with powdery mildew and one that is not.

###### Hypothesis 2: Providing a dropout layer in the hidden layer of the network improve prediction accuracy

Validation: In our initial work, the network could make highly accurate predictions on the validation dataset (accuracy score on last epoch when evaluating validation set: 99.7%) when using the adam optimiser. However, when evaluating the test data, the accuracy score reduced to 87% - suggestive of overfitting of the model. Therefore, in order to make the job harder to learn from the train data to provide a more steady but accurate pace of learning, I decided to put in a dropout layer in the hidden layer to deactivate a randomly set of neurons to improve the network’s generalisation ability. This in combination with other regularisation techniques (such as image augmentation) resulted in an accuracy score of 99.2% when the model was evaluation on test data.

###### Hypothesis 3: Adjusting the height and width shift range will improve model performance on test set

Validation: To further address the issue of the model not being to generalise well enough on test data, I also decided to augment the images to make it more challenging for the model to find patterns while training to ultimately make the model more robust. This exposed the model to different scenarios and would improve its robustness in real world citation, i.e. say in future if the farmer had some images where part of the leaf was not present in the full image. If the model wasn’t prepared for images with reduced information, the model could make inaccurate predictions. I found setting the height and width shift range from 0.1 to 0.2 in the image augmentation parameters custom function and then apply these augmentation to the train set images contributed to an increase in model performance when performing the binary classification task as this could result in parts of the leaf in the image to be cut off and therefore making the data more challenging for the network to learn patterns from.

##### Hypothesis 4: Usage of the adam optimiser over adagrad optimiser improves model performance

Validation: We initially explored the usage of different optimisers to determine what would lead to the best performance, while also reducing the change of overfitting. Usage of the adagrad optimiser results in a slow and steady increase in accuracy score but ultimately when the data was exposed to the test set, the accuracy dropped to 80%. We initially explored the `adagrad` optimiser to address concerns about model overfitting. However, following these findings we decided it would be best to explore different optimisers. The `adam` optimiser is popular as it utilises a combination of adaptive learning rates with momentum which can result in higher learning rates. However, increased learning rates in training does not necessarily mean that there is better model performance on test data. I initially found that without using regularisation techniques such as internal drop out layers and image augmentation, we still got reduced accuracy on the test set (89%). Therefore, we found usage of the regularisation techniques outlined above (dropout and image augmentation) to challenge the model, in addition to usage of the `adam` optimiser resulted in an increased accuracy score (99.2%) when evaluating the model performance on the test set.
