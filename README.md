# SentimentInsight
Sentimental Analysis Model to classify any Input Text as Positive, Negative or Neutral. [LSTM, Flask, TensorFlow]

<h1 align="center">SentimentInsight</h1>

<!-- <div align= "center"><img src="https://i.imgur.com/MfKjyLG.png"/> -->
  
<p>Sentiment Analysis Model built with Flask, Keras/TensorFlow and NLP using LSTM's in order to classify the food items in static images.</p>
</div>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

[![Made withJupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter)](https://jupyter.org/try)
<img src = "https://img.shields.io/badge/Keras-D00000?style=for-the-badge&logo=Keras&logoColor=white"/>
<img src ="https://img.shields.io/badge/scikit_learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white"/>
<img src="https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=TensorFlow&logoColor=white"/>

![Python](https://img.shields.io/badge/python-v3.6+-blue.svg)
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/techyhoney/Facemask_Detection/issues)
[![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/techyhoney/Facemask_Detection/blob/master/LICENSE)


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

![Live Demo](https://github.com/Patil-Ojas/SentimentInsight/blob/main/Sentiment_Analysis_demo.gif?raw=true)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


## :warning: TechStack/framework used

- [TensorFlow](https://www.tensorflow.org/)
- [Keras](https://keras.io/)
- [CNN](https://arxiv.org/abs/1909.09586)
- [Flask](https://flask.palletsprojects.com/en/3.0.x/)


## :file_folder: Dataset
The dataset used can be found here - [Click Here](https://www.kaggle.com/datasets/rabinandan/twitter-sentiment)

This Dataset contains tweets with their corresponding sentiments labelled as 1 (Positive), 0 (Neutral) and -1 (Negative).


## :gear: Prerequisites

All the dependencies and required libraries are included in the file <code>requirements.txt</code> [See here](https://github.com/Patil-Ojas/SentimentInsight/blob/main/requirements.txt)

## 🚀&nbsp; Installation
1. Clone the repo
```
$ git clone https://github.com/Patil-Ojas/SentimentInsight.git
```

2. Change your directory to the cloned repo 
```
$ cd SentimentInsight
```

3. Create a Python virtual environment named 'test' and activate it
```
$ virtualenv test
```
```
$ source test/bin/activate
```

4. Now, run the following command in your Terminal/Command Prompt to install the libraries required
```
$ pip3 install -r requirements.txt
```


<!-- ####          
![](https://i.imgur.com/3vo1w8f.png)

####          

#### We got the following accuracy/loss training curve plots
![](https://i.imgur.com/cLNo6nK.png)
####          
![](https://i.imgur.com/RYiOlCP.png) -->


## Flask app

Run the app.py using the below command to launch SentimenlInsight
```
$ python app.py 
```

## :trophy: Results

#### Our model gave around 71% accuracy for Face Mask Detection after training.
#### Considering humans aren't quite precise at this task themselves, getting 7 out of 10 classifications correct is decent.


## :handshake: Contribution
Feel free to **file a new issue** with a respective title and description on the the [Facemask_Detection](https://github.com/Patil-Ojas/SentimentInsight/issues) repository. If you already found a solution to your problem, **I would love to review your pull request**! 

<!-- Also credits to https://github.com/techyhoney/Facemask_Detection/tree/master for the Readme.md template! -->

## :eyes: License
[MIT](https://github.com/Patil-Ojas/SentimentInsight/blob/main/LICENSE)
