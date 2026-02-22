import streamlit as st
import joblib
import numpy as np
import warnings
warnings.filterwarnings("ignore")

# Page config
st.set_page_config(page_title="SmartScores", page_icon="📚", layout="wide")

# Load model
model = joblib.load("final_best_model.pkl")

# Custom CSS for better styling
st.markdown("""
    <style>
        .main {
            background-color: #f5f7fa;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            font-size: 18px;
            border-radius: 10px;
            height: 3em;
            width: 100%;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
    </style>
""", unsafe_allow_html=True)

# Title Section
st.title("📚 SmartScores")
st.subheader("AI-Based Student Performance Predictor")

st.markdown("---")

# Sidebar
st.sidebar.header("📌 Student Information")

study_hours = st.sidebar.slider("📖 Study Hours per Day", 0.0, 12.0, 2.0)
attendance = st.sidebar.slider("🎓 Attendance (%)", 0.0, 100.0, 80.0)
mental_health = st.sidebar.slider("🧠 Mental Health (1-10)", 1, 10, 5)
sleep_hours = st.sidebar.slider("😴 Sleep Hours per Night", 0.0, 12.0, 7.0)
part_time_job = st.sidebar.selectbox("💼 Part-time Job", ["No", "Yes"])

ptj_encoded = 1 if part_time_job == "Yes" else 0

st.markdown("### 🔍 Review Your Inputs")

col1, col2 = st.columns(2)

with col1:
    st.info(f"📖 Study Hours: {study_hours}")
    st.info(f"🎓 Attendance: {attendance}%")

with col2:
    st.info(f"🧠 Mental Health: {mental_health}")
    st.info(f"😴 Sleep Hours: {sleep_hours}")

st.markdown("---")

if st.button("🚀 Predict Performance"):

    input_data = np.array([[study_hours, attendance, mental_health, sleep_hours, ptj_encoded]])
    prediction = model.predict(input_data)

    prediction = max(0, min(100, prediction[0]))

    st.success("Prediction Complete!")

    st.markdown("## 📊 Predicted Performance Score")

    st.metric(label="Performance Score", value=f"{prediction:.2f} / 100")

    st.progress(int(prediction))

    if prediction >= 75:
        st.balloons()
        st.success("Excellent Performance! 🎉 Keep it up!")
    elif prediction >= 50:
        st.warning("Good effort! You can improve further 💪")
    else:
        st.error("Needs improvement. Stay focused and consistent 📘")