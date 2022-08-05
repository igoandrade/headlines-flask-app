from flask import Flask, render_template
import feedparser

app = Flask(__name__)

RSS_FEEDS = {
    'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
    'cnn': 'http://rss.cnn.com/rss/edition.rss',
    'fox': 'http://feeds.foxnews.com/foxnews/latest',
    'iol': 'http://www.iol.co.za/cmlink/1.640'
}


@app.route('/<rss>')
def get_news(rss):
    feed = feedparser.parse(RSS_FEEDS[rss])

    return render_template("index.html", rss=rss, articles=feed['entries'])

if __name__=='__main__':
    app.run(debug=True, port=5000)