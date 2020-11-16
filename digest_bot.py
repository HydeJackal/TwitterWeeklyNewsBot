import tweepy
import credentials
import time
from datetime import datetime
from news_access import NewsAPI
from twitter_access import TwitterAPI

def reply_digest(api):
    reply_mentions = api.get_latest_mentions()
    for mention in reply_mentions:
        api.set_last_mention(mention.id)
        if('#inthisweek' in mention.text.lower()):
            text_split = [word for word in mention.text.split() if (not word.startswith('@') and not word.startswith('#'))]
            important_text

            time_string = mention.created_at
            date_time_obj = datetime.strptime(time_string, '%Y-%m-%d %H:%M:%S')
            
            news_api = NewsAPI(credentials.NYT_API)
            url_articles = news_api.get_nyt_last_week_articles(important_text, date_time_obj)

            status = api.send_message('@' + mention.user.screen_name + 
            ' Hello there, here are some trending news from the New York Times last week in the subject(s) you specified. #inthisweek', mention.id)
            api.set_last_mention(status.id)
        

if __name__ == "__main__": 
    api = TwitterAPI(credentials.API_KEY, credentials.API_SECRET_KEY, credentials.ACCESS_TOKEN, credentials.ACCESS_TOKEN_SECRET)
    while(True):
        reply_digest(api)
        time.sleep(15)