"""This module handles the server side of the Application"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def home():
    """This handles the home of the app."""
    return render_template("index.html")


@app.route("/emotionDetector")
def emotion_detector_endpoint():
    """This function calls the api (along with the input)
    powered by IBM Ai and returns the emotion scores."""

    text_to_analyze = request.args.get('textToAnalyze')

    emotion_data = emotion_detector(text_to_analyze)
    dominant_emotion = emotion_data["dominant_emotion"]

    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    del emotion_data["dominant_emotion"]

    system_response = str(emotion_data)[1:-1]
    response_message = f"For the given statement, the system response is {system_response}."

    return  f"{response_message} The dominant emotion is {dominant_emotion}."


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
