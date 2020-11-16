import tweepy

class TwitterAPI:
    last = 1000000000000000000
    
    def __init__(self, api_key, api_secret, access, access_secret):
        auth = tweepy.OAuthHandler(api_key, api_secret)
        auth.set_access_token(access, access_secret)
        api = tweepy.API(auth)
        self.api = api

    def get_latest_mentions(self):
        mentions = self.api.mentions_timeline(self.last)
        return mentions

    def send_message(self, msg, tweet_id):
        status = self.api.update_status(msg, tweet_id)
        return status

    def set_last_mention(self, new_mention:int):
        if new_mention > self.last:
            self.last = new_mention

    def get_last_mention(self):
        return self.last