# Repo for the 'Artificial Neural Networks and Deep Learning' course (2019/2020)

This repository contains the python notebooks that were employed in 3 Kaggle challenges that were proposed during the course.
Artificial Neural Networks have shown impressing results in a broad range of application domains. The challenges are nothing else than a set of problems taken from image processing. The order in which they were presented was set to progressively increase the complexity of the tasks.

## The challenges 

1. ### Image classification 
   The first competition consists of a classification problem. In an image classification problem, given an image, the goal is to predict the correct class to which the image belongs. The task request to categorize 307 images in 20 different classes. 
   
   In this challenge we have used: Convolutional Neural Netowrks, basic data augmentation techniques (zoom, rotation, horizontal and vertical flip), transfer learning with an without fine tuning ( Resnet, DenseNet201, InceptionV3, InceptionResNetV2, InceptionResNetV2, Xception) and ensembles with K-folding.
   
   For more information on the competition or in the techniques applied take a look on the two links below.
   ![CNN](https://mett29.github.io/images/CNN_wiki.png)
   
   [to the Kaggle competition](https://www.kaggle.com/c/ann-and-dl-image-classification) ; [notebook](./image_classification.ipynb) 

2. ### Aerial image segmentation 
   In this second challenge we were requested to segment an image. Image segmentation can be seen as a classification problem applied to each pixel in the figure provided as input.
   The dataset, that with high probability was a subset of the [Inria dataset](https://project.inria.fr/aerialimagelabeling/), contains aerial ~~orthorectified~~ color images (you can see an example below). The challenge consists in determining which of the pixels belonged to a building.
    
    In this challenge we have used: U-Net models, transfer learning using pretrained networks such as DenseUNet and ResUNet, data augmentation( horizontal/vertical/zoom), preprocessing and postprocessing using techniques taken from image analysis and computer vision ( histogram equalization, Gaussian filters, morphological Transformations provided by OpenCV), we tried to increase the number of channels adding what can be obtained trough Laplacian filter and we tried a custom data augmentation, aimed at enriching the dataset by creating synthetic aerial images
   
   
   For more information on the competition or in the techniques applied take a look on the two links below.
   ![example output/input/ground truth](https://camo.githubusercontent.com/298da53a8079ae2aa109390ded90f884821ad1f2/68747470733a2f2f692e6962622e636f2f76506a306262632f706f6c79676f6e732e706e67)
   
   [to the Kaggle competition](https://www.kaggle.com/c/ann-and-dl-image-segmentation); [notebook](./image_segmentation.ipynb)

3. ### Visual question answering 

  
   For more information on the competition or in the techniques applied take a look on the two links below.
   [to the Kaggle competition](https://www.kaggle.com/c/ann-and-dl-vqa) [noptebook](./question_answering.ipynb)
