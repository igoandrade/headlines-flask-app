from flask import Flask, render_template
import feedparser

app = Flask(__name__)

BBC_FEED = "http://feeds.bbci.co.uk/news/rss.xml"

@app.route('/')
def get_news():
    feed = feedparser.parse(BBC_FEED)

    feeds = feed['entries']
    return render_template("index.html", feeds=feeds)

if __name__=='__main__':
    app.run(debug=True, port=5000)