from Summarizer import Summarizer
from Parse import Parser
from find_ent import find_ent
import text_senti as senti
"""
# Feeds
# ----------------------------------------------------------------------------
CNN = 'http://rss.cnn.com/rss/edition.rss'
BBC = 'http://feeds.bbci.co.uk/news/rss.xml'
NY_TIMES = 'http://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml'
GOOD_NEWS = 'http://www.goodnewsnetwork.org/feed/'
WSHG_POST = 'http://feeds.washingtonpost.com/rss/politics'
FOX_NEWS = 'http://feeds.foxnews.com/foxnews/latest'
HUFF_POST = 'http://www.huffingtonpost.com/feeds/index.xml'
CNBC = 'http://www.cnbc.com/id/100003114/device/rss/rss.html'

# ---------------------------------------------------------------------------
"""


class Feed:
    def __init__(self, feed_url):

        self.__feed_url = feed_url
        self.__parser = Parser(feed_url)
        #self.__title = ""
        #self.__text
        self.__summary = Summarizer()

    def get_all_posts(self):
        #print("All Links")
        return self.__parser.get_all_news_links()

    def get_article(self, post_i):
        self.__title, self.__text = self.__parser.get_news(post_i)

    def make_summary(self, n=3):
        print("\nArticle title:", self.__title + "\n")
        print('Key words:', set(find_ent(self.__text)))
        print('Article summary:')
        for s in self.__summary._summarize(self.__text, n ):
            print('*', s)
        print(senti.sentiment(self.__text))
        input("\nPress any key"">")

    def find_sim_texts(self):
        pass




def find_sim_titles():
    #parser2.print_all_news_links()

    parser2.find_sim_titles(title)

def find_feeds(feed_url):
    parser = Parser(feed_url)
    parser.get_news()


"""
parser = Parser(BBC)
parser2 = Parser(NY_TIMES)
#sim = parser.compare_texts_sim("Democrats in Split-Screen: The Base Wants It All. The Party Wants to Win. ", "Trump targets Comey on Twitter, senators weigh in")
#if sim == True:
 #   print("Same news")
#parser.print_all_news_links()
title, text = parser.get_news()

summary = Summarizer()
print(text)
print(title)
clas_text = title
for s in summary._summarize(text, 3):
    #clas_text += " " + s
    print('* ' + s)

f_sen = summary.first_sen
print("first sent", f_sen)
print(clas_text)
clas_text = title + f_sen
print(senti.sentiment(clas_text))
find_sim_titles()
"""

