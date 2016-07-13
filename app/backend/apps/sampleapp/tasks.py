from celery import shared_task
import feedparser
from textblob import TextBlob
from elasticsearch import Elasticsearch
from celery.utils.log import get_task_logger
from apps.sampleapp.models import Politician
from apps.sampleapp.models import Stats
from apps.sampleapp.models import RssStats
from apps.sampleapp.models import TwitterStats


import hashlib
import json
from urllib.request import urlopen


logger = get_task_logger(__name__)

es = Elasticsearch(["ek"])


def buildQueryRss(text, sentiment): 
  return { "query" : { "bool": { "must": [ { "match" : { "description" : { "query": text, "operator": "and" }}},{ "term": {"sentiment": sentiment} } ]}}}  

def buildQueryTwitter(text, sentiment): 
  return { "query" : { "bool": { "must": [ { "match" : { "message" : { "query": text, "operator": "and" }}},{ "term": {"sentiment": sentiment} } ]}}}  


@shared_task
def buildStats():

  logger.info("Started building Stats")

  rss_exist = es.indices.exists("rss")
  twitter_exist = es.indices.exists("twitter")

  if rss_exist and twitter_exist:

    politicians = Politician.objects.all();
    for politician in politicians:
      full_name = politician.first_name + " " + politician.last_name

      # RSS stats
      res = es.search(index="rss", body=buildQueryRss(full_name, "positive"))
      rss_positive = res['hits']['total']
      
      res = es.search(index="rss", body=buildQueryRss(full_name, "negative"))
      rss_negative = res['hits']['total']

      res = es.search(index="rss", body=buildQueryRss(full_name, "neutral"))
      rss_neutral = res['hits']['total']

      rss_total = rss_positive + rss_negative + rss_neutral

      # Twitter Stats
      res = es.search(index="twitter", body=buildQueryTwitter(full_name, "positive"))
      twitter_positive = res['hits']['total']

      res = es.search(index="twitter", body=buildQueryTwitter(full_name, "negative"))
      twitter_negative = res['hits']['total']

      res = es.search(index="twitter", body=buildQueryTwitter(full_name, "neutral"))
      twitter_neutral = res['hits']['total']

      twitter_total = twitter_positive + twitter_negative + twitter_neutral

      # Totals 
      total_positive = rss_positive + twitter_positive
      total_negative = rss_negative + twitter_negative
      total_neutral = rss_neutral + twitter_neutral

      total = total_positive + total_negative + total_neutral

      if not(politician.stats):
        stats = Stats()
        rss = RssStats()
        twitter = TwitterStats()
        rss.save()
        twitter.save()
        stats.save()
        rss.stats_set.add(stats)
        twitter.stats_set.add(stats)
        stats.politician_set.add(politician)

      politician.stats.rss.negative = rss_negative
      politician.stats.rss.positive = rss_positive
      politician.stats.rss.neutral = rss_neutral
      politician.stats.rss.total = rss_total

      politician.stats.twitter.negative = twitter_negative
      politician.stats.twitter.positive = twitter_positive
      politician.stats.twitter.neutral = twitter_neutral
      politician.stats.twitter.total = twitter_total

      politician.stats.total_negative = total_negative;
      politician.stats.total_positive = total_positive;
      politician.stats.total_neutral = total_neutral;
      politician.stats.total = total;

      politician.stats.rss.save()
      politician.stats.twitter.save()  
      politician.stats.save()
      politician.save()     
    


@shared_task
def loadPoliticians():
  logger.info("Started loading Politicians")

  response = urlopen("http://irish-elections.storyful.com/candidates.json")
  str_response = response.read().decode('utf-8')
  obj = json.loads(str_response)
  for candidate in obj["candidates"]:
    if candidate["current_td"]:
      politician, created = Politician.objects.update_or_create(
                last_name=candidate["last_name"].strip(),
                first_name=candidate["first_name"].strip(),
                email=candidate["email"],
                gender=candidate["gender"],

                photo_url=candidate["photo_url"],
                party_profile_url=candidate["party_profile_url"],
                website_url=candidate["party_profile_url"],
                twitter_url=candidate["twitter_url"],
                facebook_url=candidate["facebook_url"],
                instagram_url=candidate["instagram_url"],
                linkedin_url=candidate["linkedin_url"],
                youtube_url=candidate["youtube_url"],
                snapchat_url=candidate["snapchat_url"],
                phone_1=candidate["phone_1"],
                phone_2=candidate["phone_2"],

                constituency=candidate["constituency"]["name"].strip(),
                party=candidate["party"]["name"].strip(),
                )

@shared_task
def collectRSS():

  logger.info("Started collecting RSS")

  rssFeeds=["http://www.rte.ie/news/rss/news-headlines.xml",
            "http://feeds.examiner.ie/ieireland",
            "https://www.irishtimes.com/cmlink/news-1.1319192",
            "http://www.independent.ie/breaking-news/irish-news/?service=Rss",
            "http://www.thejournal.ie/feed/"]

  politicians = Politician.objects.all();

  for feed in rssFeeds:
      logger.info("Checking feed: " + feed)

      content = feedparser.parse(feed);

      for item in content.entries:

          found = False
          politician_found = None
          for politician in politicians:
              if item.description.find(politician.first_name + " " + politician.last_name) != -1:
                  politician_found = politician
                  found = True
                  break

          if found:
              id = str(int(hashlib.md5(item.link.encode('utf-8')).hexdigest(), 16))
              exist = es.indices.exists("rss")
              
              isIndexed = False
              if exist:
                  res = es.search(index="rss", body={"query": {"term" : { "id" : id }}})
                  logger.info(res)
                  if res['hits']['total'] > 0:
                     isIndexed = True 
                   
              if not(isIndexed):
                  
                   # pass rss content into TextBlob
                  analysedItem = TextBlob(item.description)

                  # output sentiment polarity
                  logger.info(analysedItem.sentiment.polarity)

                  # determine if sentiment is positive, negative, or neutral
                  if analysedItem.sentiment.polarity < 0:
                      sentiment = "negative"
                  elif analysedItem.sentiment.polarity == 0:
                      sentiment = "neutral"
                  else:
                      sentiment = "positive"

                  # output sentiment
                  logger.info(sentiment)

                   # add text and sentiment info to elasticsearch
                  es.index(index="rss",
                           doc_type="rss",
                           body={"id": id,
                                 "guid": getattr(item, "guid", ""),
                                 "title": item.title,
                                 "link": item.link, 
                                 "description": item.description,
                                 "published": item.published,
                                 "polarity": analysedItem.sentiment.polarity,
                                 "subjectivity": analysedItem.sentiment.subjectivity,
                                 "sentiment": sentiment})

              else:
                  logger.info("item already indexed") 
              
          else:
              logger.info("item does not pertain a politician")






