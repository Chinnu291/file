def get_chat_response(label, user_input):
    if label in ['sadness', 'anger', 'fear', 'disgust', 'nervousness']:
        return f"I'm really sorry you're feeling this way. Would you like to talk more about it? I’m here to listen."
    elif label in ['joy', 'love', 'gratitude', 'admiration', 'relief']:
        return f"That's awesome to hear! 🎉 What made you feel so {label.lower()}?"
    elif label == 'surprise':
        return f"Whoa! That sounds surprising! Want to share more about it?"
    else:
        return f"Tell me more so I can understand better."
