import sqlite3
import string
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from datetime import date

# beginning of the url we want to get the lists of metal bands from
list_url = "https://www.metal-archives.com/lists/"
# the url ends with letter A-Z depending on the first letter of the band's name
alphabet = list(string.ascii_uppercase)
# besides letters A-Z there are also sites for bands beginning with numbers or special characters
alphabet.extend(["NBR", "~"])

# connect to database
conn = sqlite3.connect('metal-archives.db')

# set up the webdriver we need using web scraping with selenium
path = "chromedriver.exe"
driver = webdriver.Chrome(path)

# loop through all urls alphabetical
for letter in alphabet:
    web = list_url + letter
    driver.get(web)  # open website in the browser
    time.sleep(5)  # load the website's content takes some time

    # searching the html for the tag in braces (which includes band names and url to band's url)
    band_list_object = driver.find_elements_by_xpath("//tbody/tr/td/a")

    # website is split up in tables you have to click through, the first table should not be skipped
    first_site = True

    while True:
        if not first_site:
            try:
                # looking if there button to click on the next site
                tag = "//a[@class='next paginate_button']"
                next_site = driver.find_element_by_xpath(tag)
            except:
                # if there is no button (no more table for the first letter's website) break the loop
                break

            # clicking the "next" button to get to the next table and get its band data (name and url)
            next_site.click()
            time.sleep(5)
            band_list_object = driver.find_elements_by_xpath("//tbody/tr/td/a")
        else:
            # set variable to False so that the loop is not skipped again
            first_site = False

        for band in band_list_object:
            # band name and url from the tables collected in the loops above
            band_name = band.text
            url = band.get_attribute('href')

            # scraping the band's info site using the beautifulsoup library
            url_request = requests.get(url)  # send request to the website
            content = url_request.text  # get the html content
            soup = BeautifulSoup(content, "lxml")  # making the soup
            band_info = soup.find(id="band_info")  # find the tag with all the data
            band_stats = band_info.find_all("dd")  # create a list of all the data

            # assign the stripped data strings dto variables
            country_of_origin = band_stats[0].text.strip()
            location = band_stats[1].text.strip()
            status = band_stats[2].text.strip()
            formed_in = band_stats[3].text.strip()
            genre = band_stats[4].text.strip()
            lyrical_themes = band_stats[5].text.strip()
            current_label = band_stats[6].text.strip()
            years_active = band_stats[7].text.strip()
            data_retrieved = date.today().strftime("%d/%m/%Y")

            # store variables in list
            data = [band_name, url, country_of_origin, location, status,
                    formed_in, genre, lyrical_themes, current_label, years_active, data_retrieved]

            # insert the data in the database
            conn.execute('''INSERT INTO band_info (band_name, url, country_of_origin, location, status, 
                                  formed_in, genre, lyrical_themes, current_label, years_active, data_retrieved)
                                          VALUES (?,?,?,?,?,?,?,?,?,?,?);''', data)

            # commit the new data set to the database
            conn.commit()

# close webdriver/browser
driver.quit()

# disconnect database
conn.close()
