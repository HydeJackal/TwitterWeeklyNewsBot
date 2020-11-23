import tweepy
import credentials
import time
from nltk.corpus import stopwords
from datetime import datetime
from news_access import NewsAPI
from twitter_access import TwitterAPI

def reply_digest(api):
    """
    Checks if there are any replies to Twitter handle and parses through data to check if there are any interesting words to search
    New York times for.

    :param TwitterAPI: The API that will handle connecting with Twitter. An instance of the class TwitterAPI from twitter_access
    """
    reply_mentions = api.get_latest_mentions()
    for mention in reply_mentions:
        api.set_last_mention(mention.id)
        if('#inthisweek' in mention.text.lower()):

            text_split = [word for word in mention.text.split(' ') if (not word.startswith('@') and not word.startswith('#'))]
            important_text = []
            important_text_no_stopwords = []
            stopwords = stopwords.words('english')
            for word in text_split:
                if word.isalpha():
                    important_text.append(word)
                    if word not in stopwords:
                        important_text_no_stopwords.append(word)
            
            if not important_text:
                important_text = important_text_no_stopwords

            time_string = mention.created_at
            date_time_obj = datetime.strptime(time_string, '%Y-%m-%d %H:%M:%S')
            
            news_api = NewsAPI(credentials.NYT_API)
            try:
                url_articles = news_api.get_nyt_last_week_articles(important_text, date_time_obj)
            except RuntimeError as e:
                msg = e

            status = api.send_message('@' + mention.user.screen_name + 
            ' Hello there, here are some trending news from the New York Times last week in the subject(s) you specified. #inthisweek', mention.id)
            api.set_last_mention(status.id)
        

if __name__ == "__main__": 
    # Run this script as the main engine of the bot
    # The below api will feed the api credentials to access Twitter
    api = TwitterAPI(credentials.API_KEY, credentials.API_SECRET_KEY, credentials.ACCESS_TOKEN, credentials.ACCESS_TOKEN_SECRET)
    while(True):
        reply_digest(api)
        # Want to make sure that we don't constantly run the for loop (takes too much resources)
        time.sleep(60)