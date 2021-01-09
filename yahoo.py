from bs4 import BeautifulSoup
import html as html_es
from Utils import text4csv


class yahoo:
    def __init__(self):
        self.login_required = False
        self.name = "yahoo.com"

    def acceptCookies(self,driver):
        try:
            accept = driver.find_element_by_name("agree")
            accept.click()
            print("Cookies accepted!")
        except:
            print("Error")
            pass
    
    def getArticle(self,html):
        article = "NA"
        author = "NA"

        soup = BeautifulSoup(html, "html.parser")

        article_tag = soup.find("div",{"class":"caas-body"})
        if article_tag!=None:
            article = ""
            for p in article_tag.find_all("p", recursive=False):
                article += text4csv(p.get_text())
                

        author_span = soup.find("div", {"class": "caas-attr-meta"})
        if author_span!=None:
            author = text4csv(author_span.get_text())

        return article, author

    def botDetected(self,html):
        return


scraper = yahoo()