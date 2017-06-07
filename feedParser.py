from Summarizer import Summarizer
from Parse import Parser

'''
MTV3_ARTICLE_CLASS = 'editorial'
YLE_ARTICLE_CLASS = 'yle__article__content'
authors = ""
title = ""
date = ""
'''









parser = Parser('http://rss.cnn.com/rss/edition.rss')
title, text = parser.get_news()

summary = Summarizer()
print(title)
for s in summary._summarize(text, 2):
    print('* ' + s)
