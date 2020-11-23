import json
import urllib.request
import credentials
from datetime import datetime, timedelta

class NewsAPI:

    def __init__(self, nyt_api):
        self.nyt_access = nyt_api

    def get_nyt_last_week_articles(self, topic, today):
        delta = timedelta(weeks = 1)
        last_week = today - delta
        begin_date = last_week.strftime('%Y%m%d')
        url = 'https://api.nytimes.com/svc/search/v2/articlesearch.json?q=' + topic + '&begin_date=' + begin_date + '&sort=best&type_of_material=Article&api-key=' + self.nyt_access
        try:
            json_url = urllib.request.urlopen(url)
            articles = json.loads(json_url.read())
        except:
            raise RuntimeError('Failed to retrive New York Times data.')
        if articles['status'] == 'OK':
            return articles['response']['docs'][0:4], articles['response']['meta']['hits']
        else:
            raise RuntimeError('Failed to find any New York Times articles with query.')

api = NewsAPI(credentials.NYT_API)
date_time_obj = datetime.now()
api.get_nyt_last_week_articles('election', date_time_obj)