from flask import Flask, render_template, request, jsonify
import numpy as np
import pickle
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)

print("Loading model and scaler...")
model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))
print("Model and scaler loaded successfully.")

# Updated course list with encoded values
course_list = [
    'Engineering', 'Psychology', 'Marine Science', 'Economics', 'Nursing', 'Islamic Education', 
    'Human Resources', 'Psychology', 'KENMS', 'Accounting', 'BIT', 'IRKHS', 'Business Administration',
    'Biomedical Science', 'Marine Science', 'Psychology', 'Human Sciences', 'Biomedical Science',
    'Biotechnology', 'Communication', 'Engineering', 'Business Administration', 'Marine Science', 
    'Law', 'Economics', 'Nursing', 'Communication', 'Radiography', 'Fiqh Fatwa', 'Nursing', 
    'Islamic Education', 'Human Sciences', 'Biomedical Science', 'KIRKHS', 'Marine Science', 
    'Business Administration', 'Communication', 'Diploma Nursing'
]

# Initialize LabelEncoder and fit it with the updated course list
course_encoder = LabelEncoder()
course_encoder.fit(course_list)

feature_order = ['Gender', 'Age', 'Course', 'Year of Study', 'CGPA', 'Marital Status', 'Anxiety', 'Panic Attack', 'Treatment']

def predict_with_knn(model, scaler, input_features):
    print(f"Received input: {input_features}")
    try:
        input_data = np.array([input_features[feature] for feature in feature_order]).reshape(1, -1)
        # Encode 'Course' and then scale the data
        input_data[0, 2] = course_encoder.transform([input_features['Course']])[0]  # Encode 'Course'
        input_data_scaled = scaler.transform(input_data)
        print(f"Input data for prediction (scaled): {input_data_scaled}")
        prediction = model.predict(input_data_scaled)
        print(f"Prediction result: {prediction}")
        return "Depression Detected" if prediction[0] == 1 else "No Depression Detected"
    except KeyError as e:
        print(f"Missing input for feature: {e}")
        return f"Missing input for feature: {e}"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        user_input = request.get_json()
        user_input_transformed = {
            'Gender': int(user_input['gender']),
            'Age': float(user_input['age']),
            'Course': user_input['course'],
            'Year of Study': int(user_input['year']),
            'CGPA': float(user_input['cgpa']),
            'Marital Status': 1 if user_input['maritalStatus'] == 'Yes' else 0,
            'Anxiety': 1 if user_input['anxiety'] == 'Yes' else 0,
            'Panic Attack': 1 if user_input['panicAttack'] == 'Yes' else 0,
            'Treatment': 1 if user_input['treatment'] == 'Yes' else 0
        }

        print(f"Transformed user input: {user_input_transformed}")

        result = predict_with_knn(model, scaler, user_input_transformed)

        print(f"Prediction result: {result}")

        return jsonify({'prediction': result})

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
