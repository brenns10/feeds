#!/usr/bin/env python3
"""
Python web application that merges RSS feeds.
"""

import xml.etree.ElementTree as ET

import requests

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


def get_feed(url):
    """Return an iterable of "item" elements from the feed at the URL."""
    resp = requests.get(url)
    root = ET.fromstring(resp.text)
    yield from root.findall(r'./channel/item')


@app.route('/')
def main():
    item_xml = []
    for url in feeds:
        item_xml += get_feed(url)
    items = [ET.tostring(x, encoding='unicode') for x in item_xml]
    return render_template('feed.xml', name=name, description=description,
                           link=link, feed_url=feed_url, items=items)


if __name__ == '__main__':
   app.run(debug=True)
