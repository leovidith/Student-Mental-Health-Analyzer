[# Student Mental Health Analyzer](https://student-mental-health-analyzer.onrender.com/)

## Overview

The **Student Mental Health Analyzer** is a web-based application designed to assess the mental health status of students using machine learning. By entering details such as gender, age, course, CGPA, marital status, anxiety, panic attack history, and treatment, the system predicts whether a student is likely to experience depression.

The app uses a **K-Nearest Neighbors (KNN)** model for predictions, built with Python and deployed with Flask. The frontend is developed using HTML, CSS, and JavaScript to ensure a smooth and interactive user experience.

---

## Agile Features

The development of this project was handled using an **Agile methodology** with two main sprints:

### Sprint 1
- **Goal**: Build the fundamental structure of the application, including the form, backend integration, and prediction functionality.
- **Outcome**: A working form that collects user data and outputs the mental health prediction result using the KNN model.

### Sprint 2
- **Goal**: Enhance the user experience and improve the styling of the application.
- **Outcome**: Added dynamic styling for prediction results, improved form validation, and overall better UX/UI design.

---

## Results

### Model Information
- **Model Used**: K-Nearest Neighbors (KNN)
- **Accuracy**: The model achieves an impressive **95% accuracy** in predicting whether a student is likely to experience depression based on the input features.

### Example Prediction
- **Input**: 
  - Gender: Male
  - Age: 19
  - Course: Engineering
  - CGPA: 8.0
  - Marital Status: No
  - Anxiety: No
  - Panic Attack: No
  - Treatment: No
- **Prediction**: No Depression Detected

### Model Performance
The KNN model was trained on a dataset of student mental health data. It uses the **K-Nearest Neighbors algorithm** to classify the mental health status based on the user's input. The high accuracy (95%) of the model indicates that it can reliably classify whether a student is at risk for depression based on the provided features.
