#!/usr/bin/env python3
"""
Python web application that merges RSS feeds.
"""

from multiprocessing.pool import ThreadPool
from time import mktime
from functools import reduce

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
def main():
    pool = ThreadPool()
    feed_objects = pool.map(feedparser.parse, feeds)
    entries = reduce(lambda l, f: l + f.entries, feed_objects, [])
    entries.sort(key=lambda e: mktime(e.published_parsed), reverse=True)
    return render_template('feed.xml', name=name, description=description,
                           link=link, feed_url=feed_url, items=entries)


if __name__ == '__main__':
    import sys
    if 'prod' in sys.argv:
        app.run(host='0.0.0.0:58008')
    else:
        app.run(debug=True)
