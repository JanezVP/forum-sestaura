#!/usr/bin/env python
import webapp2
from handlers.base import MainHandler, CookieAlertHandler, AboutHandler
from handlers.topics import TopicAdd, TopicDetails


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler, name="main-page"),
    webapp2.Route('/about', AboutHandler, name="about-page"),
    webapp2.Route('/set-cookie', CookieAlertHandler, name="set-cookie"),
    webapp2.Route('/topic/add', TopicAdd, name="topic-add"),
    webapp2.Route('/topic/<topic_id:\d+>', TopicDetails, name="topic-details"),
], debug=True)
