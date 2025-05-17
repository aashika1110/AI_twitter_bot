import streamlit as st
import os
os.environ["PORT"] = os.environ.get("PORT", "8501")

from reply_engine import generate_reply
from sentiment import get_sentiment

st.set_page_config(page_title="AI Twitter Bot", layout="centered")
st.title("🤖 Emotionally Intelligent Twitter Bot")

tweet_text = st.text_area("Enter tweet to respond to:", height=150)

if st.button("🔄 Refresh App"):
    st.rerun()

if "reply_history" not in st.session_state:
    st.session_state.reply_history = []
if "emotion" not in st.session_state:
    st.session_state.emotion = ""
if "tone" not in st.session_state:
    st.session_state.tone = ""

# Generate logic
if st.button("Generate Reply"):
    if not tweet_text.strip():
        st.warning("Please enter some tweet text.")
    else:
        sentiment = get_sentiment(tweet_text)
        st.write("📊 Sentiment (TextBlob):", sentiment)

        emotion, tone, reply = generate_reply(tweet_text)

        st.session_state.reply_history = [reply]
        st.session_state.emotion = emotion
        st.session_state.tone = tone

# Show output
if st.session_state.reply_history:
    st.write("🧠 Emotion Detected:", st.session_state.emotion)
    st.write("🎨 Tone Chosen by AI:", st.session_state.tone)

    with st.expander("💬 View & Edit AI Reply", expanded=True):
        edited_reply = st.text_area(
            label="Your AI-generated reply:",
            value=st.session_state.reply_history[-1],
            height=150,
            key="editable_reply"
        )

        if st.button("♻️ Regenerate Reply"):
            emotion, tone, new_reply = generate_reply(tweet_text)
            st.session_state.reply_history.append(new_reply)
            st.session_state.emotion = emotion
            st.session_state.tone = tone
            st.rerun()

        st.caption("📋 You can copy the reply above using Ctrl+C")





