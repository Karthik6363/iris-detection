# iris-detection

#  Flower Detection Web App

A full-stack web application for detecting different types of flowers using a trained machine learning model. The app is built with a **Flask** backend and a **responsive HTML/CSS/JS** frontend.

##  Features

- Upload or capture flower images
- Predicts the flower type in real time
- Backend powered by Flask + ML model
- Clean and simple web interface

##  Tech Stack

- Python
- Flask
- HTML5, CSS3, JavaScript
- Machine Learning (e.g., Scikit-learn / TensorFlow / OpenCV)
- Machine Learning: **KNN (K-Nearest Neighbors)**
- Jupyter Notebook (used for model training)

##  Model Training

The flower classification model was trained using **KNN (K-Nearest Neighbors)** algorithm inside a **Jupyter Notebook** environment. The dataset was preprocessed, split into training/testing sets, and the model was trained and evaluated before being saved as `flower_model.pkl` for integration into the Flask backend


karthik/
├── static/
│   ├── css/
│   └── js/
├── templates/
│   └── index.html
├── model/
│   └── flower_model.pkl
├── app.py
├── model_training.ipynb
├── requirements.txt
└── README.md

 
##  Install Python dependencies

- pip install -r requirements.txt


##  How to Run
- python app.py

- 
### 1️ Clone this repository
```bash
git clone https://github.com/Karthik6363/karthik.git
cd karthik
