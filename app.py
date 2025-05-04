import streamlit as st
from emoji_map import emoji_map
from chatbot_responses import get_chat_response
from emotion_analyzer import analyze

st.set_page_config(page_title="Emotion Emoji Chatbot", page_icon="💬")
st.title("💬 Emotion-Aware Chatbot")
st.write("Talk to the bot and get responses based on your emotions!")

user_input = st.text_input("How are you feeling today?", "")

if user_input:
    emotion = analyze(user_input)
    label = emotion['label']
    emoji = emoji_map.get(label, '❓')

    st.markdown(f"### Detected Emotion: {label} {emoji}")
    bot_response = get_chat_response(label, user_input)
    st.markdown(f"*Chatbot:* {bot_response}")
