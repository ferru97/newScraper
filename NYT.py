from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import html as html_es
import time

def slowInput(element,speed, text):
    for character in text:
        element.send_keys(character)
        time.sleep(speed)


class NYT:
    def __init__(self):
        self.login_required = True
        self.name = "nytimes.com"

        self.email = "elsajuliani93@gmail.com"
        self.psw = "project@2020"

    
    def botDetected(self,html):
        soup = BeautifulSoup(html, "html.parser")
        chapta = soup.find('span[aria-labelledby="recaptcha-accessible-status"]')
        if chapta != None:
            input("Bot detected! Solve the chapta and press ENTER")


    def login(self,driver):
        result = None
        main_page = "https://www.nytimes.com/"
        driver.get(main_page)
        time.sleep(4)

        login_btn = driver.find_element_by_xpath('//a[@data-testid="login-link"]')
        if login_btn != None:
            driver.get(login_btn.get_attribute("href"))
            username_in = driver.find_element_by_xpath('//input[@id="username"]')
            psw_in = driver.find_element_by_xpath('//input[@id="password"]')
            if username_in!=None and psw_in!=None:
                #time.sleep(4)
                #slowInput(username_in,0.5,self.email)
                #time.sleep(1.5)
                #slowInput(psw_in,0.5,self.psw)
                #psw_in.send_keys(Keys.ENTER)
                input("Log in and press ENTER:")
                return driver

        return result
    
    def getArticle(self,html):
        article = "NA"
        author = "NA"

        soup = BeautifulSoup(html, "html.parser")
        article_tag = soup.find("article")

        if article_tag!=None:
            article = str(article_tag.get_text()).replace("\n"," ")
        
        author_span = soup.find("span", {"class": "css-1baulvz last-byline"})
        if author_span!=None:
            author = str(author_span.get_text()).replace("\n"," ")

        return article, author


scraper = NYT()