import os
import time
import Utils
import sys
import usaToday
import NYT
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

wait_time = 2

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    if iteration == total: 
        print()

def main(filename, scraper):
    print("Scraping "+scraper.name)
    dataset_path = os.path.join(Utils.dataset_folder,filename)
    df = pd.read_csv(dataset_path, error_bad_lines=False, index_col=False)
    df["Author"] = "--"
    df["Article"] = "--"

    dir_path = os.path.dirname(os.path.realpath(__file__))
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    driver = webdriver.Chrome(executable_path=os.path.join(dir_path, "chromedriver"), chrome_options=options)

    if scraper.login_required==True:
        print("Login required...")
        driver = scraper.login(driver)
        if driver == None:
            print("Error: unable to login!")
            return
        print("Logged in successfully!")
     
    k = 1
    totla = len(df.index)
    for index, row in df.iterrows(): #add if already scraped continue 
        printProgressBar(k,totla)
        try:
            driver.get(row["url"])
            body = driver.find_element_by_tag_name("body")
            html = str(body.get_attribute('innerHTML'))
            scraper.botDetected(html)
            article, author = scraper.getArticle(html)
        except Exception as e:
            print(e)
            continue
        df.loc[index,"Article"] = article
        df.loc[index,"Author"] = author
        k += 1
        time.sleep(wait_time)

    df.to_csv(dataset_path, encoding='utf-8-sig', index=False) 


if __name__ == "__main__":

    for file in os.listdir(Utils.dataset_folder):
        if "usatoday-com" in file and sys.argv[1]=="1":
            main(file, usaToday.scraper)
        if "nytimes-com" in file and sys.argv[1]=="2":
            main(file, NYT.scraper)

    print("Done!")