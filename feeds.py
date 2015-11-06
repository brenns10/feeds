#!/usr/bin/env python3
"""
Python web application that merges RSS feeds.
"""

from multiprocessing.pool import ThreadPool

import feedparser
from flask import Flask, render_template
app = Flask(__name__)

# Stuff to go at the top of the feed.
name = 'HacSoc Feeds'
description = "Feeds from Hacker's Society members."
link = r'http://hacsoc.org/wiki/directory'
feed_url = r'http://localhost:8000/'
feeds = [
    r'http://stephen-brennan.com/blog/rss.xml',
    r'https://ajm188.github.io/feed.xml',
    r'https://bentley.link/index.xml',
    r'https://medium.com/feed/@KatherineCass',
    r'https://medium.com/feed/@StephHippo',
    r'https://aghassi.github.io/feed.xml',
]


@app.route('/')
def main(threaded=True):
    pool = ThreadPool()
    feed_objects = pool.map(feedparser.parse, feeds)
    return feed_objects
    #return render_template('feed.xml', name=name, description=description,
    #                       link=link, feed_url=feed_url, items=items)


if __name__ == '__main__':
    app.run(debug=True)
