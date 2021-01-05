from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import html as html_es
import time
from Utils import text4csv



class foxNews:
    def __init__(self):
        self.login_required = False
        self.name = "foxnews.com"

    
    def getArticle(self,html):
        article = "NA"
        author = "NA"

        soup = BeautifulSoup(html, "html.parser")
        article_tag = soup.find("div", {"class": "article-content"})
        if article_tag != None:
            pragraphs = article_tag.findAll("p")
            article = ""
            for p in pragraphs:
                article += text4csv(p.get_text())

        author_span = soup.find("span", {"class": "article-source"})
        if author_span!=None:
            author = text4csv(author_span.get_text())

        return article, author

    def botDetected(self,html):
        return


scraper = foxNews()