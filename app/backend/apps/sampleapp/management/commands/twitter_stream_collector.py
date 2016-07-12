from django.core.management.base import BaseCommand, CommandError
import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from textblob import TextBlob
from elasticsearch import Elasticsearch
from apps.sampleapp.models import Politician


# import twitter keys and tokens
consumer_key = "iaWUFjCmj8pkQHrB5n7Ex73x6"
consumer_secret = "FgwrlAGeDSvBMxhrKO4uLNkOyNJPATUL0jgZYMLG39kyj56MsZ"
access_token = "91611384-WMvyZAmF060lQ93ZtILR5sDseHZ2iJdomMuhHKAJR"
access_token_secret = "ZQ5VNxyIDM6ncmVmxavEmt13phjcChhk4mMfMf7vRk0G3"

# create instance of elasticsearch
es = Elasticsearch(["ek"])

class TweetStreamListener(StreamListener):

    # on success
    def on_data(self, data):

        # decode json
        dict_data = json.loads(data)

        # pass tweet into TextBlob
        tweet = TextBlob(dict_data["text"])

        # output sentiment polarity
        print(tweet.sentiment.polarity)

        # determine if sentiment is positive, negative, or neutral
        if tweet.sentiment.polarity < 0:
            sentiment = "negative"
        elif tweet.sentiment.polarity == 0:
            sentiment = "neutral"
        else:
            sentiment = "positive"

        # output sentiment
        print(sentiment)

        # add text and sentiment info to elasticsearch
        es.index(index="twitter",
                 doc_type="tweet",
                 body={"id": dict_data["id"],
                       "author": dict_data["user"]["screen_name"],
                       "picture_url": dict_data["user"]["profile_image_url"], 
                       "date": dict_data["created_at"],
                       "message": dict_data["text"],
                       "polarity": tweet.sentiment.polarity,
                       "subjectivity": tweet.sentiment.subjectivity,
                       "sentiment": sentiment})
        return True

    # on failure
    def on_error(self, status):
        print(status)

class Command(BaseCommand):
    help = 'Start the collection of tweets from twitter stream'

    def handle(self, *args, **options):
        
        politicians = Politician.objects.all();

        politician_keywords = []
        for politician in politicians:
            politician_keywords.append(politician.first_name + " " + politician.last_name)
            if politician.twitter_url:
                indexSlash = politician.twitter_url.rfind("/")
                indexQuestionMark = politician.twitter_url.rfind("?")
                if indexQuestionMark != -1:
                    twitter = politician.twitter_url[indexSlash+1:indexQuestionMark]
                else:
                    twitter = politician.twitter_url[indexSlash+1:]
                politician_keywords.append(twitter)
        
        # create instance of the tweepy tweet stream listener
        listener = TweetStreamListener()

        # set twitter keys/tokens
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        # create instance of the tweepy stream
        stream = Stream(auth, listener)


        # search twitter for "congress" keyword
        stream.filter(track=politician_keywords)
        