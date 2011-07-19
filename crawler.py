#!/usr/bin/python2.7
import urllib
from sgmllib import SGMLParser
class crawl(SGMLParser):
    def reset(self):
        SGMLParser.reset(self)
        self.urls=[]

    def start_a(self,attrs):
        href = [v for k, v in attrs if k=='href']
        if href:
            self.urls.extend(href)

    def linksInOnePage(self):
        #print(self.all_links)
        currentLink = self.all_links.pop(0)
        print("--------------",currentLink)
        if not currentLink.startswith("h"):
            return
        usock = urllib.urlopen(currentLink)
        #data = usock.read()
        #print data
        parser = self.feed(usock.read())
        usock.close()
        #self.parser.close()
        for url in self.urls:
            if url.startswith("/"):
                url = currentLink + url
            if not self.all_links.__contains__(url):
                self.all_links.append(url)
            #print url

    def recCrawl(self):
        self.linksInOnePage()
        self.recCrawl()

    def init(self,link):
        self.all_links=[]
        self.all_links.append(link)
        self.recCrawl()

item= crawl()
item.init("http://facebook.com")
