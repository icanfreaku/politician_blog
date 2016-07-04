---
layout: post
title: Fourth Post
categories: blog
author: Rodrigo Serviuc Pavezi
---

# Project Update

We are currently on the implementation phase of our project as we have already defined what needs to be done for achieving our goal. For this phase our plan is to implement 3 main MVPs and we are on the middle of the first one at the moment.

![alt text](https://trello-attachments.s3.amazonaws.com/576ab9dd2f05d019bb1abe0e/2808x1376/07c716aadbe3fb02cd07b38f930d9276/Screen_Shot_2016-07-04_at_4.40.36_PM.png " MVPs")

## MPV

* First MVP
    * Implement the collection of Tweets from the twitter stream using the stream API. 
    * Implement the collection of RSS feeds using feedparser.
    * Implement Politician page with details about each politician.
    * Implement Home Page UI.
    * Implement Rank Page UI.
    * Implement the listing of tweets and news articles on the Politician page.

* Second MVP
    * Implement the tweets and article counts for each politician.
    * Implement the stats on the Politician Page.
    * Implement the Rank by Popularity and Sentiment.
    * Implement the Top 10 on the Home Page.
    * Implement the listing of recent articles and tweets on the Home Page.

* Third MVP
    * Implement the collection of the Debate data from Dáil.
    * Implement the Debase participation count and add it to the Rank selection.
    * Implement the chart of interested topics for each politician. 


## Progress

So far we have implemented the twitter collector which uses the keyword option from the api to filter the tweets by the name of the politicians. Then it gets the sentiment related to the tweet for afterwards send the tweet with its sentiment to the elasticsearch index. We have been collecting it for almost a week and have good amount of tweets. We are using Kibana to have an overall analyse of the data. See image bellow where we have a chart showing the amount of tweets per sentiment (Negative, Positive and Neutral). 


![alt text](https://trello-attachments.s3.amazonaws.com/576ab9dd2f05d019bb1abe0e/2874x1540/e6d4404ec02d5ae71bf11db4632bdb29/Screen_Shot_2016-07-04_at_3.05.56_PM.png " Sentiment pizza chart")


We are planning to use Elasticsearch search capability to retrieve only the tweets related to a single politician. The following image shows an example of that.

![alt text](https://trello-attachments.s3.amazonaws.com/576ab9dd2f05d019bb1abe0e/2878x1052/1f56c5aeb7a69c03b7fea075e7d68b35/Screen_Shot_2016-07-04_at_3.06.32_PM.png " Search sample")


We are also in middle of the implementation of the RSS collector. This conclusion of it is delayed because of issues on running the RSS collection task on Celery. The main problem was the integration between Django and Celery. Now, it is sorted and we are finishing the implementation of the task. It is going to read each rss feed, look for new items, then get its sentiment and store it on Elasticsearch index. The task will run once every 15 minutes.


Lastly we have done some work on the Home page UI.

## Plan

We plan to finish the first MVP this week and move to work on the next MVP. We know we are behind schedule but we are making progress.  







