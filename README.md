# Repo for the 'Artificial Neural Networks and Deep Learning' course (2019/2020)

This repository contains the python notebooks that were employed in 3 Kaggle challenges that were proposed during the course.
The datasets that were used in each of the challenge are contained in a separate repo which is imported as a submodule.
Artificial Neural Networks have shown impressing results in a broad range of application domains. The challenges are nothing else than a set of problems taken from image processing. The order in which they were presented was set to progressively increase the complexity of the tasks.

The repo is organzed as follow:
 
[DL-CompetitionsDatasets](DL-CompetitionsDatasets),       contains the datasets;

[dataSetStatistics.py](dataSetStatistics.py),             was used to evaluate some characteristics of the datasets;

[image_classification.ipynb](image_classification.ipynb), python notebook for the first  challenge;

[image_segmentation.ipynb](image_segmentation.ipynb),     python notebook for the second challenge;

[question_answering.ipynb](question_answering.ipynb),     python notebook for the third  challenge;

[resize_on_disk.ipynb](resize_on_disk.ipynb),             python notebook to transform the dataset of the third challenge;

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
   This was the most difficult challenge we faced. In this task the network takes two inputs: i) a synthetic scene in which are presented several objects with different geometric shapes and/or finishes (colour, material) ii) and a question about the existence of something in the scene (e.g., Is there a yellow thing?') or about counting (e.g., How many big objects are there?'). The network has to produce a suitable answer by choosing between a set of predefined sentence: yes, no, 0, 1, ..., 9. So in a certain sense, it can be seen as a classification problem. 
   
   An example.
   |----|   
   | ![example](https://www.googleapis.com/download/storage/v1/b/kaggle-user-content/o/inbox%2F3311561%2F25ee0570e55dd0f702a2c07887453269%2Fvqa_ex1.png?generation=1576719696601958&alt=media) |
   | Q: What number of other matte objects are the same shape as the small rubber object? |
   | A: 1 |
    
   Even if the challenge was a subset of [CLEVR](https://cs.stanford.edu/people/jcjohns/clevr/), the dataset was huge : more than 12 GB. 
   As a consequence, the first thing we did was to accelerate the training procedure (a batch of 64 elements took 2 seconds to be processed). After reading [A simple neural network module for relational reasoning](https://arxiv.org/pdf/1706.01427.pdf), it became clear that the task could be solved using images with lower resolution. In this way, we were able to reduce by around 8 times the time taken to process a batch and this allows to exploit more efficient caching mechanisms.
   
   The basic architecture that we used was a combination of three NNs. A CNN processed the image, while embedding + LSTM examined the question. The two outputs were then transformed by a dense layer to output a 1-hot encoded answer.
   
   We have tried several approach: tackling with different networks counting and boolean questions, GRU, different pre-trained feature extractors, pretrained word embedding, attention mechanisms and we designed a custom data generator to provide evenly distributed batches.
   
   For more information on the competition or in the techniques applied take a look on the two links below.

   [to the Kaggle competition](https://www.kaggle.com/c/ann-and-dl-vqa); [notebook](./question_answering.ipynb) 
