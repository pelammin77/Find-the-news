"""
file: console_view.py
author: Petri Lamminaho 
"""
from feedParser import Feed
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


class View:
    def show_main_menu(self):
        print('''Availble news feeds:
        
                 1. CNN
                 2. BBC
                 3. NY Times
                 4. Washington News
                 5. Fox News
                 6. Huff Post
                 7. CNBC
                 8. Good News
                 0. Exit 
             ''')
        self.switch_feed()

    def switch_feed(self):
        self.val = input("Pick yor news feed>")
        print(self.val)
        if self.val == '0':
            exit(0)
        if self.val == '1':
            self.cnn()
        if self.val == '2':
            self.bbc()
        if self.val == '3':
            self.ny_times()
        if self.val == '4':
            self.wsh_times()
        if self.val == '5':
            self.fox_news()
        if self.val == '6':
            self.huff_post()
        if self.val == '7':
            self.cnbc()
        if self.val == '8':
            self.good_news()

    def no_command(self):
        print("Unknown command try again")
        return
    def conn_to_feed(self, site_id):
        self.feed = Feed(site_id)

    def get_all_posts(self):
        print("All posts:\n")
        arr = self.feed.get_all_posts()
        i = 1
        for post in arr:
            print(i, post.title + ":" + post.link)
            i = i+1
        self.sellect_the_post()


    def sellect_the_post(self):
        v = int(input('Give post id>'))
        if v == 0:
            return
        self.fetch_post(v)


    def fetch_post(self, post_id):

        #self.feed = Feed(site_id)
        self.feed.get_article(post_id - 1)
        #self.feed.get_article(0)
        self.feed.make_summary()

    def cnn(self):
        print("You picked CNN")
        self.conn_to_feed(CNN)
        self.get_all_posts()

    def bbc(self):
        print("You pocked BBC")
        self.conn_to_feed(BBC)
        self.get_all_posts()

    def ny_times(self):
        print("You picked NY Times")
        self.conn_to_feed(NY_TIMES)
        self.get_all_posts()

    def wsh_times(self):
        print("You picked WSH Post")
        self.conn_to_feed(WSHG_POST)
        self.get_all_posts()

    def fox_news(self):
        print("You picked Fox News")
        self.conn_to_feed(FOX_NEWS)
        self.get_all_posts()

    def huff_post(self):
        print("You picked Huff post")
        self.conn_to_feed(HUFF_POST)
        self.get_all_posts()

    def cnbc(self):
        print("You picked CNBC")
        self.conn_to_feed(CNBC)
        self.get_all_posts()

    def good_news(self):
        print("You picked Good News.com")
        self.conn_to_feed(GOOD_NEWS)
        self.get_all_posts()

    # define the function blocks

    def zero(sef):
        exit(0)
