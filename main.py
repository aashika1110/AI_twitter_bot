from fastapi import FastAPI
from pydantic import BaseModel
from reply_engine import generate_reply
from twitter_client import post_reply
from sentiment import get_sentiment  # Optional – still in use for comparison if needed

app = FastAPI()

class TweetData(BaseModel):
    text: str
    id: str
    user_handle: str

@app.post("/webhook")
async def handle_mention(payload: TweetData):
    print("📩 Payload received:", payload)
    tweet_text = payload.text
    tweet_id = payload.id
    user_handle = payload.user_handle

    print("✅ Received tweet:", tweet_text)

    try:
        sentiment = get_sentiment(tweet_text)
        print("🔍 Sentiment:", sentiment)
    except Exception as e:
        print("❌ Sentiment Error:", e)
        return {"status": "error", "message": "Sentiment error"}

    try:
        emotion, reply = generate_reply(tweet_text)
        print("🧠 Emotion Detected:", emotion)
        print("💬 GPT Reply:", reply)
    except Exception as e:
        print("❌ GPT Error:", e)
        return {"status": "error", "message": "GPT error"}

    try:
        post_reply(reply, tweet_id, user_handle)
        print("📤 Tweet sent!")
    except Exception as e:
        print("❌ Twitter Error:", e)
        return {"status": "error", "message": "Twitter error"}

    return {"status": "ok"}

