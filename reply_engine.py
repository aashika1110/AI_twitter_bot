import os
from openai import OpenAI
from dotenv import load_dotenv
from sentiment import get_sentiment

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_reply(tweet_text):
    # Detect basic sentiment using TextBlob
    sentiment = get_sentiment(tweet_text)
    is_negative = sentiment in ["negative", "neutral"]

    # Conditional hashtag/emojis guidance
    hashtag_instruction = (
        "- If the tweet sounds frustrated, sad, or angry, DO NOT include hashtags or emojis. Be calm, respectful, and solution-oriented."
        if is_negative else
        "- If the tweet sounds excited or thankful, you MAY include 1 brand-friendly hashtag or emoji (like #Thanks or 😊), but only if it feels natural."
    )

    prompt = f"""
You are an emotionally intelligent AI assistant that replies to customer tweets.

Tasks:
1. Detect the user's **emotion**. Choose one: excited, confused, frustrated, sad, thankful, neutral.
2. Choose a **reply tone**: empathetic, friendly, playful, professional, or sarcastic.
3. Craft a tweet-length **reply** in that tone that fits the emotion.

If the tweet is vague or lacks clear detail, politely ask the user to provide more context. Do NOT assume or give generic responses.

Guidelines:
{hashtag_instruction}
- Avoid sounding like an email or formal customer support agent.
- Keep the tone human, conversational, and suitable for Twitter — short, helpful, and real.
- Always stay under 280 characters.

Respond in this format:

Emotion: <emotion>
Tone: <tone>
Reply: <crafted tweet>

Tweet: "{tweet_text}"
"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    full_output = response.choices[0].message.content.strip()

    try:
        lines = full_output.split("\n")
        emotion = lines[0].replace("Emotion:", "").strip()
        tone = lines[1].replace("Tone:", "").strip()
        reply = lines[2].replace("Reply:", "").strip()
    except:
        emotion = "unknown"
        tone = "neutral"
        reply = full_output

    return emotion, tone, reply



