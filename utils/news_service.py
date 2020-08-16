from pygooglenews import GoogleNews

api = GoogleNews(lang='en')

news = api.search('blockchain')
print(news)
