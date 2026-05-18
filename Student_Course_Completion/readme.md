# 🎓 Student Course Completion Prediction using Machine Learning

## 🎯 Problem Statement
Many students enroll in online courses but do not complete them due to factors such as low engagement, lack of motivation, or external constraints.

The goal of this project is to develop a **machine learning model that predicts whether a student will complete a course or not** using behavioral and engagement data.

Early prediction can help educational platforms:

✔ Identify at-risk students  
✔ Provide personalized support  
✔ Improve learning engagement  
✔ Increase course completion rates  

---

## 📊 Dataset
The dataset contains approximately **100,000 student records** with multiple features related to student learning behavior.

### 🔑 Key Features
- 📈 Progress Percentage
- 🎥 Video Completion Rate
- 📝 Assignments Submitted
- ⏱ Time Spent on Platform
- 🧠 Quiz Score Average
- 💳 Payment Mode
- 🌐 Internet Connection Quality
- 💻 Device Type
- 🎓 Education Level
- 👤 Gender

### 🎯 Target Variable
**Completed**

- `1` → Student completed the course  
- `0` → Student did not complete the course  

---

## ⚙️ Data Preprocessing

The following preprocessing steps were applied:

✔ Handling missing values  
✔ Feature selection using **Correlation & Chi-Square tests**  
✔ Encoding categorical variables using **OrdinalEncoder**  
✔ Scaling numerical features using **RobustScaler**  
✔ Train-test split for model evaluation  

A **ColumnTransformer + Pipeline** was used to ensure proper preprocessing during model training.

---

## 🤖 Machine Learning Models Used

### 🔹 Base Models
- Logistic Regression
- Decision Tree
- K-Nearest Neighbors (KNN)
- Support Vector Machine (SVM)
- Naive Bayes

### 🌳 Ensemble Models
- Random Forest
- AdaBoost
- Gradient Boosting
- XGBoost

### 🔗 Ensemble Techniques
- Voting Classifier
- Bagging

---

## 📏 Model Evaluation Metrics

The models were evaluated using:

📊 Accuracy  
📌 Precision  
🔍 Recall  
⚖️ F1 Score  

---

🏆 **Best Performing Models:**  
AdaBoost and Logistic Regression

This indicates the model performs **better than random guessing but still has moderate predictive power**.

---

## 🔍 Key Insights

📌 Student engagement metrics significantly influence course completion.

Important factors include:

✔ Progress Percentage  
✔ Video Completion Rate  
✔ Assignments Submitted  
✔ Learning activity engagement  

---

## 🛠 Technologies Used

🐍 Python  
📊 Pandas  
🔢 NumPy  
🤖 Scikit-learn  
⚡ XGBoost  
📈 Matplotlib & Seaborn  
🌐 Streamlit  
💻 Google Colab  

---

## 🔄 Project Workflow

```
Data Exploration
        ↓
Feature Selection
        ↓
Data Preprocessing
        ↓
Model Training
        ↓
Hyperparameter Tuning
        ↓
Model Evaluation
        ↓
Model Comparison
        ↓
Streamlit Deployment
```

## 🌐 Live Application

🚀 **Streamlit Deployment**

You can try the live application here:

👉 **Live Demo:**  
https:https://studentcoursecompletion-kysbzmfxarek3mgsog7iff.streamlit.app/

This interactive web app allows users to input student learning metrics and predict whether the student is likely to complete the course.

---

---

## 🚀 Future Improvements

Possible improvements include:
 
🔹 Deep learning based models  
🔹 Real-time analytics for learning platforms  

---

## 🏁 Conclusion

This project demonstrates how machine learning can be used to **predict student course completion** based on engagement and behavioral data.

Such predictive systems can help online learning platforms **identify students at risk of dropping out and improve learning outcomes through early intervention.**

---

