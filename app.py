from flask import Flask, render_template, request
from keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model


app = Flask(__name__)

import pickle

with open('tokenizer.pickle', 'rb') as handle:
    loaded_tokenizer = pickle.load(handle)


nlp_model = load_model("sentiment_analysis_model1.h5")


def decode_sentiment(score):
    a, b, c = score

    if (a >= b and a >= c):
        return "negative"
    elif (b >= a and b >= c):
        return "neutral"
    else:
        return "positive"

def predict(text):
    # Tokenize text
    x_test = pad_sequences(loaded_tokenizer.texts_to_sequences([text]), maxlen=30)
    # Predict
    score = nlp_model.predict([x_test])[0]
    # Decode sentiment
    label = decode_sentiment(score)

    return str(label)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict_route():
    print("check1")
    if request.method == 'POST':
        text = request.form['text']
        prediction = predict(text)
        return render_template('index.html', text=text, prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
