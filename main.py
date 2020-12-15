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

def main(filename, scraper):
    dataset_path = os.path.join(Utils.dataset_folder,filename)
    df = pd.read_csv(dataset_path, error_bad_lines=False)
    df["Article"] = "--"

    dir_path = os.path.dirname(os.path.realpath(__file__))
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    driver = webdriver.Chrome(executable_path=os.path.join(dir_path, "chromedriver"), chrome_options=options)
    
    for _, row in df.iterrows():
        try:
            driver.get(row["url"])
            body = driver.find_element_by_tag_name("body")
            html = str(body.get_attribute('innerHTML'))
        except:
            continue
        article = scraper.getArticle(html)    
        time.sleep(wait_time)


if __name__ == "__main__":
    for file in os.listdir(Utils.dataset_folder):
        if "usatoday-com" in file:
            main(file, usaToday.scraper)