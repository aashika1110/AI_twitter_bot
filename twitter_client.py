import tweepy
import os
from dotenv import load_dotenv

load_dotenv()

auth = tweepy.OAuth1UserHandler(
    os.getenv("TWITTER_CONSUMER_KEY"),
    os.getenv("TWITTER_CONSUMER_SECRET"),
    os.getenv("TWITTER_ACCESS_TOKEN"),
    os.getenv("TWITTER_ACCESS_SECRET")
)
api = tweepy.API(auth)

def post_reply(text, tweet_id, user_handle):
    reply_text = f"@{user_handle} {text}"
    print(f"📤 [MOCK POST] Would reply to tweet ID {tweet_id} with:\n{reply_text}")

