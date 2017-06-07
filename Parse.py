
import feedparser
import bs4 as bs
from newspaper import Article


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

