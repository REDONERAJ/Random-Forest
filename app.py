from flask import Flask, render_template, request
import joblib
import numpy as np
from sklearn.datasets import load_breast_cancer

app = Flask(__name__)
model = joblib.load('random_forest_breast_cancer.pkl')

selected_features = [
    "mean radius",
    "mean texture",
    "mean perimeter",
    "mean area",
    "mean smoothness",
    "mean compactness"
]

placeholder_values = {
    "mean radius": 14.2,
    "mean texture": 20.1,
    "mean perimeter": 92.0,
    "mean area": 654.5,
    "mean smoothness": 0.095,
    "mean compactness": 0.084
}

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        inputs = [float(request.form[f]) for f in selected_features]

        cancer = load_breast_cancer()
        mean_values = cancer.data.mean(axis=0)
        feature_vector = mean_values.copy()

        for i, feat in enumerate(selected_features):
            idx = list(cancer.feature_names).index(feat)
            feature_vector[idx] = inputs[i]
            
        pred = model.predict([feature_vector])[0]
        prediction = "Malignant" if pred == 0 else "Benign"

    return render_template(
        'index.html',
        features=selected_features,
        placeholders=placeholder_values,
        prediction=prediction
    )

if __name__ == '__main__':
    app.run(debug=True)
