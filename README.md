# 💰 Salary Prediction Web App

A Machine Learning web application that predicts salary based on years of experience.  
This project demonstrates end-to-end ML workflow — from training to deployment.

---

## 🚀 Live Demo

👉 https://salary-prediction-flask-app-msbegfa9xp496advunql9v.streamlit.app/

---

## 📌 Features

- Predict salary using ML model
- Simple and interactive UI
- Real dataset used
- Deployed on cloud (Streamlit)

---

## 🧠 Tech Stack

- Python
- Streamlit
- Scikit-learn
- Pandas
- NumPy

---

## 📊 Machine Learning Model

- Algorithm: Linear Regression
- Input: Years of Experience
- Output: Predicted Salary

---

## 📁 Project Structure

salary_prediction_project/
│
├── app.py # Flask app (optional)
├── app_streamlit.py # Streamlit app
├── train_model.py # Model training script
│
├── model/
│ └── model.pkl # Trained model
│
├── data/
│ └── salary_data.csv # Dataset
│
├── templates/ # Flask HTML templates
├── static/ # CSS files
│
├── requirements.txt # Dependencies
├── runtime.txt # Python version




---

## ⚙️ Installation & Setup

### 1️ Clone the repository

```bash
git clone https://github.com/your-username/salary-prediction-flask-app.git
cd salary-prediction-flask-app



Install dependencies
pip install -r requirements.txt
 Run the app
 Streamlit App
streamlit run app_streamlit.py
 Flask App (optional)
python app.py



📈 Dataset

The dataset contains:

Years of Experience

Salary

Used for training a regression model.

🌐 Deployment

This app is deployed using Streamlit Cloud.
