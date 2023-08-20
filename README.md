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

