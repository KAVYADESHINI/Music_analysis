**🎧 Music Listening Reason Prediction App**

A Machine Learning–powered web application that predicts why a music track ended (reason_end) based on user listening behavior.
The app is built using Streamlit and a trained XGBoost classification model, providing an interactive and user-friendly interface.

**🚀 Project Overview**

Music streaming platforms collect rich user interaction data. Understanding why a song ends (track completion, skip, logout, error, etc.) helps improve user experience, recommendations, and platform stability.

**This project:**
Trains a machine learning model on listening behavior data,
Predicts the end reason of a music session,
Deploys the model using Streamlit for real-time inference.

**🧠 Machine Learning Model**
**Algorithm:** XGBoost Classifier
**Problem Type:** Multi-class Classification
**Target Variable:** reason_end
**Input Features:**
platform,
reason_start,
source_file,
duration_ms,
shuffle,
hour,
weekday.
The model is saved as a pickle file **(xg_model.pkl)** and loaded into the Streamlit app for predictions.


**🖥️ Application Features**
Interactive UI built with Streamlit,
Dropdowns for categorical inputs,
Numeric validation for time-based features,
Real-time prediction with human-readable labels,
Handles sklearn version compatibility issues.

**🛠️ Tech Stack**
**Programming Language:** Python
**Web Framework:** Streamlit
**Machine Learning:** XGBoost, Scikit-learn
**Data Handling:** Pandas
**Model Persistence:** Pickle

**📂 Project Structure**
├── app.py                  # Streamlit application
├── xg_model.pkl            # Trained ML model
├── music.ipynb             # Model training & experimentation notebook
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation

**▶️ How to Run the App Locally**
**1.Clone the repository**
git clone https://github.com/your-username/music-reason-prediction.git
cd music-reason-prediction

**2.Install dependencies**
pip install -r requirements.txt

**3.Run the Streamlit app**
streamlit run app.py


**🎯 Example Prediction Output**
**Predicted Reason End:** trackdone
The output is mapped from numeric model predictions to meaningful labels for easy interpretation.



**📌 Use Cases**
User behavior analysis for music streaming platforms,
Improving recommendation systems,
Identifying app usability or technical issues,
Learning end-to-end ML deployment with Streamlit.

**📝 Future Enhancements**
Add probability scores for predictions,
Improve feature engineering,
Deploy on Streamlit Community Cloud,
Integrate real-time user data.

**🙌 Acknowledgements**
Streamlit for rapid ML app deployment,
Scikit-learn & XGBoost for model development.

**⭐ If you like this project, give it a star on GitHub!**
