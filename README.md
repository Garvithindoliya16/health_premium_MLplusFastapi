# 🧮 Insurance Premium Prediction System

A complete Machine Learning Web Application built with **FastAPI (backend)** and **Streamlit (frontend)** to predict the insurance premium category for users based on health, lifestyle, and demographic factors.

---

## 🚀 Project Overview

This project provides:

- 🧠 **ML Model** trained to classify insurance premium categories (Low, Medium, High)
- ⚡ **FastAPI Backend** for serving predictions via REST API
- 💻 **Streamlit Frontend** for an interactive user interface
- 🔍 **Health check endpoint** for deployment readiness (useful for AWS, Docker, etc.)
- ✅ **Automatic feature computation** (BMI, age group, lifestyle risk, city tier)

---

## 🧠 Tech Stack

| Layer | Technology |
|--------|-------------|
| Frontend | Streamlit |
| Backend | FastAPI |
| Modeling | scikit-learn |
| Data Processing | Pandas, NumPy |
| Validation | Pydantic |
| Server | Uvicorn |

---

## 📂 Project Structure

```
.
├── main.py                  # FastAPI backend
├── model/
│   ├── model.pkl            # Trained ML model file
│   └── predict.py           # Model loading & prediction logic
├── schema/
│   ├── user_input.py        # Input data validation schema
│   └── prediction_response.py # Response schema
├── config/
│   └── city_tier.py         # City tier classification
├── frontend/
│   └── app.py               # Streamlit UI (frontend)
├── requirements.txt          # Dependencies
└── README.md                 # Documentation
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Garvithindoliya16/health_premium_MLplusFastapi.git
cd <repo-health_premium_MLplusFastapi>
```

### 2️⃣ Create a Virtual Environment
```bash
python -m venv fastAPI
source fastAPI/Scripts/activate   # For Windows
# or
source fastAPI/bin/activate       # For macOS/Linux
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the FastAPI Backend
```bash
uvicorn main:app --reload
```
✅ You should see:
```
Uvicorn running on http://127.0.0.1:8000
```

### 5️⃣ Run the Streamlit Frontend
```bash
streamlit run frontend/app.py
```
Then open the URL displayed in your terminal (usually **http://localhost:8501**).

---

## 🌐 API Endpoints

### **Root Endpoint**
**GET /**  
Response:
```json
{ "Message": "Insurance Premium Prediction API" }
```

### **Health Check**
**GET /health**  
Response:
```json
{ "status": "OK", "Version": "1.0.0", "model_loaded": true }
```

### **Predict Premium Category**
**POST /predict**  
Example Request:
```json
{
  "age": 35,
  "weight": 72.5,
  "height": 1.75,
  "income_lpa": 10,
  "smoker": false,
  "city": "Delhi",
  "occupation": "private_job"
}
```
Example Response:
```json
{
  "response": {
    "predicted_category": "Medium",
    "confidence": 0.78,
    "class_probabilities": {
      "Low": 0.12,
      "Medium": 0.78,
      "High": 0.10
    }
  }
}
```

---

## 🧩 Streamlit Frontend Interface

**Features:**
- Form-based data input (age, height, weight, city, income, etc.)
- Automatic request to FastAPI backend
- Displays:
  - Predicted premium category
  - Model confidence score
  - Probability distribution across categories

**Example Screenshot:**
*(Add screenshot of your Streamlit UI here)*

---

## 🧮 Computed Features (Handled Automatically)

| Feature | Formula / Logic | Example |
|----------|----------------|----------|
| BMI | weight / (height²) | 24.2 |
| Age Group | <25: young, <45: adult, <60: middle_aged, else: senior adult | adult |
| Lifestyle Risk | Based on smoking & BMI (>30 high, >27 medium, else low) | medium |
| City Tier | From config file (Tier 1, Tier 2, Tier 3) | 1 |

---

## 🧩 Requirements File

Here’s the complete list of dependencies used:

*(Include only top-level libraries in `requirements.txt`)*
```txt
fastapi
uvicorn
streamlit
pydantic
scikit-learn
pandas
numpy
joblib
```
