from flask import Flask, request, jsonify, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET'])
def detect_emotion():
    text_to_analyze = request.args.get('textToAnalyze', '')
    if not text_to_analyze.strip():
        return "Invalid text! Please try again!", 400

    result = emotion_detector(text_to_analyze)

    if 'error' in result:
        return f"Error: {result['error']}", 500

    if result.get('dominant_emotion') is None:
        return "Invalid text! Please try again!", 400

    emotions = result.get('emotions', {})
    response = (
        f"For the given statement, the system response is "
        f"'anger': {emotions.get('anger', 0)}, "
        f"'disgust': {emotions.get('disgust', 0)}, "
        f"'fear': {emotions.get('fear', 0)}, "
        f"'joy': {emotions.get('joy', 0)}, "
        f"and 'sadness': {emotions.get('sadness', 0)}. "
        f"The dominant emotion is {result.get('dominant_emotion', 'unknown')}."
    )

    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


