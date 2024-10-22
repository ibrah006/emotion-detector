# Emotion Detection - Python Web Application


This repository contains a web-based Python application that detects emotions in user-provided text input. The application is built using Flask as the web framework.
Features

    Emotion Detection: Analyze text input to detect underlying emotions such as happiness, sadness, anger, etc.
    Flask Framework: The application is built with Flask to handle web routing and interaction.
    User-Friendly Interface: Simple and clean UI for users to input text and view emotion analysis.

Technologies Used

    Flask: Web framework for handling routes and rendering templates.
    Python: Core logic for emotion detection and text processing.
    HTML/CSS: For front-end structure and styling.
    JavaScript (optional): For handling dynamic elements, if required.

# Setup Instructions
To run this application locally, follow the steps below:
Be sure that Python is installed in your system.

1. Clone the repository:
    ```bash
    git clone https://github.com/ibrah006/emotion-detector.git
    cd emotion-detector
    ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install required dependencies:
   ```bash
   pip install flask
   pip install requests
   ```
4. Run the Flask application:
   ```bash
   python3.11 server.py
   ```
6. Finally, Open your browser: Navigate to http://127.0.0.1:5000/ to access the application.

# Usage
1. Enter text into the input field.
2. Submit the form to analyze the emotion within the text.
3. The application will display the detected emotion along with a confidence score.

# Contributing
Feel free to submit issues or contribute to the project via pull requests. Any enhancements or bug fixes are welcome!
