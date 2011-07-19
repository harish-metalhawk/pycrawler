#!/usr/bin/python2.7
import urllib
from time import sleep
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
        print(self.all_links)
        currentLink = self.all_links.pop(0)
        print("--------------",currentLink)
        if not currentLink.startswith("h"):
            return
        usock = urllib.urlopen(currentLink)
        #data = usock.read()
        #print data
        parser = self.feed(usock.read())
        usock.close()
        self.visited_links.append(currentLink)
        #self.parser.close()
        for url in self.urls:
            print url
            if not url.startswith("http"):
                url = currentLink + url
            if not self.all_links.__contains__(url):
                self.all_links.append(url)
            print url

    def recCrawl(self):
        self.linksInOnePage()
        sleep(2)
        self.recCrawl()

    def init(self,link):
        self.all_links=[]
        self.visited_links=[]
        self.all_links.append(link)
        self.recCrawl()

item= crawl()
item.init("http://google.com")
