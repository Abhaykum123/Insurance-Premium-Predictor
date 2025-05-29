# from fastapi import FastAPI
# from fastapi.responses import JSONResponse
# from pydantic import BaseModel, Field, computed_field
# from typing import Literal, Annotated
# import pickle
# import pandas as pd
# import json
# import os

# # import the ml model
# with open('model.pkl', 'rb') as f:
#     model = pickle.load(f)

# app = FastAPI()

# def load_data():
#     with open('data.json', 'r') as f:
#         data = json.load(f)

#     return data

# def save_data(data):
#     with open('data.json','w') as f:
#         json.dump(data, f)

# tier_1_cities = ["Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata", "Hyderabad", "Pune"]
# tier_2_cities = [
#     "Jaipur", "Chandigarh", "Indore", "Lucknow", "Patna", "Ranchi", "Visakhapatnam", "Coimbatore",
#     "Bhopal", "Nagpur", "Vadodara", "Surat", "Rajkot", "Jodhpur", "Raipur", "Amritsar", "Varanasi",
#     "Agra", "Dehradun", "Mysore", "Jabalpur", "Guwahati", "Thiruvananthapuram", "Ludhiana", "Nashik",
#     "Allahabad", "Udaipur", "Aurangabad", "Hubli", "Belgaum", "Salem", "Vijayawada", "Tiruchirappalli",
#     "Bhavnagar", "Gwalior", "Dhanbad", "Bareilly", "Aligarh", "Gaya", "Kozhikode", "Warangal",
#     "Kolhapur", "Bilaspur", "Jalandhar", "Noida", "Guntur", "Asansol", "Siliguri"
# ]

# # pydantic model to validate incoming data
# class UserInput(BaseModel):

#     age: Annotated[int, Field(..., gt=0, lt=120, description='Age of the user')]
#     weight: Annotated[float, Field(..., gt=0, description='Weight of the user')]
#     height: Annotated[float, Field(..., gt=0, lt=2.5, description='Height of the user')]
#     income_lpa: Annotated[float, Field(..., gt=0, description='Annual salary of the user in lpa')]
#     smoker: Annotated[bool, Field(..., description='Is user a smoker')]
#     city: Annotated[str, Field(..., description='The city that the user belongs to')]
#     occupation: Annotated[Literal['retired', 'freelancer', 'student', 'government_job',
#        'business_owner', 'unemployed', 'private_job'], Field(..., description='Occupation of the user')]
    
#     @computed_field
#     @property
#     def bmi(self) -> float:
#         return self.weight/(self.height**2)
    
#     @computed_field
#     @property
#     def lifestyle_risk(self) -> str:
#         if self.smoker and self.bmi > 30:
#             return "high"
#         elif self.smoker or self.bmi > 27:
#             return "medium"
#         else:
#             return "low"
        
#     @computed_field
#     @property
#     def age_group(self) -> str:
#         if self.age < 25:
#             return "young"
#         elif self.age < 45:
#             return "adult"
#         elif self.age < 60:
#             return "middle_aged"
#         return "senior"
    
#     @computed_field
#     @property
#     def city_tier(self) -> int:
#         if self.city in tier_1_cities:
#             return 1
#         elif self.city in tier_2_cities:
#             return 2
#         else:
#             return 3

# @app.post('/predict')
# def predict_premium(data: UserInput):

#     input_df = pd.DataFrame([{
#         'bmi': data.bmi,
#         'age_group': data.age_group,
#         'lifestyle_risk': data.lifestyle_risk,
#         'city_tier': data.city_tier,
#         'income_lpa': data.income_lpa,
#         'occupation': data.occupation
#     }])

#     prediction = model.predict(input_df)[0]

#     return JSONResponse(status_code=200, content={'predicted_category': prediction})


from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Literal
import pickle
import pandas as pd
import json
import os

# Load the ML model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

app = FastAPI()

# Define city tiers
tier_1_cities = ["Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata", "Hyderabad", "Pune"]
tier_2_cities = [
    "Jaipur", "Chandigarh", "Indore", "Lucknow", "Patna", "Ranchi", "Visakhapatnam", "Coimbatore",
    "Bhopal", "Nagpur", "Vadodara", "Surat", "Rajkot", "Jodhpur", "Raipur", "Amritsar", "Varanasi",
    "Agra", "Dehradun", "Mysore", "Jabalpur", "Guwahati", "Thiruvananthapuram", "Ludhiana", "Nashik",
    "Allahabad", "Udaipur", "Aurangabad", "Hubli", "Belgaum", "Salem", "Vijayawada", "Tiruchirappalli",
    "Bhavnagar", "Gwalior", "Dhanbad", "Bareilly", "Aligarh", "Gaya", "Kozhikode", "Warangal",
    "Kolhapur", "Bilaspur", "Jalandhar", "Noida", "Guntur", "Asansol", "Siliguri"
]

# Input schema
class UserInput(BaseModel):
    age: int = Field(..., gt=0, lt=120, description="Age of the user")
    weight: float = Field(..., gt=0, description="Weight in kg")
    height: float = Field(..., gt=0, lt=2.5, description="Height in meters")
    income_lpa: float = Field(..., gt=0, description="Annual income in LPA")
    smoker: bool
    city: str
    occupation: Literal['retired', 'freelancer', 'student', 'government_job',
                        'business_owner', 'unemployed', 'private_job']

def compute_features(data: UserInput):
    bmi = data.weight / (data.height ** 2)
    
    if data.smoker and bmi > 30:
        lifestyle_risk = "high"
    elif data.smoker or bmi > 27:
        lifestyle_risk = "medium"
    else:
        lifestyle_risk = "low"

    if data.age < 25:
        age_group = "young"
    elif data.age < 45:
        age_group = "adult"
    elif data.age < 60:
        age_group = "middle_aged"
    else:
        age_group = "senior"

    if data.city in tier_1_cities:
        city_tier = 1
    elif data.city in tier_2_cities:
        city_tier = 2
    else:
        city_tier = 3

    return bmi, lifestyle_risk, age_group, city_tier

@app.post("/predict")
def predict_premium(data: UserInput):
    bmi, lifestyle_risk, age_group, city_tier = compute_features(data)

    input_df = pd.DataFrame([{
        'bmi': bmi,
        'age_group': age_group,
        'lifestyle_risk': lifestyle_risk,
        'city_tier': city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }])

    try:
        prediction = model.predict(input_df)[0]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Model prediction failed: {str(e)}")

    # Build output record
    record = data.dict()
    record.update({
        "bmi": bmi,
        "lifestyle_risk": lifestyle_risk,
        "age_group": age_group,
        "city_tier": city_tier,
        "predicted_category": prediction
    })

    # Append to file
    with open("data.json", "a") as f:
        json.dump(record, f)
        f.write("\n")

    return JSONResponse(status_code=200, content={"predicted_category": prediction})
