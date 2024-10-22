import requests
import json

def emotion_detector(text_to_analyse: str):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    obj_data = { "raw_document": { "text": text_to_analyse } }

    print(f"text_to_analyse provided: {text_to_analyse}, type: {type(text_to_analyse)}")

    response = requests.post(url, headers = header, json = obj_data)

    print(f"statuscode : {response.status_code}")

    if response.status_code == 500:
        return " Invalid text! Please try again!."

    formatted_response = json.loads(response.text)

    emotion_scores = {}
    if response.status_code == 400:
        emotion_scores["anger"] = None
        emotion_scores["disgust"] = None
        emotion_scores["fear"] = None
        emotion_scores["joy"] = None
        emotion_scores['sadness'] = None

        dominant_emotion = None
    else:
        emotionPredictions = formatted_response["emotionPredictions"][0]
        emotion_scores = emotionPredictions["emotion"]

        dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    return {
        "anger": emotion_scores["anger"],
        'disgust': emotion_scores['disgust'],
        'fear': emotion_scores['fear'],
        'joy': emotion_scores['joy'],
        'sadness': emotion_scores['sadness'],
        'dominant_emotion': dominant_emotion
    }
