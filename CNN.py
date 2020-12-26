from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import html as html_es
import time
from Utils import text4csv



class CNN:
    def __init__(self):
        self.login_required = False
        self.name = "foxnews.com"

    
    def getArticle(self,html):
        avoid_text = ["Do Not Sell","We're no longer maintaining this page.","For the latest business news and markets data, please visit CNN"]
        article = "NA"
        author = "NA"

        soup = BeautifulSoup(html, "html.parser")
        article_tag = soup.findAll("div", {"class": "el__leafmedia el__leafmedia--sourced-paragraph"})
        article_tag += soup.findAll("div", {"class": "zn-body__paragraph"})
        if len(article_tag)>0: #version 1
            article = ""
            for d in article_tag:
                if d.get_text().strip() in avoid_text:
                    continue
                article += " "+text4csv(d.get_text())
        
        else: #version 2
            article_tag = soup.find("div", {"id": "storytext"})
            if article_tag != None:
                paragraphs = article_tag.findAll("p")
                if len(paragraphs)>0:
                    article = ""
                    for p in paragraphs:
                        if p.get_text().strip() in avoid_text:
                            continue
                        article += " "+text4csv(p.get_text())

        author_span = soup.find("span", {"class": "metadata__byline__author"})
        if author_span == None:
            author_span = soup.find("span", {"class": "byline"})

        if author_span!=None:
            author = text4csv(author_span.get_text())

        return article, author

    def botDetected(self,html):
        return


scraper = CNN()