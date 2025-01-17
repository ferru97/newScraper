import os
import time
import Utils
import sys
import usaToday
import CNN
import foxNews
import theStreet
import yahoo
import cnbc
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

def main(filename, scraper, start, end):
    print("Scraping "+scraper.name)
    dataset_path = os.path.join(Utils.dataset_folder,filename)
    df = pd.read_csv(dataset_path, error_bad_lines=False, index_col=False)
    if 'Article' not in df.columns:
        df["Author"] = "--"
        df["Article"] = "--"
    if 'Video' not in df.columns and "cnbc" in scraper.name:
        df["Video"] = "--"


    if start==None:
        start = 0
        end = len(df.index)

    dir_path = os.path.dirname(os.path.realpath(__file__))
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    options.add_argument("--log-level=3");
    driver = webdriver.Chrome(executable_path=os.path.join(dir_path, "chromedriver"), chrome_options=options)
     
    cookies_accepted = False
    count = 0 
    k = 1
    totla = end-start+2
    for index, row in df.iterrows():
        if index<start or index>end:
            continue

        count += 1
        if count>99:
            print("Saveing..")
            df.to_csv(dataset_path, encoding='utf-8-sig', index=False) 
            count = 0

        k += 1
        printProgressBar(k,totla)
        if row["Article"] not in ["NA", "--"]:
            continue
        try:
            driver.get(row["url"])
            if scraper.name=="cnbc.com":
                if "video.cnbc.com" in row["url"]:
                    df.loc[index,"Video"] = "True"
                else:
                    df.loc[index,"Video"] = "False"

            if scraper.name in ["yahoo.com"] and cookies_accepted==False:
                scraper.acceptCookies(driver)
                cookies_accepted = True
                time.sleep(wait_time)
            
            body = driver.find_element_by_tag_name("body")
            html = str(body.get_attribute('innerHTML'))
            scraper.botDetected(html)
            article, author = scraper.getArticle(html)
        except Exception as e:
            print("Error: "+str(e))
            continue
        df.loc[index,"Article"] = article
        df.loc[index,"Author"] = author

        time.sleep(wait_time)

    df.to_csv(dataset_path, encoding='utf-8-sig', index=False) 


if __name__ == "__main__":
    print(sys.argv)
    if len(sys.argv)==2:
        start = None
        end = None
    else:
        start = int(sys.argv[2])-1
        end = int(sys.argv[3])-1

    web_source = sys.argv[1]
    for file in os.listdir(Utils.dataset_folder):
        if "usatoday" in file and web_source=="1":
            main(file, usaToday.scraper, start, end)
        if "cnn" in file and web_source=="2":
            main(file, CNN.scraper, start, end)
        if "foxnews" in file and web_source=="3":
            main(file, foxNews.scraper, start, end)
        if "yahoo" in file and web_source=="4":
            main(file, yahoo.scraper, start, end)
        if "thestreet" in file and web_source=="5":
            main(file, theStreet.scraper, start, end)
        if "cnbc" in file and web_source=="6":
            main(file, cnbc.scraper, start, end)

    print("Done!")