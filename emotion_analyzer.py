try:
    from transformers import pipeline
except ModuleNotFoundError:
    raise ModuleNotFoundError("Install dependencies using: pip install -r requirements.txt")

@staticmethod
def load_model():
    return pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", return_all_scores=True)

model_instance = load_model()

def analyze(text):
    predictions = model_instance(text)
    sorted_emotions = sorted(predictions[0], key=lambda x: x['score'], reverse=True)
    return sorted_emotions[0]  # Return top emotion
