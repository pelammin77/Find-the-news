from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from collections import defaultdict
from string import punctuation
from heapq import nlargest
from Summarizer import Summarizer
import feedparser
import bs4 as bs
from newspaper import Article
import re, math
from collections import Counter


'''
MTV3_ARTICLE_CLASS = 'editorial'
YLE_ARTICLE_CLASS = 'yle__article__content'
authors = ""
title = ""
date = ""
'''

class Parser:
    def __init__(self, link):
        self.__link = link
        self._text =""
        self._title= ""

    def __parse_feed(self):
        self._feeds = feedparser.parse(self.__link)
        news = self._feeds.entries[1]
        print(news.link)
       # parseArticle(news.link)

        article = Article(news.link)
        article.download()
        article.parse()
        self._sauce = article.html
        self._authors = article.authors
        self._title = article.title
        self._publish_date = article.publish_date
        self.__make_soup()

    def __make_soup(self): # private
        self.__soup = bs.BeautifulSoup(self._sauce, 'html.parser')
        self.__parse_news()

    def __parse_news(self): # private

        [s.extract() for s in self.__soup('style')]
        [s.extract() for s in self.__soup('a')]
        self._title = self.__soup.find('title').text
        self._text = ' '.join(map(lambda p: p.text, self.__soup.find_all('p')))

    def get_news(self):
        self.__parse_feed()
        return self._title, self._text










parser = Parser('http://rss.cnn.com/rss/edition.rss')
title, text = parser.get_news()

summary = Summarizer()
print(title)
for s in summary._summarize(text, 2):
    print('* ' + s)
