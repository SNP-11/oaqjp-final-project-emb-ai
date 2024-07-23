"""
This module contains a Flask application that provides endpoints for emotion detection.

The application has two routes:
1. '/' - Renders the index.html template.
2. '/emotionDetector' - Accepts GET requests with a query parameter 'textToAnalyze',
   analyzes the emotion in the provided text, and returns a JSON response with emotion
   details or an error message.
"""

from flask import Flask, request, jsonify, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    """
    Render the index.html template.
    """
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET'])
def detect_emotion():
    """
    Detect emotion from the provided text.
    Returns a JSON response with emotion details or an error message.
    """
    text_to_analyze = request.args.get('textToAnalyze', '').strip()

    if not text_to_analyze:
        response = {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": "Invalid text! Please try again!"
        }
        return jsonify(response), 200

    result = emotion_detector(text_to_analyze)

    if 'error' in result:
        return jsonify({"error": result['error']}), 500

    dominant_emotion = result.get('dominant_emotion')
    if dominant_emotion is None:
        response = {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": "Invalid text! Please try again!"
        }
        return jsonify(response), 200

    emotions = result.get('emotions', {})
    response = {
        "anger": emotions.get('anger', 0),
        "disgust": emotions.get('disgust', 0),
        "fear": emotions.get('fear', 0),
        "joy": emotions.get('joy', 0),
        "sadness": emotions.get('sadness', 0),
        "dominant_emotion": dominant_emotion
    }

    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
