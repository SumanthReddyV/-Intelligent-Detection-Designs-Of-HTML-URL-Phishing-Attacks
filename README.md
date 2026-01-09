# -Intelligent-Detection-Designs-Of-HTML-URL-Phishing-Attacks

This project leverages machine learning techniques to analyze URLs and detect potential phishing attacks. It focuses on identifying malicious patterns and characteristics in URLs to enhance cybersecurity measures.

## Features Used for Detection
- **URL Length**: Measures the length of the URL.
- **Letters Count**: Counts the number of alphabetic characters in the URL.
- **Digits Count**: Counts the number of numeric characters in the URL.
- **Special Character Count**: Counts the number of special characters in the URL.
- **Shortened URL**: Identifies if the URL is shortened.
- **Abnormal URL**: Detects if the URL structure is abnormal.
- **Secure HTTP (HTTPS)**: Checks if the URL uses HTTPS for secure communication.
- **IP Address**: Identifies if the URL contains an IP address instead of a domain name.
- **URL Region**: Analyzes the geographical region of the URL.
- **Root Domain**: Examines the root domain of the URL.

## Project Structure
- **app.py**: The main application file.
- **malicious_phish.csv**: Dataset used for training and testing the model.
- **templates/**: Contains HTML templates for the web interface.
  - `home.html`: Homepage of the application.
  - `performance.html`: Displays model performance metrics.
  - `prediction.html`: Interface for making predictions.
  - `result.html`: Displays prediction results.
- **static/**: Contains static assets like images and stylesheets.

## How to Run the Project
1. Clone the repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the application using `python app.py`.
4. Open the application in your browser at `http://127.0.0.1:5000/`.

## Dataset
The dataset `malicious_phish.csv` contains labeled data for training and testing the phishing detection model. Ensure the dataset is placed in the root directory of the project.

## Contributions
Contributions are welcome! Feel free to fork the repository and submit pull requests.

