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
        article = "NA"
        author = "NA"

        soup = BeautifulSoup(html, "html.parser")
        article_tag = soup.findAll("div", {"class": "zn-body__paragraph"})
        if len(article_tag)>0: #version 1
            article = ""
            for d in article_tag:
                article += " "+text4csv(d.get_text())
        
        else: #version 2
            article_tag = soup.find("div", {"id": "storytext"})
            if article_tag != None:
                paragraphs = soup.findAll("p")
                if len(paragraphs)>0:
                    article = ""
                    for p in paragraphs:
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