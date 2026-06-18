#  Heart Disease Prediction App

A Machine Learning-based web application that predicts the likelihood of heart disease using patient health parameters. The application is built with Python, Scikit-Learn, and Streamlit.

##  Live Demo

https://heartdiseasegit-44xbqxt82r7wwt6zqtgjrz.streamlit.app/

##  Features

* Predicts the risk of heart disease using a trained Machine Learning model.
* Simple and user-friendly Streamlit interface.
* Real-time prediction based on user input.
* Data preprocessing using StandardScaler.
* Logistic Regression based prediction model.

##  Technologies Used

* Python
* Streamlit
* Pandas
* NumPy
* Scikit-Learn
* Joblib

##  Input Parameters

The model uses the following medical parameters:

* Age
* Sex
* Chest Pain Type (cp)
* Resting Blood Pressure (trestbps)
* Cholesterol (chol)
* Fasting Blood Sugar (fbs)
* Resting ECG (restecg)
* Maximum Heart Rate Achieved (thalach)
* Exercise Induced Angina (exang)
* ST Depression (oldpeak)
* Slope
* Number of Major Vessels (ca)
* Thalassemia (thal)

##  Project Structure

```text
heart_disease/
│
├── app.py
├── heart.pkl
├── heart_scaler.pkl
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/chandrika018/heart_disease.git
```

2. Move to project directory:

```bash
cd heart_disease
```

3. Create virtual environment:

```bash
python -m venv venv
```

4. Activate virtual environment:

Windows:

```bash
venv\Scripts\activate
```

5. Install dependencies:

```bash
pip install -r requirements.txt
```

6. Run the application:

```bash
streamlit run app.py
```

##  Model Performance

* Algorithm: Logistic Regression
* Accuracy: Approximately 82%

##  Developer

Chandrika Nandehariya

##  License

This project is developed for educational and learning purposes.
