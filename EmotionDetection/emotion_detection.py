import requests

def emotion_detector(text_to_analyze):
    # Handle blank input
    if not text_to_analyze.strip():
        return {
            'text': text_to_analyze,
            'emotions': {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None
            },
            'dominant_emotion': None
        }
    
    # API details
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    try:
        response = requests.post(url, headers=headers, json=input_json)

        # Handle API response
        if response.status_code == 200:
            response_json = response.json()
            emotion_predictions = response_json.get('emotionPredictions', [])
            if emotion_predictions:
                emotions = emotion_predictions[0].get('emotion', {})
                required_emotions = { 
                    'anger': emotions.get('anger', 0),
                    'disgust': emotions.get('disgust', 0),
                    'fear': emotions.get('fear', 0),
                    'joy': emotions.get('joy', 0),
                    'sadness': emotions.get('sadness', 0)
                }
                dominant_emotion = max(required_emotions, key=required_emotions.get)
                
                return {
                    'text': text_to_analyze,
                    'emotions': required_emotions,
                    'dominant_emotion': dominant_emotion
                }
            else:
                return {
                    'text': text_to_analyze,
                    'emotions': { 'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None },
                    'dominant_emotion': None
                }
        else:
            # Handle errors with status code 400
            if response.status_code == 400:
                return {
                    'text': text_to_analyze,
                    'emotions': { 'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None },
                    'dominant_emotion': None
                }
            else:
                return {
                    'text': text_to_analyze,
                    'emotions': { 'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None },
                    'dominant_emotion': None,
                    'error': f"Request failed with status code {response.status_code}"
                }
    except requests.RequestException as e:
        return {
            'text': text_to_analyze,
            'emotions': { 'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None },
            'dominant_emotion': None,
            'error': str(e)
        }
