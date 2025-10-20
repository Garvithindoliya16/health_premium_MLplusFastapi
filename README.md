🧮 Insurance Premium Prediction System

A complete Machine Learning Web Application built with FastAPI (backend) and Streamlit (frontend) to predict the insurance premium category for users based on health, lifestyle, and demographic factors.

🚀 Project Overview

This project provides:

🧠 ML Model trained to classify insurance premium categories (Low, Medium, High).

⚡ FastAPI Backend for serving predictions via REST API.

💻 Streamlit Frontend for an interactive user interface.

🔍 Health check endpoint for deployment readiness (useful for AWS, Docker, etc.).

✅ Automatic feature computation (BMI, age group, lifestyle risk, city tier).

🧠 Tech Stack
Layer	Technology
Frontend	Streamlit
Backend	FastAPI
Modeling	scikit-learn
Data Processing	Pandas, NumPy
Validation	Pydantic
Server	Uvicorn
📂 Project Structure
.
├── main.py                        # FastAPI backend
├── model/
│   ├── model.pkl                  # Trained ML model file
│   └── predict.py                 # Model loading & prediction logic
├── schema/
│   ├── user_input.py              # Input data validation schema
│   └── prediction_response.py     # Response schema
├── config/
│   └── city_tier.py               # City tier classification
├── frontend/
│   └── app.py                     # Streamlit UI (frontend)
├── requirements.txt               # Dependencies
└── README.md                      # Documentation

⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>

2️⃣ Create a Virtual Environment
python -m venv fastAPI
source fastAPI/Scripts/activate   # For Windows
# or
source fastAPI/bin/activate       # For macOS/Linux

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the FastAPI Backend
uvicorn main:app --reload


✅ You should see:

Uvicorn running on http://127.0.0.1:8000

5️⃣ Run the Streamlit Frontend
streamlit run frontend/app.py


Then open the URL displayed in your terminal (usually http://localhost:8501).

🌐 API Endpoints
1. Root Endpoint

GET /

{
  "Message": "Insurance Premium Prediction API"
}

2. Health Check

GET /health

{
  "status": "OK",
  "Version": "1.0.0",
  "model_loaded": true
}

3. Predict Premium Category

POST /predict

Example Request:
{
  "age": 35,
  "weight": 72.5,
  "height": 1.75,
  "income_lpa": 10,
  "smoker": false,
  "city": "Delhi",
  "occupation": "private_job"
}

Example Response:
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

🧩 Streamlit Frontend Interface
Features:

Form-based data input (age, height, weight, city, income, etc.)

Automatic request to FastAPI backend.

Displays:

Predicted premium category

Model confidence score

Probability distribution across categories

Example Screenshot:

(Add screenshot of your Streamlit UI here)

🧮 Computed Features (Handled Automatically)
Feature	Formula / Logic	Example
BMI	weight / (height²)	24.2
Age Group	<25: young, <45: adult, <60: middle_aged, else: senior	adult
Lifestyle Risk	Based on smoking & BMI (>30 high, >27 medium, else low)	medium
City Tier	From config file (Tier 1, Tier 2, Tier 3)	1
🧩 Requirements File

Here’s the complete list of dependencies used:

altair==5.5.0
annotated-types==0.7.0
anyio==4.11.0
attrs==25.4.0
blinker==1.9.0
cachetools==6.2.1
certifi==2025.10.5
charset-normalizer==3.4.4
click==8.3.0
colorama==0.4.6
fastapi==0.119.0
gitdb==4.0.12
GitPython==3.1.45
h11==0.16.0
idna==3.11
Jinja2==3.1.6
joblib==1.5.2
jsonschema==4.25.1
jsonschema-specifications==2025.9.1
MarkupSafe==3.0.3
narwhals==2.8.0
numpy==2.3.4
packaging==25.0
pandas==2.3.3
pillow==11.3.0
protobuf==6.33.0
pyarrow==21.0.0
pydantic==2.12.3
pydantic_core==2.41.4
pydeck==0.9.1
pydentic==0.0.1.dev3
python-dateutil==2.9.0.post0
python-stdnum==2.1
pytz==2025.2
referencing==0.37.0
requests==2.32.5
rpds-py==0.27.1
scikit-learn==1.7.2
scipy==1.16.2
six==1.17.0
smmap==5.0.2
sniffio==1.3.1
starlette==0.48.0
streamlit==1.50.0
tenacity==9.1.2
threadpoolctl==3.6.0
toml==0.10.2
tornado==6.5.2
typing-inspection==0.4.2
typing_extensions==4.15.0
tzdata==2025.2
urllib3==2.5.0
uvicorn==0.38.0
watchdog==6.0.0
