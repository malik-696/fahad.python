from flask import Flask, render_template, request, jsonify
import pickle
from sklearn.feature_extraction.text import CountVectorizer

app = Flask(__name__)

# Load your pre-trained model and vectorizer
# For this example, we assume you have 'model.pkl' and 'vectorizer.pkl'
model = pickle.load(open('spam_model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        message = request.form['message']
        data = [message]
        vect = vectorizer.transform(data).toarray()
        prediction = model.predict(vect)
        return render_template('index.html', prediction=prediction[0])

if __name__ == '__main__':
    app.run(debug=True)