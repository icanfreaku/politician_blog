from django.core.management.base import BaseCommand, CommandError
import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from textblob import TextBlob
from elasticsearch import Elasticsearch

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
        # create instance of the tweepy tweet stream listener
        listener = TweetStreamListener()

        # set twitter keys/tokens
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        # create instance of the tweepy stream
        stream = Stream(auth, listener)

        # search twitter for "congress" keyword
        stream.filter(track=["Bobby Aylward", "Pat Deering", "Kathleen Funchion", "John McGuinness", "John Paul Phelan", "Heather Humpries", "Caoimhghin O'Caolain", "Brendan Smith", "Niamh Smyth", "Pat Breen", "Joe Carey", "Timmy Dooley", "Michael Harty", "Pat Buckley", "Kevin O'Keeffe", "Sean Sherlock", "David Stanton", "Mick Barry", "Billy Kelleher", "Dara Murphy", "Johnathan O'Brien", "Michael Creed", "Aindrias Moynihan", "Michael Moynihan", "Simon Coveney", "Micheal Martin", "Michael McGrath", "Donnchadh O'Laoghaire", "Michael Collins", "Jim Daly", "Margaret Murphy O'Mahony", "Pearse Doherty", "Pat Gallagher", "Charlie McConalogue", "Joe McHugh", "Thomas Pringle", "Tommy Broughan", "Richard Bruton", "Sean Haughey", "Finian McGrath", "Denise Mitchell", "Eoghan Murphy", "Jim O'Callaghan", "Kate O'Connell", "Eamon Ryan", "Paschal Donohoe", "Mary Lou McDonald", "Maureen O'Sullivan", "Clare Daly", "Alan Farrell", "Darragh O'Brien", "Louise O'Reilly", "Brendan Ryan", "John Curran", "Frances Fitzgerald", "Gino Kenny", "Eoin O'Broin", "Dessie Ellis", "Noel Rock", "Roisin Shortall", "Josepha Madigan", "Catherine Martin", "Shane Ross", "Catherine Byrne", "Joan Collins", "Aengus O'Snodaigh", "Brid Smith", "Colm Brophy", "Sean Crowe", "John Lahart", "Paul Murphy", "Katherine Zappone", "Joan Burton", "Jack Chambers", "Ruth Coppinger", "Leo Varadkar", "Maria Bailey", "Richard Boyd-Barrett", "Mary Mitchell-OConnor", "Sean Canney", "Ciaran Cannon", "Anne Rabbitte", "Catherine Connolly", "Noel Grealish", "Sean Kyne", "Hildegarde Naughten", "Eamon O'Cuiv", "John Brassil", "Martin Ferris", "Brendan Griffin", "Danny Healy Rae", "Michael Healy Rae", "Bernard Durkan", "James Lawless", "Catherine Murphy", "Frank O'Rourke", "Martin Heydon", "Sean O'Fearghaill", "Fiona O'Loughlin", "Charlie Flanagan", "Sean Fleming", "Brian Stanley", "Micheal Noonan", "Willie O'Dea", "Jan O'Sullivan", "Maurice Quinlivan", "Niall Collins", "Tom Neville", "Patrick O'Donovan", "Kevin Boxer Moran", "Peter Burke", "Willie Penrose", "Robert Troy", "Gerry Adams", "Declan Breathnach", "Peter Fitzpatrick", "Imelda Munster", "Fergus O'Dowd", "Dara Calleary", "Lisa Chambers", "Enda Kenny", "Michael Ring", "Thomas Byrne", "Regina Doherty", "Helen McEntee", "Shane Cassells", "Damien English", "Peadar Toibn", "Marcella Corcoran-Kennedy", "Barry Cowen", "Carol Nolan", "Michael Fitzmaurice", "Eugene Murphy", "Denis Naughten", "Martin Kenny", "Marc MacSharry", "Tony McLoughlin", "Eamon Scanlon", "Jackie Cahill", "Seamus Healy", "Alan Kelly", "Michael Lowry", "Mattie McGrath", "Mary Butler", "David Cullinane", "John Deasy", "John Halligan", "James Browne", "Michael D'Arcy", "Brendan Howlin", "Paul Kehoe", "Mick Wallace", "John Brady", "Pat Casey", "Stephen Donnelly", "Andrew Doyle", "Simon Harris"])
