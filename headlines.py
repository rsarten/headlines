import feedparser
from flask import Flask

app = Flask(__name__)

RSS_FEED = 	{'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
		'cnn': 'http://rss.cnn.com/rss/edition.rss',
		'fox': 'http://feeds.foxnews.com/foxnews/latest',
		'iol': 'http://www.iol.co.za/cmlink/1.640'} 

@app.route("/")
@app.route("/<publication>")
def get_news(publication="bbc"):
	feed = feedparser.parse(RSS_FEED[publication])
	first_article = feed['entries'][0]
	return """<html>
		<body>
			<h1>HEADLINES</h1>
			<b>{0}</b> <br/>
			<i>{1}</i> <br/>
			<p>{2}</p> <br/>
		</body>
		</html>""".format(first_article.get("title"), first_article.get("published"), first_article.get("summary"))

	return "no news is good news"

if __name__ == '__main__':
	app.run(port=5000, debug=True)

