---
layout: post
title: Third Blog
categories: blog
author: Arun Kishore Rajendran
---

# Final Project Idea:
Our final project idea is to provide trustful information about the politician to people. We are building a web application that provide valid information about Irish politicians. The application ranks the politicians based on their popularity, sentiment analysis or corruption mentions. The application will collect and parse the data from Irish newspaper and twitter feeds. The application is designed for the users who is interested in knowing about Irish politics and who is willing to have every single piece of data in a centralized place where they can easily access it. The users could be voters, new agencies, researchers, student. The user can use the application to know about the details of each politician, rank of politician, top 10 politician, politicians latest twitter feed, new article about politician. We believe that rank will be the good indicator for users to know about the sentiment analysis.

## Pages Design:

### Home Page

![alt text](https://trello-attachments.s3.amazonaws.com/574da9b98c679fb319d73d50/574x487/970c420e9260e306d58756c04bbb97c1/Picture1.png "HOME PAGE DESIGN") 

### Rank page:

![alt text](https://trello-attachments.s3.amazonaws.com/574da9b98c679fb319d73d50/569x549/d9bce09baabd7aaeea1a07d5481508c8/Picture2.png "Rank Page Design") 
 
### Details page:
 
![alt text](https://trello-attachments.s3.amazonaws.com/574da9b98c679fb319d73d50/573x540/6c386dce4d3bcfb3510fc4e5342a0cf7/Picture3.png "Details Page Design") 
 

## System design:
We are building our system using Docker which allow us to separate it into containers. All the different containers will be managed by docker compose. In this matter we will leverage an open source project seed which already has a working system with django, postgres and angular. 

