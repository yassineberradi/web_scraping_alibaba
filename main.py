from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time

from selenium.webdriver.common.by import By
# header = {
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
#     "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
# }
#
# response = requests.get("https://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en&CatId=&SearchText=paracord&viewtype=&tab=", headers=header)
#
# data = response.text
# soup = BeautifulSoup(data, "html.parser")
chrome_driver_path = "//chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(
    "https://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en&CatId=&SearchText=paracord&viewtype=&tab=")
html = driver.page_source
time.sleep(2)
soup = BeautifulSoup(html, "html.parser")
all_link_elements = soup.select(".elements-title-normal")
all_links = []
for link in all_link_elements:
    href = link["href"]
    print(href)
    all_links.append(href)
all_title_elements = soup.select(".elements-title-normal")
all_titles = [title.get_text() for title in all_title_elements]

all_price_elements = soup.select(".elements-offer-price-normal__promotion")
all_prices = [price.get_text() for price in all_price_elements]

all_ranking_elements = soup.select(".seb-supplier-review-gallery-test__score")
all_ranking = [price.get_text() for price in all_ranking_elements]
print(f"title: {all_titles}; prices: {all_prices}; ranking:  {all_ranking}")

for n in range(len(all_links)):
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSf3iTXNiALCqCfHbZean7tSfnpaP6-D34ewl2XRFGgWP1moOA/viewform?usp=sf_link")
    time.sleep(2)
    title = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    ranking = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')

    title.send_keys(all_titles[n])
    price.send_keys(all_prices[n])
    ranking.send_keys(all_ranking[n])
    link.send_keys(all_links[n])
    submit_button.click()
