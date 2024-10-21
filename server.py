from flask import Flask
import json
from EmotionDetection.emotion_detection import emotion_detector

app = Flask()

@app.route("/emotionDetector")
def emotion_detector_endpoint():
    return json.dumps(emotion_detec)