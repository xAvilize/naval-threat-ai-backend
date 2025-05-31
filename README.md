# Naval Threat AI – Backend

Flask-based backend API for real-time naval threat prediction.

## 🔧 Tech Stack
- Python 3.x
- Flask
- Scikit-learn (Linear Regression)
- joblib

## 🔍 Features
- `/api/predict`: Accepts JSON input (lat, lng, velocity, heading) and returns risk score.
- Model trained on mock threat data.

## 📦 How to Run
```bash
pip install -r requirements.txt
python app/predict.py
