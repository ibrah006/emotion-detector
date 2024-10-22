from flask import Flask, request, render_template
import json
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/emotionDetector")
def emotion_detector_endpoint():
    text_to_analyze = request.args.get('textToAnalyze')

    emotion_data = emotion_detector(text_to_analyze)
    dominant_emotion = emotion_data["dominant_emotion"]
    del emotion_data["dominant_emotion"]

    score_response_formatted = f"For the given statement, the system response is {str(emotion_data)[1:-1]}."

    return  f"{score_response_formatted} The dominant emotion is {dominant_emotion}."


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)