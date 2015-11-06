Feed Combinator
===============

I'm looking into ways that I can take multiple RSS feeds and serve them up
together as a single feed.  This would be a very cool way to create an RSS feed
of all HacSoc members' blog content.  This isn't something you can statically
generate, so this is a proof of concept web app that will load many feeds and
serve them as a single one.

It is stupidly slow...  If I were to make this into a real implementation, I
would probably need to do some threading or use coroutines to handle I/O
asynchronously.  Caching would be a definite plus as well (however requests
handles that).

Try
---


    $ git clone git@github.com:brenns10/feeds.git
    $ cd feeds
    $ virtualenv venv
    $ source venv/bin/activate
    $ pip install -r requirements.txt
    $ python feeds.py

And then navigate to http://localhost:5000
