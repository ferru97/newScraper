from bs4 import BeautifulSoup
import html as html_es
from Utils import text4csv


class usaToday:
    def __init__(self):
        self.login_required = False
        self.name = "usatoday.com"
    
    def getArticle(self,html):
        article = "NA"
        author = "NA"

        soup = BeautifulSoup(html, "html.parser")
        article_tag = soup.find("div",{"class":"caas-content-wrapper"})
        if article_tag==None:
            article_tag = soup.find("article")

        if article_tag!=None:
            article = ""
            for p in article_tag.find_all("p", recursive=False):
                article += text4csv(p.get_text())

        author_span = article_tag.find("div", {"class": "caas-attr-meta"})
        if author_span==None:
            author_span = article_tag.find("a", {"class": "authors"})
        if author_span==None:
            author_span = article_tag.find("span", {"class": "authors"})
        

        if author_span!=None:
            author = text4csv(author_span.get_text())


        return article, author

    def botDetected(self,html):
        return


scraper = usaToday()