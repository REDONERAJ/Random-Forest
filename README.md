# 🩺 Breast Cancer Diagnosis Predictor (Random Forest + Flask)

This project is a web-based machine learning application that predicts whether a breast lump is **Benign** (non-cancerous) or **Malignant** (cancerous) using a Random Forest Classifier trained on the Breast Cancer Wisconsin Diagnostic dataset from `scikit-learn`.

The app provides a simple, user-friendly form that only requires 6 key tumor features as input, each with example placeholder values for ease of use.

---

## 🚀 Features
- Predicts breast cancer diagnosis using only 6 user-input numeric features
- Random Forest Classifier trained on established dataset
- Responsive Flask web interface
- Example placeholders for user convenience

---

## 📂 Project Structure
```
breast-cancer-diagnosis/
│
├── app.py                               # Main Flask app
├── model.py                             # Model training script
├── breast_cancer_diagnosis_model.pkl    # Saved Random Forest classifier model
├── templates/
│   └── index.html                       # Web interface template
├── requirements.txt                     # Python dependencies
└── README.md                            # Project documentation
```

---

## 📊 Dataset

Uses the **Breast Cancer Wisconsin Diagnostic Dataset** from `scikit-learn`, featuring 30 computed imaging features.

**Prediction target:**
- `0` → Malignant (cancerous)
- `1` → Benign (non-cancerous)

**The web form collects these 6 features:**
- Mean Radius (e.g., 14.2)
- Mean Texture (e.g., 20.1)
- Mean Perimeter (e.g., 92.0)
- Mean Area (e.g., 654.5)
- Mean Smoothness (e.g., 0.095)
- Mean Compactness (e.g., 0.084)

_All others are set to their dataset averages to keep predictions accurate._

---

## 📦 Requirements
- Flask
- scikit-learn
- pandas
- numpy
- joblib

---

## 🖼️ Screenshots
<<<<<<< HEAD
=======
<img width="1366" height="640" alt="Screenshot 2025-08-10 230358" src="https://github.com/user-attachments/assets/2cca37b6-7d55-4575-a301-98c05b3550d3" />
<img width="1366" height="647" alt="Screenshot 2025-08-10 230435" src="https://github.com/user-attachments/assets/a6ee3909-66d1-4529-9589-8d3e750bf806" />
<img width="1366" height="644" alt="Screenshot 2025-08-10 230446" src="https://github.com/user-attachments/assets/1a077cea-6428-4f1d-b94f-b8fb0e6054c3" />
>>>>>>> 4d6afd9cc839dceba63e9c4e574e54403d745385

