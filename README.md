# 🛡️ Insurance Premium Predictor
Predict the insurance premium category of individuals using a machine learning model with a fully interactive web interface.

This project combines data science, machine learning, API development, and modern UI to deliver a real-world application built using:
<ul>
<li>
    🧠 Scikit-learn for model training
</li><br>
<li>
  ⚙️ FastAPI for building RESTful prediction endpoints
</li><br>
<li>
  🖥️ Streamlit for creating a sleek and interactive user interface
</li><br>
<li>📊 Pandas & Pydantic for data processing and validation
</li>
 <br>
</ul>

---
## 🔍 What This App Does

> Given user inputs like **age**, **BMI**, **smoking habits**, **income**, **occupation**, and **city**,  
the app categorizes the user into an **insurance premium segment** — e.g., **Low**, **Medium**, or **High**.

 The goal is to demonstrate how data can be translated into real-time insights via a machine learning pipeline.

---

### ✨ Key Features
<ul>
<li>End-to-End ML Deployment: From notebook to web interface
</li>
<li>Dynamic Feature Engineering:
  <ul>
<li>BMI calculation
</li>
<li>Lifestyle risk evaluation
</li>
<li>Age group classification
</li>
<li>City tier mapping
</li>
  </ul>
</li>
<li>
Responsive Web Interface: Built with Streamlit and deployable locally or to the cloud
</li>
<li>API-Driven Architecture: Easy to integrate with other apps or systems
</li>
<li>Data Logging: Stores prediction history in a data.json log
</li>
</ul>

---

### 🗂️ Project Structure
```
📁 Insurance-Premium-Predictor/
├── app.py                  # FastAPI backend for ML model serving
├── frontend.py             # Streamlit frontend for user interaction
├── model.pkl               # Trained machine learning model (serialized)
├── insurance.csv           # Dataset used for training
├── Insurance_Predictor.ipynb  # Jupyter Notebook: data prep + model building
├── data.json               # Prediction logs (auto-generated)
├── Requirements.txt
└── README.md               # Project documentation (you're here)
```
---

### 🚀 Getting Started
#### 1️⃣ Clone this repository
git clone [https://github.com/your-username/insurance-premium-predictor.git](https://github.com/Abhaykum123/Insurance-Premium-Predictor)
cd insurance-premium-predictor

---

#### 2️⃣ Set up your environment
```
python -m venv venv
source venv/bin/activate        # macOS/Linux
# OR
venv\Scripts\activate           # Windows
```
#### 3️⃣ Install dependencies
```
pip install -r requirements.txt
```
If requirements.txt is not present, install manually:
```
pip install fastapi uvicorn streamlit pandas scikit-learn requests pydantic
```

---
 ### 🖥️ Running the App
##### Start the FastAPI Backend (Port 8000)
```
uvicorn app:app --reload
```
#### Start the Streamlit Frontend (in another terminal)
```
streamlit run frontend.py
```
Visit: http://localhost:8501

---
### 📡 API Usage
<li>
Endpoint: POST /predict
</li>
<li>
Content-Type: application/json
<li>

🔸 Example Request:
```

{
  "age": 32,
  "weight": 78,
  "height": 1.76,
  "income_lpa": 15,
  "smoker": false,
  "city": "Delhi",
  "occupation": "private_job"
}
```
🔸 Example Response:
```
{
  "predicted_category": "Medium"
}
```
### 📸 Screenshots

![Screenshot 2025-05-30 012127](https://github.com/user-attachments/assets/3c412c09-22c5-4db5-90c1-1122fc802b41)

![Screenshot 2025-05-30 012140](https://github.com/user-attachments/assets/57484c68-6221-488c-bb06-d0dd894feb2b)

---

### 🧪 Model Training
To retrain the model:
<ol>
  <li>Open Insurance_Predictor.ipynb
</li>
  <li>Load and explore insurance.csv
</li>
  <li>Train a model using Scikit-learn
</li>
  <li>Export it as model.pkl
</li>
</ol>

### 🧾 Requirements

```
fastapi
uvicorn
streamlit
scikit-learn
pandas
requests
pydantic
```
---

### 👤 Author
Abhay Kumar
Let's connect on [LinkedIn](https://www.linkedin.com/in/abhay-kumar-aa1a9129a?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BiN9yMzITTT%2Bw7fOOwaUDpQ%3D%3D)<br>
Check out more of my work on [GitHub](https://github.com/Abhaykum123)



