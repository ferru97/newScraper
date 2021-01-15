from bs4 import BeautifulSoup
import html as html_es
from Utils import text4csv


class theStreet:
    def __init__(self):
        self.login_required = False
        self.name = "thestreet.com"
    
    def getArticle(self,html):
        article = "NA"
        author = "NA"

        soup = BeautifulSoup(html, "html.parser")

        article_tag = soup.find("div",{"class":"m-detail--body"})
        if article_tag!=None:
            article = ""
            for p in article_tag.find_all("p", recursive=False):
                article += text4csv(p.get_text())
                

        author_a = soup.find("a", {"phx-track-id": "Author Name"})
        if author_a!=None:
            author = text4csv(author_a.get_text())

        return article, author

    def botDetected(self,html):
        return


scraper = theStreet()