from flask import Flask, request, jsonify
import pickle
import streamlit as st

model = pickle.load(open("model.pkl", "rb"))

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    prediction = model.predict(data['input_data'])
    return jsonify({'prediction': prediction.tolist()})

def run():
    with st.spinner('Loading model...'):
        app.run()

if __name__ == '__main__':
    run()
