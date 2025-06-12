from flask import Flask, render_template, request, url_for
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained KNN model
with open('knn_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Dictionary to map species index to name and image
species_map = {
    0: {"name": "Setosa", "image": "setosa.jpg"},
    1: {"name": "Versicolor", "image": "versicolor.jpg"},
    2: {"name": "Virginica", "image": "virginica.jpg"}
}

@app.route('/', methods=['GET', 'POST'])
def predict():
    prediction = None
    confidence = None
    image_url = None

    if request.method == 'POST':
        try:
            # Get input values
            sepal_length = float(request.form['sepal_length'])
            sepal_width = float(request.form['sepal_width'])
            petal_length = float(request.form['petal_length'])
            petal_width = float(request.form['petal_width'])

            # Convert input to NumPy array
            features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])

            # Get probabilities and predicted class
            probabilities = model.predict_proba(features)[0]
            class_index = np.argmax(probabilities)

            # Retrieve species name, confidence, and image path
            prediction = species_map[class_index]["name"]
            image_filename = species_map[class_index]["image"]
            image_url = url_for('static', filename=image_filename)  # Flask dynamic URL
            confidence = round(probabilities[class_index] * 100, 2)

        except ValueError:
            prediction = "Invalid Input! Enter numbers only."
            confidence = None
            image_url = None

    return render_template('index.html', prediction=prediction, confidence=confidence, image_url=image_url)

if __name__ == '__main__':
    app.run(debug=True)
