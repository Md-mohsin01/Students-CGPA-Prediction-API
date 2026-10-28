from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(
    title="Students CGPA Prediction API",
    description="An ML-Powered API endpoint to predict student CGPA based on academic and life style metrics.",
    version="1.0.0"
)

class prediction_input(BaseModel):
    study_hours: float = Field(..., description="Daily Study Hours", ge=0.0, le=24.0)
    attendance: float = Field(..., description="Attendance Percentage", ge=0.0, le=100.0)
    sleep_hours: float = Field(..., description="Average daily sleep hours", ge=0.0, le=24.0)

    class Config:
        json_schema_extra = {
            "example": {
                "study_hours": 6.5,
                "attendance": 85.0,
                "sleep_hours": 7.0
            }
        }

@app.post("/predict", tags=["Machine learning"])
def predict_cgpa(data: prediction_input):
    # We removed the try/except block so the terminal will show us EXACTLY what is wrong if it fails!
    calculated_score = (data.study_hours * 0.4) + (data.attendance * 0.05) + (data.sleep_hours * 0.1)
    mock_cgpa = min(round(calculated_score, 2), 10.0)
    
    return {
        "status": "success",
        "predicted_cgpa": mock_cgpa
    }
