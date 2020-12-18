import os
import time
import Utils
import sys
import usaToday
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

def main(filename, scraper, website):
    print("Scraping "+website)
    dataset_path = os.path.join(Utils.dataset_folder,filename)
    df = pd.read_csv(dataset_path, error_bad_lines=False, index_col=False)
    df["Author"] = "--"
    df["Article"] = "--"

    dir_path = os.path.dirname(os.path.realpath(__file__))
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    driver = webdriver.Chrome(executable_path=os.path.join(dir_path, "chromedriver"), chrome_options=options)
    
    k = 1
    totla = len(df.index)
    for index, row in df.iterrows(): #add if already scraped continue 
        printProgressBar(k,totla)
        try:
            driver.get(row["url"])
            body = driver.find_element_by_tag_name("body")
            html = str(body.get_attribute('innerHTML'))
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
        if "usatoday-com" in file:
            main(file, usaToday.scraper, "usatoday.com")

    print("Done!")