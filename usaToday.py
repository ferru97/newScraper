from bs4 import BeautifulSoup
import html as html_es


class usaToday:
    def __init__(self):
        self.login_required = False
    
    def getArticle(self,html):
        article = "NA"
        author = "NA"

        soup = BeautifulSoup(html, "html.parser")
        article_tag = soup.find("article")

        if article_tag!=None:
            article = ""
            for p in article_tag.find_all("p", recursive=False):
                article += str(p.get_text()).replace("\n"," ")

        #author_span = soup.findAll("span", {"class": "authors"})
        #if author_span!=None:
        #    author = str(author_span.get_text()).replace("\n"," ")

        return article, author


scraper = usaToday()