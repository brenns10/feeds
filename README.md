Feed Combinator
===============

This is a web application that merges multiple RSS/Atom/whatever feeds into a
single RSS feed that you can subscribe.  It's set up to do HacSoc members'
feeds.  Yay.

Try
---

    $ git clone git@github.com:brenns10/feeds.git
    $ cd feeds
    $ virtualenv venv
    $ source venv/bin/activate
    $ pip install -r requirements.txt
    $ python feeds.py

And then navigate to http://localhost:5000
