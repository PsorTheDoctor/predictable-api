from pygooglenews import GoogleNews

api = GoogleNews(lang='en')
news = api.search('blockchain')


def get_header(idx):
    return news['entries'][idx]['title']


def get_link(idx):
    return news['entries'][idx]['link']


def get_published_date(idx):
    return news['entries'][idx]['published']
