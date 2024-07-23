import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    
    def setUp(self):
        self.test_cases = {
            "I am glad this happened": "joy",
            "I am really mad about this": "anger",
            "I feel disgusted just hearing about this": "disgust",
            "I am so sad about this": "sadness",
            "I am really afraid that this will happen": "fear"
        }

    def test_emotion_detection(self):
        for statement, expected_emotion in self.test_cases.items():
            with self.subTest(statement=statement):
                result = emotion_detector(statement)
                dominant_emotion = result.get('dominant_emotion')
                self.assertEqual(dominant_emotion, expected_emotion, 
                                 f"Expected '{expected_emotion}' but got '{dominant_emotion}' for statement: '{statement}'")

if __name__ == '__main__':
    unittest.main()
