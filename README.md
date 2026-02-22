# 📚 SmartScores – AI-Based Student Performance Predictor

<img width="1880" height="828" alt="smartscore1" src="https://github.com/user-attachments/assets/a9d9148e-8d95-41c4-9ce4-b5451b93dad3" />
<img width="1881" height="832" alt="smartscore2" src="https://github.com/user-attachments/assets/f68d3e71-8c88-4ad6-8796-08fd6954bbc7" />

## Project Overview

**SmartScores** is a machine learning project designed to **predict student exam performance** based on their study habits, mental health, sleep, attendance, and part-time job status. The project demonstrates a complete ML workflow from **data preprocessing, model selection, evaluation, explainability**, to **deployment as an interactive web application** using Streamlit.

---

## 🔍 Features

### Data Exploration

* Handles missing values and duplicates.
* Visualizes distributions of **categorical and numerical features**.
* Generates **scatter plots, boxplots, and correlation heatmaps** to understand feature relationships with exam scores.

### Machine Learning

* Supports **Linear Regression, Decision Tree, and Random Forest** models.
* Implements **hyperparameter tuning** using `GridSearchCV`.
* Evaluates models using **RMSE and R² scores** to select the best-performing model.

### Model Explainability

* Implements **Permutation Feature Importance** to show which features impact predictions the most.
* Visualizes feature importance with horizontal bar charts for clear insights.

### Deployment

* Streamlit-based interactive app allows users to input **student information**:

  * Study Hours
  * Attendance %
  * Mental Health rating
  * Sleep Hours
  * Part-Time Job status

* Displays **predicted exam score** with progress bars, metrics, and conditional feedback:

  * 🎉 Excellent performance
  * 💪 Good effort
  * 📘 Needs improvement

---

## 📦 Technologies Used

* **Python 3.12**
* **Pandas & NumPy** – Data handling
* **Matplotlib & Seaborn** – Data visualization
* **Scikit-learn** – Machine learning & model evaluation
* **Joblib** – Model saving/loading
* **Streamlit** – Web app interface

---
