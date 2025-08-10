# Breast Cancer Diagnosis Predictor (Random Forest + Flask)

This project is a **web-based machine learning application** that predicts whether a breast lump is **Benign** (non-cancerous) or **Malignant** (cancerous) using a **Random Forest Classifier** trained on the **Breast Cancer Wisconsin Diagnostic dataset** from `scikit-learn`.

The app provides a simple, user-friendly form that only requires **6 key tumor features** as input, each with example placeholder values for ease of use.

---

## 🚀 Features
- **Random Forest Classifier** trained on a well-known medical dataset
- Minimal input: only **6 important numeric features**
- Clean and responsive Flask web interface
- Real-time prediction on form submission
- Example placeholders so users don’t need to know valid ranges

---

## 📂 Project Structure

breast-cancer-diagnosis/
│
├── app.py                              # Main Flask app
├── model.py                            # Model training script
├── breast_cancer_diagnosis_model.pkl  # Saved Random Forest classifier model
├── templates/
│   └── index.html                      # Web interface template
├── requirements.txt                    # Python dependencies
└── README.md                          # Project documentation



---

## 📊 Dataset

The app uses the **Breast Cancer Wisconsin Diagnostic Dataset** from `scikit-learn`, which contains **30 numeric features** computed from digitized images of fine needle aspirate (FNA) of a breast mass.  
The prediction target is:
- **0** → Malignant (cancerous)
- **1** → Benign (non-cancerous)

⚠️ For the web form, only 6 of these features are requested from the user:
- Mean Radius (e.g., 14.2)
- Mean Texture (e.g., 20.1)
- Mean Perimeter (e.g., 92.0)
- Mean Area (e.g., 654.5)
- Mean Smoothness (e.g., 0.095)
- Mean Compactness (e.g., 0.084)

The remaining features are filled automatically with dataset mean values to keep predictions accurate.

---

## 🛠 Installation & Usage

### 1️⃣ Clone the repository
git clone https://github.com/your-username/breast-cancer-flask.git
cd breast-cancer-flask


### 2️⃣ Install dependencies
pip install -r requirements.txt


### 3️⃣ Train the model (optional if `.pkl` already included)
python model.py


### 4️⃣ Run the Flask app
python app.py


### 5️⃣ Open in browser
Go to:
http://127.0.0.1:5000


---

## 🖥 Example Prediction
Enter the 6 feature values in the form (examples already in placeholders) and click **"Predict Diagnosis"**.  
You will receive:
- **Benign** → Non-cancerous tumor  
- **Malignant** → Cancerous tumor

---

## 📦 Requirements
Flask
scikit-learn
pandas
numpy
joblib

# Screenshots
<img width="1366" height="640" alt="Screenshot 2025-08-10 230358" src="https://github.com/user-attachments/assets/cb7f64d3-02d5-413e-ab3c-99dba4d9dd98" />
<img width="1366" height="647" alt="Screenshot 2025-08-10 230435" src="https://github.com/user-attachments/assets/a2ca1afb-8b2c-4e01-82bc-8c9363abaa1a" />
<img width="1366" height="644" alt="Screenshot 2025-08-10 230446" src="https://github.com/user-attachments/assets/c37fc148-9eac-4824-b15c-d5b765725152" />

---
