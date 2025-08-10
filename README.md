# 🌳 Decision Tree Diabetes Progression Predictor

## 📌 About
Decision Tree Regression is a non-linear model that predicts a target variable by splitting the dataset into branches based on feature values. It uses if-else rules to form a tree structure, where each leaf node represents a predicted value, making it easy to interpret and visualize.

## 📂 Project Structure
```
├── model.py        # Trains the Decision Tree model on the Diabetes dataset
├── app.py          # Flask app to serve predictions
├── templates/
│   └── index.html  # Interactive UI for user input
├── decision_tree_diabetes.pkl  # Saved model file
└── requirements.txt # Project dependencies
```

## 📊 Dataset
We use the Diabetes dataset from `sklearn.datasets`, which contains medical details to predict disease progression.

**Features used:**
- Age (years)
- BMI (kg/m²)
- Blood Pressure (mm Hg)
- S5 Serum Measurement (lab test)
- S1 Serum Measurement (lab test)

**Target:** A quantitative measure of diabetes progression one year after baseline.

## 🚀 How to Run
1. Clone this repository
2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```
3. Train the model (optional, already trained in repo)
   ```bash
   python model.py
   ```
4. Run the Flask app
   ```bash
   python app.py
   ```
5. Open browser and go to: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## 📦 Requirements
- Flask
- scikit-learn
- pandas
- numpy
- joblib


## 🖼️ Screenshots
<img width="1366" height="640" alt="Screenshot 2025-08-10 230358" src="https://github.com/user-attachments/assets/2cca37b6-7d55-4575-a301-98c05b3550d3" />
<img width="1366" height="647" alt="Screenshot 2025-08-10 230435" src="https://github.com/user-attachments/assets/a6ee3909-66d1-4529-9589-8d3e750bf806" />
<img width="1366" height="644" alt="Screenshot 2025-08-10 230446" src="https://github.com/user-attachments/assets/1a077cea-6428-4f1d-b94f-b8fb0e6054c3" />

