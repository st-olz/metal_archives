import sqlite3
import string
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from datetime import date

list_url = "https://www.metal-archives.com/lists/"
alphabet = list(string.ascii_uppercase)
alphabet.extend(["NBR", "~"])

conn = sqlite3.connect('metal-archives.db')

path = "chromedriver.exe"
driver = webdriver.Chrome(path)

for letter in alphabet:
    web = list_url + letter
    driver.get(web)
    time.sleep(5)

    band_list_object = driver.find_elements_by_xpath("//tbody/tr/td/a")

    first_site = True

    while True:
        if not first_site:
            try:
                tag = "//a[@class='next paginate_button']"
                next_site = driver.find_element_by_xpath(tag)
            except:
                break

            next_site.click()
            time.sleep(5)
            band_list_object = driver.find_elements_by_xpath("//tbody/tr/td/a")
        else:
            first_site = False

        for band in band_list_object:
            band_name = band.text
            url = band.get_attribute('href')

            url_request = requests.get(url)
            content = url_request.text
            soup = BeautifulSoup(content, "lxml")
            band_info = soup.find(id="band_info")
            band_stats = band_info.find_all("dd")

            country_of_origin = band_stats[0].text.strip()
            location = band_stats[1].text.strip()
            status = band_stats[2].text.strip()
            formed_in = band_stats[3].text.strip()
            genre = band_stats[4].text.strip()
            lyrical_themes = band_stats[5].text.strip()
            current_label = band_stats[6].text.strip()
            years_active = band_stats[7].text.strip()
            data_retrieved = date.today().strftime("%d/%m/%Y")

            data = [band_name, url, country_of_origin, location, status,
                    formed_in, genre, lyrical_themes, current_label, years_active, data_retrieved]

            conn.execute('''INSERT INTO band_info (band_name, url, country_of_origin, location, status, 
                                  formed_in, genre, lyrical_themes, current_label, years_active, data_retrieved)
                                          VALUES (?,?,?,?,?,?,?,?,?,?,?);''', data)
            conn.commit()

driver.quit()

conn.close()
