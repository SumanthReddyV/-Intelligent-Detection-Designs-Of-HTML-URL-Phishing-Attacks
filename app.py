from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)

# Load the trained model
rf_classifier = pickle.load(open("model.pkl", "rb"))

train_accuracy = 0.90
test_accuracy = 0.95

# Function to get user input for a new data point
def get_user_input():
    try:
        url_len = int(request.form.get('url_len', 0))
        letters_count = int(request.form.get('letters_count', 0))
        digits_count = int(request.form.get('digits_count', 0))
        special_chars_count = int(request.form.get('special_chars_count', 0))
        shortened = int(request.form.get('shortened', 0))
        abnormal_url = int(request.form.get('abnormal_url', 0))
        secure_http = int(request.form.get('secure_http', 0))
        ip_address = int(request.form.get('ip_address', 0))
        url_region = int(request.form.get('url_region', 0))
        root_domain = int(request.form.get('root_domain', 0))
        
        new_data = {
            'url_len': [url_len],
            'letters_count': [letters_count],
            'digits_count': [digits_count],
            'special_chars_count': [special_chars_count],
            'Shortened': [shortened],
            'abnormal_url': [abnormal_url],
            'Secure_HTTP': [secure_http],
            'ip_address': [ip_address],
            'url_region': [url_region],
            'root_domain': [root_domain],
        }
        
        return pd.DataFrame(new_data)
    except ValueError:
        # Handle the case where a form field is not a valid integer
        return None

@app.route('/')
def home():
    return render_template('home.html')

# @app.route('/predict', methods=['GET', 'POST'])
# def predict():
#     if request.method == 'POST':
#         user_input_data = get_user_input()
#         if user_input_data is not None:
#             prediction = rf_classifier.predict(user_input_data)
#             print(prediction)
            

#             return render_template('result.html', prediction=prediction[0])
#         else:
#             # Handle the case where user input is not valid
#             return render_template('prediction.html', error_message='')
#     else:
#         return render_template('prediction.html')  # Render the form for GET requests


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        user_input_data = get_user_input()  # Assuming you have a function to get user input
        if user_input_data is not None:
            prediction = rf_classifier.predict(user_input_data)
            print(prediction)
            
            if prediction == 0:
                prediction_message = "Normal"
                
                
            elif prediction == 1:
                prediction_message = "phishing"
                
            elif prediction == 2:
                prediction_message = "malware"
               
            else:
                prediction_message = "Unknown"
            

            return render_template('result.html', prediction=prediction_message)
        else:
            # Handle the case where user input is not valid
            return render_template('prediction.html', error_message='')
    else:
        return render_template('prediction.html')  # Render the prediction form




@app.route("/result")
def result():
    return render_template("result.html")

@app.route('/performance')
def performance():
    # Add code for performance metrics (e.g., confusion matrix)
    return render_template('performance.html', train_accuracy=train_accuracy, test_accuracy=test_accuracy)

if __name__ == '__main__':
    app.run()
