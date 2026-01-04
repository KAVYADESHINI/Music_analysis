import streamlit as st
import pandas as pd
import pickle

# ------------------------------
# Load trained Pickle Model
# ------------------------------
import os
import pickle
import streamlit as st

# sklearn compatibility fix
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "xg_model.pkl")

model = pickle.load(open(MODEL_PATH, "rb"))

st.success("Model loaded successfully 🎉")


st.set_page_config(page_title="🎧 Music Listening Prediction", layout="centered")

st.title("🎧 Music Listening Reason Prediction")
st.write("Provide listening details to predict **reason_end**.")

# ------------------------------
# Input Fields (ONLY selected columns)
# ------------------------------

# Categorical Inputs
platform = st.selectbox(
    "Platform",
    ["android", "ios", "web", "windows", "mac"]  # adjust if needed
)

reason_start = st.selectbox(
    "Reason Start",
    ["trackdone", "fwdbtn", "backbtn", "clickrow", "appload"]
)

source_file = st.text_input("Source File")

# Numeric Inputs
duration_ms = st.number_input(
    "Duration (milliseconds)",
    min_value=0,
    max_value=1_000_000,
    step=1000
)

shuffle = st.selectbox("Shuffle Enabled?", ["Yes", "No"])
shuffle = 1 if shuffle == "Yes" else 0

hour = st.number_input(
    "Hour of Day",
    min_value=0,
    max_value=23
)

weekday = st.number_input(
    "Weekday (0 = Monday, 6 = Sunday)",
    min_value=0,
    max_value=6
)

# ------------------------------
# Prepare Input DataFrame
# ------------------------------
input_df = pd.DataFrame({
    "platform": [platform],
    "reason_start": [reason_start],
    "source_file": [source_file],
    "duration_ms": [duration_ms],
    "shuffle": [shuffle],
    "hour": [hour],
    "weekday": [weekday]
})
reason_end_labels = [
    "trackdone",
    "fwdbtn",
    "endplay",
    "logout",
    "unexpected-exit-while-paused",
    "backbtn",
    "remote",
    "popup",
    "unknown",
    "unexpected-exit",
    "clickrow",
    "trackerror",
    "click-row",
    "playbtn",
    "appload",
    "clickside",
    "uriopen"
]

# ------------------------------
# Prediction Button
# ------------------------------
if st.button("🔮 Predict Reason End"):
    try:
        pred_num = model.predict(input_df)[0]
        pred_label = reason_end_labels[pred_num]

        st.success(f"🎯 Predicted Reason End: **{pred_label}**")


    except Exception as e:
        st.error(f"❌ Prediction Error: {e}")
