from bs4 import BeautifulSoup
import html as html_es
from Utils import text4csv


class cnbc:
    def __init__(self):
        self.login_required = False
        self.name = "cnbc.com"
    
    def getArticle(self,html):
        article = "NA"
        author = "NA"

        soup = BeautifulSoup(html, "html.parser")

        article_tag = soup.find("div",{"class":"ArticleBody-articleBody"})
        if article_tag!=None:
            article = ""
            div_groups =  article_tag.find_all("div",{"class":"group"}, recursive=False)
            for d in div_groups:
                for p in d.find_all("p", recursive=False):
                    article += text4csv(p.get_text())
        else: #is a video
            video_desc_div = soup.find("div",{"class":"ClipPlayer-clipPlayerIntroSummary"})
            if video_desc_div!=None:
                article = text4csv(video_desc_div.get_text())
                

        author_a = soup.find("div", {"class": "Author-author"})
        if author_a!=None:
            author = text4csv(author_a.get_text())

        return article, author

    def botDetected(self,html):
        return


scraper = cnbc()