from celery import shared_task
import feedparser
from textblob import TextBlob
from elasticsearch import Elasticsearch
from celery.utils.log import get_task_logger
import hashlib

logger = get_task_logger(__name__)

es = Elasticsearch(["ek"])

@shared_task
def collectRSS():

    logger.info("Started collecting RSS")

    rssFeeds=["http://www.rte.ie/news/rss/news-headlines.xml",
              "http://feeds.examiner.ie/ieireland",
              "https://www.irishtimes.com/cmlink/news-1.1319192",
              "http://www.independent.ie/breaking-news/irish-news/?service=Rss",
              "http://www.thejournal.ie/feed/"]

    politicians = ["Bobby Aylward", "Pat Deering", "Kathleen Funchion", "John McGuinness", "John Paul Phelan", "Heather Humpries", "Caoimhghin O'Caolain", "Brendan Smith", "Niamh Smyth", "Pat Breen", "Joe Carey", "Timmy Dooley", "Michael Harty", "Pat Buckley", "Kevin O'Keeffe", "Sean Sherlock", "David Stanton", "Mick Barry", "Billy Kelleher", "Dara Murphy", "Johnathan O'Brien", "Michael Creed", "Aindrias Moynihan", "Michael Moynihan", "Simon Coveney", "Micheal Martin", "Michael McGrath", "Donnchadh O'Laoghaire", "Michael Collins", "Jim Daly", "Margaret Murphy O'Mahony", "Pearse Doherty", "Pat Gallagher", "Charlie McConalogue", "Joe McHugh", "Thomas Pringle", "Tommy Broughan", "Richard Bruton", "Sean Haughey", "Finian McGrath", "Denise Mitchell", "Eoghan Murphy", "Jim O'Callaghan", "Kate O'Connell", "Eamon Ryan", "Paschal Donohoe", "Mary Lou McDonald", "Maureen O'Sullivan", "Clare Daly", "Alan Farrell", "Darragh O'Brien", "Louise O'Reilly", "Brendan Ryan", "John Curran", "Frances Fitzgerald", "Gino Kenny", "Eoin O'Broin", "Dessie Ellis", "Noel Rock", "Roisin Shortall", "Josepha Madigan", "Catherine Martin", "Shane Ross", "Catherine Byrne", "Joan Collins", "Aengus O'Snodaigh", "Brid Smith", "Colm Brophy", "Sean Crowe", "John Lahart", "Paul Murphy", "Katherine Zappone", "Joan Burton", "Jack Chambers", "Ruth Coppinger", "Leo Varadkar", "Maria Bailey", "Richard Boyd-Barrett", "Mary Mitchell-OConnor", "Sean Canney", "Ciaran Cannon", "Anne Rabbitte", "Catherine Connolly", "Noel Grealish", "Sean Kyne", "Hildegarde Naughten", "Eamon O'Cuiv", "John Brassil", "Martin Ferris", "Brendan Griffin", "Danny Healy Rae", "Michael Healy Rae", "Bernard Durkan", "James Lawless", "Catherine Murphy", "Frank O'Rourke", "Martin Heydon", "Sean O'Fearghaill", "Fiona O'Loughlin", "Charlie Flanagan", "Sean Fleming", "Brian Stanley", "Micheal Noonan", "Willie O'Dea", "Jan O'Sullivan", "Maurice Quinlivan", "Niall Collins", "Tom Neville", "Patrick O'Donovan", "Kevin Boxer Moran", "Peter Burke", "Willie Penrose", "Robert Troy", "Gerry Adams", "Declan Breathnach", "Peter Fitzpatrick", "Imelda Munster", "Fergus O'Dowd", "Dara Calleary", "Lisa Chambers", "Enda Kenny", "Michael Ring", "Thomas Byrne", "Regina Doherty", "Helen McEntee", "Shane Cassells", "Damien English", "Peadar Toibn", "Marcella Corcoran-Kennedy", "Barry Cowen", "Carol Nolan", "Michael Fitzmaurice", "Eugene Murphy", "Denis Naughten", "Martin Kenny", "Marc MacSharry", "Tony McLoughlin", "Eamon Scanlon", "Jackie Cahill", "Seamus Healy", "Alan Kelly", "Michael Lowry", "Mattie McGrath", "Mary Butler", "David Cullinane", "John Deasy", "John Halligan", "James Browne", "Michael D'Arcy", "Brendan Howlin", "Paul Kehoe", "Mick Wallace", "John Brady", "Pat Casey", "Stephen Donnelly", "Andrew Doyle", "Simon Harris"]
    
    for feed in rssFeeds:
        logger.info("Checking feed: " + feed)

        content = feedparser.parse(feed);

        for item in content.entries:

            found = False
            for politician in politicians:
                if item.description.find(politician) != -1:
                    found = True
                    logger.info(politician)
                    logger.info(item.description)
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






