from flask import Flask, request, render_template, jsonify, url_for
import pickle
from utils import get_predict

app = Flask(__name__)

# Mapping for user-friendly input to numerical values
sex_mapping = {'female': 0, 'male': 1}
bp_mapping = {'low': 2, 'normal': 1, 'high': 3}
cholesterol_mapping = {'normal': 0, 'high': 1}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['GET','POST'])
def predict():
    data = request.form
    Age = float(data['Age'])
    Sex = sex_mapping[data['Sex'].lower()]
    BP = bp_mapping[data['BP'].lower()]
    Cholesterol = cholesterol_mapping[data['Cholesterol'].lower()]
    Na_to_K = float(data['Na_to_K'])

    predicted_drug = get_predict(Age , Sex, BP, Cholesterol, Na_to_K)

    print(f"Predicted Drug is {predicted_drug}")

    return render_template('index.html', predicted_drug=f"{predicted_drug}")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=False)
